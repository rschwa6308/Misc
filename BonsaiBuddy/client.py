import requests
import threading, time
import logging
from random import random


mock_response_body = {
    'batch_number': 538,
    'events': [
        {
            'time': time.time() + 10,   # 10 seconds from program start
            'type': 'water_plant',
            'volume': '25ml'
        },
        {
            'time': time.time() + 30,   # 30 seconds from program start
            'type': 'refill_tray',
            'volume': '10ml'
        },
    ],
    'status': 'scheduled'   # scheduled, in_progress, success, failure, canceled
}

# set logging output format
logging.basicConfig(level=logging.INFO, format='%(threadName)s (%(thread)s):\t%(message)s')


# minium amount of time between event executions (seconds)
EVENT_EXECUTION_PERIOD = 2

# amount of time between GET/POST requests (seconds)
BATCH_UPDATE_PERIOD = 10 * 60   # every 10 minutes


class Client:
    def __init__(self):
        self.quit_event = threading.Event()
        self.events_worker = None
        self.status_updates_worker = None
        self.execution_lock = threading.RLock()

        self.active_batches = []
        self.last_completed_batch_number = None
    
    # add the given batch to the active batch pool
    def add_batch(self, batch):
        for event in batch['events']:
            event['status'] = 'scheduled'    # scheduled, in_progress, success, failure
        self.active_batches.append(batch)

    # remove the given a batch from the active batch pool
    def remove_batch(self, batch):
        self.active_batches.remove(batch)
    
    # execute the given event; return an error message if execution fails
    def execute_event(self, event):
        logging.info(f'Executing event: {event}... ')
        time.sleep(10)
        error_message = None
        if error_message is None:
            logging.info('Event executed successfully')
        else:
            logging.error(f'Event failed with error message: {error_message}')
        return error_message
    
    # download the next batch from the server
    def get_batch_update(self):
        mock_response = requests.get('https://postman-echo.com/get')
        if mock_response.ok:
            logging.info('Update downloaded successfully')
        else:
            logging.error(f'Failed to download update with status code: {mock_response.status_code} ({mock_response.reason})')
        return mock_response_body
    
    # upload current batch status to the server
    def post_batch_update(self, batch):
        logging.info(f'Posting update for batch #{batch["batch_number"]}...')
        status_update = {
            'batch_number': batch['batch_number'],
            'status': batch['status'],
            'events': [event['status'] for event in batch['events']],
            'error_messages': [event['error_message'] if 'error_message' in event else None for event in batch['events']]
        }
        mock_response = requests.post('https://postman-echo.com/post', data=status_update)
        if mock_response.ok:
            logging.info('Batch update posted successfully')
        else:
            logging.error(f'Failed to post results with status code: {mock_response.status_code} ({mock_response.reason})')
    
    def post_sensor_update(self):
        logging.info(f'Posting sensor update...')
        status_update = {
            'moisture_level': random()
        }
        mock_response = requests.post('https://postman-echo.com/post', data=status_update)
        if mock_response.ok:
            logging.info('Sensor update posted successfully')
        else:
            logging.error(f'Failed to post results with status code: {mock_response.status_code} ({mock_response.reason})')

    def _run_events(self):
        time.sleep(1)   # allow self.start() to finish gracefully
        while not self.quit_event.is_set():
            # logging.info('Checking event queue...')
            current_time = time.time()
            for batch in self.active_batches:
                for event in batch['events']:
                    if event['time'] <= current_time and event['status'] == 'scheduled':
                        if batch['status'] == 'scheduled':          # set batch status to in_progress (if first event)
                            batch['status'] = 'in_progress'
                        event['status'] = 'in_progress'
                        # acquire lock before executing event to prevent interruption
                        with self.execution_lock:
                            error_message = self.execute_event(event)
                        if error_message is None:
                            event['status'] = 'success'
                        else:
                            event['status'] = 'failure'
                            event['error_message'] = error_message
                        # post results and discard batch if exhausted
                        if all(event['status'] in ('success', 'failure') for event in batch['events']):
                            batch_number = batch['batch_number']
                            logging.info(f'Batch #{batch_number} completed')
                            batch['status'] = 'success' if all(event['status'] == 'success' for event in batch['events']) else 'failure'
                            self.post_batch_update(batch)
                            self.remove_batch(batch)
                            self.last_completed_batch_number = batch_number
                # logging.info('Done')
            self.quit_event.wait(EVENT_EXECUTION_PERIOD)
    
    def _run_updates(self):
        time.sleep(1)   # allow self.start() to finish gracefully
        while not self.quit_event.is_set():
            # GET batch updates from server (after waiting for any in_progress events to finish executing)
            with self.execution_lock:
                logging.info('Checking for batch updates...')
                batch = self.get_batch_update()
                batch_number = batch['batch_number']
                active_batch_numbers = [b['batch_number'] for b in self.active_batches]
                if batch_number not in active_batch_numbers and batch_number != self.last_completed_batch_number:
                    num_events = len(batch["events"])
                    logging.info(f'New batch found: #{batch_number} ({num_events} event{"s" if num_events > 1 else ""})')
                    self.add_batch(batch)
                else:
                    logging.info('No updates found')
            
            # POST status update to server (after waiting for any in_progress events to finish executing)
            with self.execution_lock:
                # logging.info('Posting status update...')
                for batch in self.active_batches:
                    self.post_batch_update(batch)
                self.post_sensor_update()
                # logging.info('Done')
            
            self.quit_event.wait(BATCH_UPDATE_PERIOD)
    
    def start(self):
        self.quit_event.clear()
        self.events_worker = threading.Thread(target=self._run_events, name='EventsWorker')
        self.status_updates_worker = threading.Thread(target=self._run_updates, name='UpdatesWorker')
        self.events_worker.start()
        self.status_updates_worker.start()
        logging.info(f'Client started with worker threads "{self.events_worker.name}" ({self.events_worker.ident}) and "{self.status_updates_worker.name}" ({self.status_updates_worker.ident})')
    
    def stop(self):
        logging.info('Stopping all workers...')
        self.quit_event.set()
        logging.info('Done')



def main():
    client = Client()
    client.start()
    time.sleep(60)
    client.stop()

if __name__ == '__main__':
    main()

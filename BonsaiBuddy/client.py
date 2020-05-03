import requests
import time
import threading
import logging


mock_response_body = {
    'batchNumber': 538,
    'events': [
        {
            'time': time.time() + 20,   # 20 seconds from program start
            'type': 'water_plant',
            'volume': '25ml'
        },
        {
            'time': time.time() + 45,   # 45 seconds from program start
            'type': 'refill_tray',
            'volume': '10ml'
        },
    ]
}

# set logging output format
logging.basicConfig(level=logging.INFO, format='%(threadName)s (%(thread)s):\t%(message)s')


# minium amount of time between event executions (seconds)
EVENT_EXECUTION_PERIOD = 2

# amount of time between GET requests (seconds)
BATCH_UPDATE_PERIOD = 10 * 60   # every 10 minutes

class Client:
    def __init__(self):
        self.event_queue = []
        self.quit_event = threading.Event()
        self.events_worker = None
        self.updates_worker = None
        self.last_batch = None
    
    def enqueue_event(self, event):
        self.event_queue.append(event)

    def dequeue_event(self, event):
        self.event_queue.remove(event)
    
    def execute_event(self, event):
        logging.info(f'Executing event: {event}... ')
        time.sleep(1)
        error_message = None
        if error_message is None:
            logging.info('Event executed successfully')
        else:
            logging.error(f'Event failed with error message: {error_message}')
    
    def fetch_batch_updates(self):
        return mock_response_body
    
    def _run_events(self):
        time.sleep(1)   # allow self.start() to finish gracefully
        while not self.quit_event.is_set():
            # logging.info('Checking event queue...')
            current_time = time.time()
            for event in self.event_queue:
                if event['time'] <= current_time:
                    self.execute_event(event)
                    self.dequeue_event(event)
            # logging.info('Done')
            self.quit_event.wait(EVENT_EXECUTION_PERIOD)
    
    def _run_updates(self):
        time.sleep(1)   # allow self.start() to finish gracefully
        while not self.quit_event.is_set():
            logging.info('Checking for batch updates...')
            batch = self.fetch_batch_updates()
            if self.last_batch is None or batch['batchNumber'] != self.last_batch['batchNumber']:
                num_events = len(batch["events"])
                logging.info(f'New batch found: #{batch["batchNumber"]} ({num_events} event{"s" if num_events > 1 else ""})')
                self.last_batch = batch
                for event in batch['events']: self.enqueue_event(event)
            else:
                logging.info('No updates found')
            self.quit_event.wait(BATCH_UPDATE_PERIOD)
    
    def start(self):
        self.quit_event.clear()
        self.events_worker = threading.Thread(target=self._run_events, name='EventsWorker')
        self.updates_worker = threading.Thread(target=self._run_updates, name='UpdatesWorker')
        self.events_worker.start()
        self.updates_worker.start()
        logging.info(f'Client started with worker threads "{self.events_worker.name}" ({self.events_worker.ident}) and "{self.updates_worker.name}" ({self.updates_worker.ident})')
    
    def stop(self):
        logging.info('Stopping all workers...')
        self.quit_event.set()
        logging.info('Done')



def main():
    client = Client()
    client.start()
    time.sleep(90)
    client.stop()

if __name__ == '__main__':
    main()

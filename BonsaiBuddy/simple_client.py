import requests
from requests.compat import urljoin
import json
import threading, time
import logging
from random import random


# mock_response_body = {
#     'batch_number': 538,
#     'events': [
#         {
#             'time': time.time() + 10,   # 10 seconds from program start
#             'type': 'water_plant',
#             'volume': '25ml'
#         },
#         {
#             'time': time.time() + 30,   # 30 seconds from program start
#             'type': 'refill_tray',
#             'volume': '10ml'
#         },
#     ],
#     'status': 'scheduled'   # scheduled, in_progress, success, failure, canceled
# }

# set logging output format
logging.basicConfig(level=logging.INFO, format='%(threadName)s (%(thread)s):\t%(message)s')


# minium amount of time between event executions (seconds)
EVENT_EXECUTION_PERIOD = 10

# amount of time between GET/POST requests (seconds)
BATCH_UPDATE_PERIOD = 10 * 60   # every 10 minutes


BASE_URL = 'http://127.0.0.1:8000/'
TASKS_UPDATE_URL = urljoin(BASE_URL, 'next_tasks/')
SENSOR_UPDATE_URL = urljoin(BASE_URL, 'sensor_update/')
TASK_NOTIFICATION_URL = urljoin(BASE_URL, 'notify_task/')
UPLOAD_PASSWORD = 'password'


class Client:
    def __init__(self):
        self.quit_event = threading.Event()
        self.events_worker = None
        self.status_updates_worker = None
        self.execution_lock = threading.RLock()

        self.scheduled_tasks = {}

    # execute the given command; return an error message if execution fails
    def execute_command(self, command):
        logging.info(f'Executing command: {command}... ')
        time.sleep(10)
        error_message = None
        if error_message is None:
            logging.info('Event executed successfully')
        else:
            logging.error(f'Event failed with error message: {error_message}')
        return error_message
    
    # download the next tasks from the server
    def get_tasks_update(self):
        response = requests.get(TASKS_UPDATE_URL)
        if response.ok:
            logging.info('Update downloaded successfully')
        else:
            logging.error(f'Failed to download update with status code: {response.status_code} ({response.reason})')
        return json.load(response.content)
    
    def post_sensor_update(self):
        logging.info('Reading sensor values... ')
        status_update = {
            'password': UPLOAD_PASSWORD,
            'sensors': [
                {
                    'sensor_name': 'test sensor',
                    'value': random(),
                    'time': round(datetime.datetime.today().timestamp()),
                },
                {
                    'sensor_name': 'test sensor 2',
                    'value': random(),
                    'time': round(datetime.datetime.today().timestamp()),
                }
            ]
        }
        logging.info('done')
        logging.info('Posting sensor update... ')
        
        response = requests.post(SENSOR_UPDATE_URL, data=status_update)
        if response.ok:
            logging.info('Sensor update posted successfully')
        else:
            logging.error(f'Failed to post sensor update with status code: {response.status_code} ({response.reason})')
    
    def notify_task_completed(self, task):
        logging.info('Posting task completion notification... ')
        status_update = {
            'task_id': task['task_id'],
            'completion_time': round(time.time().timestamp())
        }
        requests.post(TASK_NOTIFICATION_URL, data=status_update)
        logging.info('done')

    def _run_tasks(self):
        time.sleep(1)   # allow self.start() to finish gracefully
        while not self.quit_event.is_set():
            # logging.info('Checking event queue...')
            current_time = time.time()
            for task in self.scheduled_tasks:
                if task['next_time'] <= current_time:
                    with self.execution_lock:
                        self.execute_command(task['command'])
                        self.notify_task_completed(task)
                        self.scheduled_tasks.remove(task)
            self.quit_event.wait(EVENT_EXECUTION_PERIOD)
    
    def _run_updates(self):
        time.sleep(1)   # allow self.start() to finish gracefully
        while not self.quit_event.is_set():
            # GET batch updates from server (after waiting for any in-progress commands to finish executing)
            with self.execution_lock:
                logging.info('Checking for task updates...')
                response = requests.get(TASKS_UPDATE_URL)
                self.scheduled_tasks = response['scheduled_tasks']  # TODO...
            
            # TODO: this entire block vvv
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
        logging.info('done')



def main():
    client = Client()
    client.start()
    time.sleep(60)
    client.stop()

if __name__ == '__main__':
    main()

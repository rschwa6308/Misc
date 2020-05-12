import requests, json
import datetime


UPLOAD_PASSWORD = 'password'

data = {
    'password': UPLOAD_PASSWORD,
    'sensors': [
        {
            'sensor_name': 'test sensor',
            'value': 0.696,
            'time': round(datetime.datetime.today().timestamp()),
        },
        {
            'sensor_name': 'test sensor 2',
            'value': 0.123,
            'time': round(datetime.datetime.today().timestamp()),
        }
    ]
}
response = requests.post('http://127.0.0.1:8000/sensor_update/', json=data)

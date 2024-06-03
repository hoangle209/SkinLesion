import requests
import json

http_host = "http://192.168.6.115:3336/api/events"

image_path = "/home/thanh/noisy_image.png"

dict_data = {
    'deviceId': 1,
    'type': 'ND_DoiTuong',
    # 'data': {
    #     'types': ['person', 'person', 'person', 'person'],
    #     'colors': ['blue', 'blue', 'blue', 'blue']
    # },
    'data': json.dumps({
        'types': ['person', 'person', 'person', 'person'],
        # 'colors': ['blue', 'blue', 'blue', 'blue']
    }),
    'aiId': 2,
    'time': '2024-02-05 10:31:50.891848+00'
}
try:
    response = requests.post(
        http_host,
        files={'images': ('test.jpg', open(image_path, "rb"), "image/jpeg"), },
        data=dict_data,
    )
    print(response.json())
except Exception as e:
    print("Error", e)

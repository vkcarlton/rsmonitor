import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('GOVEE_API_KEY')

# url1 = "https://openapi.api.govee.com/router/api/v1/device/control"

# headers1 = {
#     "Govee-API-Key": api_key,
#     "Content-Type": "application/json"
# }

# data1 = {
#     "requestId": "uuid",
#     "payload": {
#         "sku": "H6076",
#         "device": "83:CF:C3:30:38:35:4D:92",
#         "capability": {
#             "type": "devices.capabilities.on_off",
#             "instance": "powerSwitch",
#             "value": 0
#         }
#     }
# }

# res = requests.post(url1, headers=headers1, json=data1)

# print(res.status_code)


# url2 = "https://openapi.api.govee.com/router/api/v1/user/devices"

# headers2 = {
#     "Govee-API-Key": api_key,
#     "Content-Type": "application/json"
# }
# res = requests.get(url2, headers=headers2)

# print(res.status_code)
# if res.status_code == 200:
#     print(json.dumps(res.json(), indent=4))

from govee_api_ble import GoveeDevice
my_device = GoveeDevice("83:CF:C3:30:38:35:4D:92")
my_device.setPower(True)
my_device.setPower(False)
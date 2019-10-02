import requests
import os

r = requests.get(os.environ['STF_API_URL'], headers={'Authorization': f"Bearer {os.environ['STF_TOKEN']}"})

data = r.json()

for device in data['devices']:
    if device['present'] and device['remoteConnectUrl']:
        device_name=f"{device['manufacturer']}-{device['model']}-sdk{device['sdk']}-{device['version']}-{device['abi']}"
        port=device['remoteConnectUrl'].split(':')[1]
        command=f"python tests/test_first.py \"{device_name}\" 192.168.1.207:{port}"
        print(command)
        os.system(command)

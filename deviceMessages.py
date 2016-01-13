import requests
import os
from requests.auth import HTTPBasicAuth

user = os.getenv('API_USER')
password = os.getenv('API_PASSWORD')
deviceId = os.getenv('DEVICEID')

url = 'https://backend.sigfox.com/api/devices/'+deviceId+'/messages'

r = requests.get(url, auth=HTTPBasicAuth(user, password))
print r.status_code
print r.text

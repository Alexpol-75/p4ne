
import ssl
import requests
import pprint
import urllib3

host_url = "https://10.31.70.210:55443"

from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

class Ssl1HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLSv1)

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

s = requests.Session()
s.mount("https://10.31.70.210:55443", Ssl1HttpAdapter())

r = s.get("https://10.31.70.210:55443", verify=False)
#print(r.status_code)

r = s.post(host_url + "/api/v1/auth/token-services", auth=("restapi","j0sg1280-7@"), verify=False)
#print(r.status_code)

token = r.json()['token-id']
header = {"content-type": "application/json", "X-Auth-Token": token}
r = s.get(host_url + '/api/v1/interfaces', headers=header, verify=False)
#pprint.pprint(r.json())

#stat = s.get(host_url + '/api/v1/interfaces/GigabitEthernet1/statistics', headers=header, verify=False)
#pprint.pprint(stat.json())

int_packets = dict()
for i in r.json()['items']:
    int_name = (i['if-name'])
    stat = s.get(host_url + '/api/v1/interfaces/' + int_name + '/statistics', headers=header, verify=False)
    int_packets[int_name] = stat.json()['in-total-packets']

for k in int_packets:
    print('"' + k + '" total packets:', int_packets[k])
#print(int_name, 'total packets:', stat.json()['in-total-packets'])



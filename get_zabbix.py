import json
import requests

url = 'http://129.211.93.125/zabbix/api_jsonrpc.php'
post_headers = {'Content-Type': 'application/json'}
post_data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip"
        ]
    },
    "id": 2,
    "auth": "1f3a4aa49480b8ee6c4ef854cc6d2646"
}

ret = requests.post(url, data=json.dumps(post_data), headers=post_headers)
print(ret.text)

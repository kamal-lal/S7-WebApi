import http.client
import json
import ssl
import time

PLC_IP = "192.168.0.15"
USER_NAME = "admin"
PASSWORD = "Siemens100"


conn = http.client.HTTPSConnection(PLC_IP, context = ssl._create_unverified_context())

headers = {'Content-Type': 'application/json'}

payload_login = json.dumps({
    "jsonrpc": "2.0",
    "method": "Api.Login",
    "id": 10,
    "params": {
        "user": USER_NAME,
        "password": PASSWORD
    }
})

conn.request("POST", "/api/jsonrpc", payload_login, headers)

login_res = conn.getresponse()
login_data = json.loads(login_res.read())
token = login_data["result"]["token"]

headers["X-Auth-Token"] = token

id = 20

while True:
    payload_read = json.dumps({
        "jsonrpc": "2.0",
        "method": "PlcProgram.Read",
        "id": id,
        "params": {
            "var": "\"mem\".value[1]"
        }
    })

    conn.request("POST", "/api/jsonrpc", payload_read, headers)

    read_res = conn.getresponse()
    read_data = json.loads(read_res.read())
    value = read_data["result"]

    print(f"Result from ID no. {read_data["id"]} : {value}.")

    id = id + 1
    time.sleep(1.0)


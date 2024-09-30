import http.client
import json
import ssl

conn = http.client.HTTPSConnection("192.168.0.15",context=ssl._create_unverified_context())

payload = json.dumps({
  "jsonrpc": "2.0",
  "method": "Api.Version",
  "id": 20
})

headers = {
  'Content-Type': 'application/json'
}

conn.request("POST", "/api/jsonrpc", payload, headers)

res = conn.getresponse()

data = json.loads(res.read())
print(data)
# print(data.decode("utf-8"))
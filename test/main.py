print "send request"

import httplib, urllib

root = {}
root["action_name"] = "QR_LIMIT_SCENE"

scene_id = {}
scene_id["scene_id"] = 1000

scene = {}
scene["scene"] = scene_id

root["action_info"] = scene
params = urllib.urlencode(root)

#https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=TOKEN
url = "api.weixin.qq.com"

conn = httplib.HTTPSConnection(url)
conn.request("POST", "/cgi-bin/qrcode/create?access_token=0807136895fce8fbe4f929b0d72a6a1m", params)

response = conn.getresponse()
print response.status, response.reason, response.read()

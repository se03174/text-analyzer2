
#-*- coding:utf-8 -*-
#동음이의어 정보 
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/Homonym"
accessKey = "e307a6dd-d1ee-4123-8c43-5956d1e396c3"
word = "배"
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "word": word
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode]" + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))
                                  

#-*- coding:utf-8 -*-
#단어 어휘 분석 api 
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/Word"
accessKey ="e307a6dd-d1ee-4123-8c43-5956d1e396c3"
word = "꽃"
 
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
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))
                                 
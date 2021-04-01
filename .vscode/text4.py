
#-*- coding:utf-8 -*-
#어휘 간 유사도 분석 api 
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/WordRel"
accessKey = "e307a6dd-d1ee-4123-8c43-5956d1e396c3"
firstWord = '수영'
firstSenseId = 'FIRST_SENSE_ID'
secondWord = '오리발'
secondSenseId = 'SECOND_SENSE_ID'
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        'first_word': firstWord,
        #'first_sense_id': firstSenseId,
        'second_word': secondWord,
        #'second_sense_id': secondSenseId
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
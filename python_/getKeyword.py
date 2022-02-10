import os
import sys
import urllib.request
import pandas as pd
import json
import re
import time
import random
import requests
import pandas as pd
import signaturehelper
import operator
client_id = "QLp09VOgdjmFi6J0QHPZ"
client_secret = "GRF88BMtYM"
input_data = input("검색 질의: ")
query = urllib.parse.quote(input_data)
idx = 0
display = 100
start = 1
end = 1000

web_df = pd.DataFrame(columns=['Title'])

for start_index in range(start, end, display):
    url = "https://openapi.naver.com/v1/search/webkr?query=" + query \
        + "&display=" + str(display) \
        + "&start=" + str(start_index)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    # 응답받을때
    if(rescode == 200):
        response_body = response.read()
        response_dict = json.loads(response_body.decode('utf-8'))
        items = response_dict['items']
        for item_index in range(0, len(items)):
            remove_tag = re.compile('<.*?>')
            title = re.sub(remove_tag, '', items[item_index]['title'])
            # link = items[item_index]['link']
            # description = re.sub(remove_tag, '', items[item_index]['description'])
            web_df.loc[idx] = [title]
            idx += 1
    else:
        print("Error Code:" + rescode)

web_df.to_csv('{}.txt'.format(input_data), sep='\t', index=False)

file = open('{}.txt'.format(input_data),"r",encoding="utf-8")

text = file.read()

wordList = text.split()

wordCount = {}

# 특수문자 숫자 알파벳 거르기
# word.isalnum() and not word.isdigit() and alphabet.find(word[0])==-1 and 
for word in wordList:
    if word[-2:] == "축제":
        wordCount[word] = wordCount.get(word,0)+1

sortedWordCount = sorted(wordCount.items(), key=operator.itemgetter(0))

festival = list(wordCount.keys())

def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(
        timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8',
            'X-Timestamp': timestamp, 'X-API-KEY': API_KEY,
            'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}


BASE_URL = 'https://api.naver.com'
API_KEY = '0100000000412fe7ec7b54506df13f3000c2a1ba1cca156095ae0ad5f4d7466058628e8149'
SECRET_KEY = 'AQAAAABBL+fse1RQbfE/MADCobocpcZt7CZZqYIlnXl69WhkYw=='
CUSTOMER_ID = '2363828'

uri = '/keywordstool'
method = 'GET'


for i in festival[:5]:
    r = requests.get(BASE_URL + uri+'?hintKeywords={}&showDetail=1'.format(i),
        headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))
    df = pd.DataFrame(r.json()['keywordList'])
    df.rename({'compIdx': '경쟁정도',
            'monthlyAveMobileClkCnt': '월평균클릭수_모바일',
            'monthlyAveMobileCtr': '월평균클릭률_모바일',
            'monthlyAvePcClkCnt': '월평균클릭수_PC',
            'monthlyAvePcCtr': '월평균클릭률_PC',
            'monthlyMobileQcCnt': '월간검색수_모바일',
            'monthlyPcQcCnt': '월간검색수_PC',
            'plAvgDepth': '월평균노출광고수',
            'relKeyword': '연관키워드'}, axis=1, inplace=True)
    df = df[['연관키워드', '월간검색수_PC', '월간검색수_모바일',
            '월평균클릭수_PC', '월평균클릭수_모바일',
            '월평균클릭률_PC', '월평균클릭률_모바일',
            '경쟁정도', '월평균노출광고수']]
    print(df.head())

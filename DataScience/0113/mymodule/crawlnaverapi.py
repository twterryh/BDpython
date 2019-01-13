import requests
from urllib.parse import quote

def get1000Result(keyword):
    list = []
    for num in range(0, 10):
        list = list + call(keyword, num * 100 + 1)['items']
    return list
    
def call(keyword, start): #몇 번부터 시작할 지를 입력값으로.
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100" + "&start=" + str(start)
    result = requests.get(url = url, 
                          headers={"X-Naver-Client-Id": "ECHV86pScmsxBJZTnSVs", 
                                   "X-Naver-Client-Secret": "12HmTNDqIs"
                          })
    print(result)
    return result.json()

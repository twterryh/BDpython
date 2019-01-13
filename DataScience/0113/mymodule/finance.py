import requests
from bs4 import BeautifulSoup

def finance(number):
    url = 'https://finance.naver.com/item/main.nhn?code='+number
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content,'html.parser')

    no_today = bs_obj.find('p',{'class':'no_today'})

    blind_now = no_today.find('span',{'class':'blind'})

    return blind_now.text

def updown(number):
    url = 'https://finance.naver.com/item/main.nhn?code='+number
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content,'html.parser')

    a = bs_obj.find('td',{'class':'first'})

    aa = a.find('span',{'class':'blind'})

    return aa.text


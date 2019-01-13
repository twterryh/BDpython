# pwd : C:\Users\pc\Desktop\terry\0113
# module : C:\Users\pc\Desktop\terry\0113\mymodule

import requests

def crawl(url):
    result = requests.get(url)
    return result.content
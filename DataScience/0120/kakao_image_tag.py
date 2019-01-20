import sys

import argparse

import requests
# connect to network

from PIL import Image, ImageDraw, ImageFont
# draw (on) image

from io import BytesIO 
# image 를 byte 로 읽는 library

API_URL = 'https://kapi.kakao.com/v1/vision/multitag/generate'
MYAPP_KEY = '6dfff849a1fcd94ae6703e8e636b6883'

def generate_tag(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        result = resp.json()['result']
        if len(result['label_kr']) > 0:
            if type(result['label_kr'][0]) != str:
                result['label_kr'] = map(lambda x: str(x.encode("utf-8")), result['label_kr'])
            print("이미지를 대표하는 태그는 \"{}\"입니다.".format(','.join(result['label_kr'])))
        else:
            print("이미지로부터 태그를 생성하지 못했습니다.")

    except Exception as e:
        print(str(e))
        sys.exit(0)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Classify Tags')
    parser.add_argument('image_url', type=str, nargs='?',
        default="http://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/08.jpg",
        help='image url to classify')

    args = parser.parse_args()

    generate_tag(args.image_url)
  

# RESULT >> 이미지를 대표하는 태그는 "사람,여러사람,전자제품,여성"입니다.
import sys

import argparse

import requests
# connect to network

from PIL import Image, ImageDraw, ImageFont
# draw (on) image

from io import BytesIO 
# image 를 byte 로 읽는 library

# 인증 정보 ---------------------------------------------------------------------
API_URL = 'https://kapi.kakao.com/v1/vision/product/detect'
MYAPP_KEY = '6dfff849a1fcd94ae6703e8e636b6883'

# 상품 추출 함수 -----------------------------------------------------------------
def detect_product(image_url):
    headers = {'Authorization':'KakaoAK {}'.format(MYAPP_KEY)}
    try :
        data = {'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        print(resp.json())
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)
    
# JSON 파일 형태로 넘겨진 결과값 처리 함수 -----------------------------------------
def show_products(image_url, detection_result):
    try:
        image_resp = requests.get(image_url)    # image 에 대한 정보
        image_resp.raise_for_status()
        file_jpgdata = BytesIO(image_resp.content)  # image 정보만 byte 로 가져오기
        image = Image.open(file_jpgdata)        # image 를 열람함 -> 박스 그릴 준비
    except Exception as e:
        print(str(e))
        sys.exit(0)


    draw = ImageDraw.Draw(image)
    for obj in detection_result['result']['objects']:
        x1 = int(obj['x1']*image.width)
        y1 = int(obj['y1']*image.height)
        x2 = int(obj['x2']*image.width)
        y2 = int(obj['y2']*image.height)
        draw.rectangle([(x1,y1), (x2, y2)], fill=None, outline=(255,0,0,255))
        draw.text((x1+5,y1+5), obj['class'], (255,255,0))   # class 에 물체 이름들 있음
    del draw

    return image

# --------------------------------- 실제 실행 -----------------------------------
if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Dectect Products.')
    # parser analyzes objects/arguments
    
    parser.add_argument('image_url', type=str, nargs='?',
                        default="http://img.allurekorea.com/allure/2016/05/style_5747de654ddc2-683x1024.jpg",
                        help='')
    
    args = parser.parse_args()
    
    # 상품 추출 함수
    detection_result = detect_product(args.image_url)
    
    # JSON 파일 형태로 넘겨진 결과값 처리 함수
    image = show_products(args.image_url, detection_result)
    image.show()
    
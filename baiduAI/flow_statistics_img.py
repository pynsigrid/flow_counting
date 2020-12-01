import requests
import base64
import json

'''
人流量统计
'''


def save_base_image(img_str,filename):

    img_data = base64.b64decode(img_str)
    with open(filename, 'wb') as f:
        f.write(img_data)
    return


request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"
# 二进制方式打开图片文件
f = open('/Users/panyining/PycharmProjects/video_processing/test_img.jpg', 'rb')
img = base64.b64encode(f.read())
img_name = 'result.png'

params = {"image": img,
          "show": True}
access_token = '24.242e7e4428c9b54d6c203fd133b877d8.2592000.1609119362.282335-23057366'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:

    # response = response.decode('utf-8')
    # data = json.loads(response)
    person_num = response.json().get('person_num')
    print('person_num', person_num)
    img_str = response.json().get('image')
    save_base_image(img_str, img_name)




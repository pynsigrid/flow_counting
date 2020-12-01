import os
import urllib
from urllib.request import urlopen
import re
import base64
import numpy as np
import cv2

img_path = "/Users/panyining/PycharmProjects/video_processing/test_video2"

# 读文件夹下的jpg
images = os.listdir(img_path)
images = sorted(images) # shape: 1920*888
request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_tracking"

# 便利图片
for i in images:
    f = open(img_path + '/' + i, 'rb')
    try:
        img = base64.b64encode(f.read())
        params = {"area": "1, 1, 500, 1, 888, 1000, 1, 888", "case_id": 1, "case_init": "false", "dynamic": "true",
                  "image": img, "show": "true"}
        params = urllib.parse.urlencode(params).encode("utf-8")
        # 官方代码是python2我的是py3 其中urllib有蛮大的差多的，请自己如果跑不通请自己百度
        access_token = '24.242e7e4428c9b54d6c203fd133b877d8.2592000.1609119362.282335-23057366'
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urlopen(request)
        content = response.read().decode('utf-8')

        if content:
            print(i)
            print(content)
            # 返回的内容很蛋疼，返回的content是一个str，其中有in和out，但是这个in和out是指的当前帧的in和out，不会自动累加，
            # 我是在选择参数那里加上了show = true，会返回一个很长的base64的图片格式信息，在网上找格式转换，在图片中，它的in和out回自动累加
            # 一开始只能手动的粘贴复制，去网上查看返回的图片，最后写了代码，可以直接批量保存读取
            # 试着用正则化来提取image的base64编码段，这里的正则化还有待加强，暂时先这样吧（就是懒），正则化不常用，每次都忘记
            # 这里的正则化的目的主要是读取返回的base64的信息，来图像化。
            relink = '"image": "(.*)",'
            info = re.findall(relink, content)
            # 这里用opencv来显示base64的图像
            str_to_bytes = bytes(info[0], encoding="utf8")
            img_b64decode = base64.b64decode(str_to_bytes)  # base64解码

            img_array = np.fromstring(img_b64decode, np.uint8)  # 转换np序列
            img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)  # 转换Opencv格式
            # 保存在自己的文件夹下
            cv2.imwrite('/Users/panyining/PycharmProjects/video_processing/result_test_video3/' + i, img)

            # cv2.imshow("img", img)
            # cv2.waitKey(100)

            request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_tracking"

    except:
        print('find .DS_Store!!!')
        continue

#人数预警例代码

#filename:原图片名（本地存储包括路径）；resultfilename:处理后的文件保存名称(每个人打标)

#warningnum告警人数

# def crowd_num_warning(filename,resultfilename,warningnum):
#
#     person_num=body_num(filename,resultfilename)  # body_num统计area内人数
#
#     if person_num>warningnum:
#
#         warningmessage="警告：人数过于拥挤，最大人数"+str(warningnum)+"，当前人数:"+str(person_num)
#
#         print(warningmessage)
#
#         # 增加其他预警处理代码，比如将信息通过短信，APP发布给相关人
#
# crowd_num_warning('crowd2.jpg','crowd2_num.jpg',30)
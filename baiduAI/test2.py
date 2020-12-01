import cv2
# from utils import image_processing
import numpy as np

image_path = "/Users/panyining/PycharmProjects/video_processing/test_video2/7_35.jpg"
res = cv2.imread(image_path)
# print(res.shape)
p1, p2 = (1, 1), (1920, 888)

cv2.rectangle(res, p1, p2, (255, 0, 0), thickness=2)
while True:
    # cv2.setMouseCallback('image',)
    # cv2.startWindowThread()  # 加在这个位置
    cv2.imshow('image', res)
    key = cv2.waitKey(0)
    if key == 13 or key == 32:  # 按空格和回车键退出
        break
cv2.destroyAllWindows()


import cv2
import os
import numpy as np
import argparse
import time
import imutils
from imutils.video import FPS
from imutils.video import VideoStream

in_path = r'/Users/panyining/PycharmProjects/video_processing/people-counting-opencv/videos/example_01.mp4'
out_path = r'/Users/panyining/PycharmProjects/video_processing/blue-line-challenge/output/example_01_out.avi'
# cap = cv2.VideoCapture('/Users/panyining/PycharmProjects/video_processing/blue-line-challenge/video/output_01.avi')

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default=in_path,
                help="path to optional input video file")
ap.add_argument("-o", "--output", type=str, default=out_path,
                help="path to optional output video file")

args = vars(ap.parse_args())


fps = FPS().start()
i = 1
height = 0
old_frame = np.ones((372, 500, 3), dtype=np.uint8)
old_frame[:, :, 0] = 0
old_frame[:, :, 1] = 0
old_frame[:, :, 1] = 0

# if not os.path.exists(out_path):
#     os.makedirs(out_path)

if not args.get("input", False):
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    time.sleep(2.0)
else:
    print("[INFO] opening video file...")
    vs = cv2.VideoCapture(args["input"])

writer = None
W = None
H = None

# while (cap.isOpened()):
while True:
    frame = vs.read()
    frame = frame[1] if args.get("input", False) else frame

    # ret, frame = cap.read()  # ret是bool型，当读完最后一帧就是False，frame是ndarray型
    # if ret == False:  #
    #     break
    # print(frame.shape)  # gif(331, 420, 3), camera(280, 500, 3) 22(1920, 888, 3)

    frame = imutils.resize(frame, width=500)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if W is None or H is None:
        (H, W) = frame.shape[:2]
    if args["output"] is not None and writer is None:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(args["output"], fourcc, 30,
                                 (W, H), True)

    frame[:height, :, :] = old_frame[:height, :, :]
    line = frame[height:height + 1, :, :]


    if writer is not None:
        writer.write(frame)
    # frame[height:height + 1, :, 0] = 240  # B
    # frame[height:height + 1, :, 1] = 127  # G
    # frame[height:height + 1, :, 2] = 0  # R
    # time.sleep(1.0)
    # frame[height:height + 1, :, :] = line

    # cv2.imencode('.jpg', frame)[1].tofile(out_path + 'frame_' + str(i) + '.jpg')  # 路径含中文存图
    cv2.imshow('frame', frame)

    i += 1
    height += 3
    # print(f'i, height = {i}, {height}')


    old_frame = frame


    # 不加这一句，由于计算速度极快，直接会显示到最后一帧
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 检测到按下q，就break。waitKey(1)相当于1ms延时
        break
    # totalFrames += 1  # 跳帧
    fps.update()

fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
if writer is not None:
    writer.release()
if not args.get("input", False):
    vs.stop()
else:
    vs.release()

# cv2.waitKey(0)
# cap.release()
cv2.destroyAllWindows()

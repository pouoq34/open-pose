#train을 위해 영상을 이미지로 분할!
import cv2

vidcap = cv2.VideoCapture('C:/Users/user/PycharmProjects/pose/video/train_video1.mov')
success, image = vidcap.read()
count = 1
success = True

while success:
    success, image = vidcap.read()
    cv2.imwrite("C:/Users/user/PycharmProjects/pose/image/%d.jpg" % count, image)
    print("saved image %d.jpg" % count)

    if cv2.waitKey(10)==27:
        break
    count +=1

import cv2 
# 영상이 있는 경로
vidcap = cv2.VideoCapture('/home/kjjgo35/PythonHome/Image/video/[mix]세번째 영상_WT.mkv')
count = 0
while(vidcap.isOpened()):
    try:
        ret, image = vidcap.read()
        # 이미지 사이즈 960x540으로 변경
        image = cv2.resize(image, (960, 540), cv2.INTER_AREA)
        if(ret and int(vidcap.get(1)) % 30 == 0):
            print('Saved frame number : ' + str(int(vidcap.get(1))))
            # 추출된 이미지가 저장되는 경로
            cv2.imwrite("/home/kjjgo35/PythonHome/Image/image/fish%d.png" % count, image)
            count += 1

    except Exception as e:
        print(str(e)) 
        
vidcap.release()

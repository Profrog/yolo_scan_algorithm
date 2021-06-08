
* camera.py : 파이썬 웹캠 제어(바코드 인식 가능)
* camera1.py : camera.py의 가벼운 버전(웹캠 제어만 가능)
* convert.py : gnss 장비 파싱 프로그램
* gnss_convert.py : convert.py의 가벼운 버전
* graham_scan(matplot + bresenham).py : grahamscan으로 얻어낸 점의 좌표를 채우는 것 까지 가능한 파일
* graham_scan(matplot).py : 랜덤한 크기와 개수를 이용하여 grahamscan 알고리즘 검증용 파일
* graham_scan.py : graham scan으로 점의 좌표만 얻애내는 파일(가벼운 버전)
* yolo_webcam.py : in darket it can realtime-yolo-detecting
* rosyolo : yolo 데이터 값을 ros2에 올린다.
* yolo_webcam.py : 웹캠으로 얻어낸 실시간 이미지를 yolo로 검출하여 그 결과 값을 보여준다
* crawling.py : .txt의 내용들을 크롤링 하여 이미지로 저장
* crawling(auto).py : crawling. update 버전
* sir2020_serial.py : sir2020값을 .txt로 로깅 
* sir2020_map.py : .txt로 로깅된 sir2020값을 matplot형태로 보여줌
* coco_divide.py : image + annotation(yolo) 기준에서 특정 라벨을 가진 이미지만 추출
* label_match.py : annotaion이 있는 이미지만 save 해주는 코드
* pluslabel.py : 데이터셋에서 다른 weights에 있는 label 중 해당 names와 일치하는 것들은 추가 라벨링을 해주는 프로그램
* train_txt.py : 해당 파일의 이미지 경로(.jpg)를 모아 train.txt를 만들어준다
* precision.py : 해당 묶음의 dataset에 있는 사진들을 yolo를 돌려 class 별 검출률을 조사한다.
* serial.py : serial 값을 받는 python 코드
* chanage_label.py : data set의 yolo annotation label 번호를 수정하는 코드
* extract_image.py : 영상에서 n장의 사진을 추출해 내는 코드
* precision2.py : class 별 검출률 조사 + 검출 표시 iamge를 다른 폴더에 저장한다

# yolo_scan_algorithm

# 구현 순서

0. gramham 알고리즘 구현(포인트를 잘 집어내는지 확인)

1. 단일 bresenham 알고리즘 구현 및 graham scan algortihm와의연결(알고리즘 이해 및 변수목록, 함수 헤더 바꾸어보면서) c++로 작성
return : int(두 좌표가 주어졌을 때 함수가 지나가는 block의 개수)

2. 복합 bresenham 알고리즘 구현(알고리즘 이해 및 변수목록, 함수 헤더 바꾸어보면서) c++로 작성
return : int(여러 좌표(vector<int>가 주어졌을 때 함수가 지나가는 block의 개수))

3. 영역 탐지 : bresenham 응용 : 연이어진 좌표들을 bresenham으로 연결하면서 만들어지는 도형의 안쪽 값들을 1로 선이 지나지
않는 바깥쪽은 0으로 만듦 c++
return : vector<int,int> or vector<bool, bool>

4. python 번역 : 박사님의 알고리즘 평가를 받은 후 python으로 번역

------------------------------------------------------------------

# 참조

0. https://www.acmicpc.net/problem/1708
0. https://huiung.tistory.com/141

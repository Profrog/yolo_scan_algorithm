
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

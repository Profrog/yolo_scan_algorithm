
* camera.py : webcam control python code
* yolo_webcam.py : in darket it can realtime-yolo-detecting
* rosyolo : yolo 데이터 값을 ros2에 올린다.
* convert.py : .txt 로깅 데이터 추출용 

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

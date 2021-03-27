#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

//Convex hull(볼록 껍질) 연습

struct pos {
	long long x, y;
};

pos v[100010];
int N; //얼마나 많은 점일 것인가
int M; //얼마나 넓은 좌표체계

stack<pos> s;/// 점들의 좌표가 쌓이는 container
vector<pos> s1; // 오리지널 데이터
vector<pos> s2; // 남겨진 데이터
vector<vector<int>> data0;


void print1()
{
	cout << endl;

	for (int x = 0; x < M; x++)
	{
		for (int y = 0; y < M; y++)
		{
			cout << data0[x][y] << " ";
		}

		cout << endl;
	}

	cout << endl;
}

bool comp_y(pos a, pos b) {

	if (a.y != b.y)	return a.y < b.y;
	else return a.x < b.x;
}

long long ccw(pos a, pos b, pos c) { //ccw
	return a.x * b.y + b.x * c.y + c.x * a.y - (b.x * a.y + c.x * b.y + a.x * c.y);
}


bool comp_c(pos a, pos b) { //반시계 정렬

	long long cc = ccw(v[0], a, b);
	if (cc != 0) return cc > 0; // 각도 작은 순
	else return (a.x + a.y) < (b.x + b.y); //일직선 있을경우 좌표가 작은
}

void algorithm()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	//main 함수 위의 입력예시 부분 참조
	cout << "M값 입력 (0,0) ~ (M,M) " << endl;
	cin >> M;
	cout << "좌표영역은 0,0 에서 " << M << "," << M << "까지" << endl;



	cout << "N값 입력" << endl;
	cin >> N;
	cout << "N개의 점의 x,y 값 입력" << endl;
	for (int i = 0; i < N; i++) {
		cin >> v[i].x >> v[i].y;
		s1.push_back(v[i]);
	}

	//---------------------------
	sort(v, v + N, comp_y);
	sort(v + 1, v + N, comp_c);

	s.push(v[0]);
	s.push(v[1]);
	pos first, second;


	for (int i = 2; i < N; i++) {
		while (s.size() >= 2) {
			second = s.top();
			s.pop();
			first = s.top();
			if (ccw(first, second, v[i]) > 0) { //좌회전
				s.push(second);
				break;
			}

		}
		s.push(v[i]);
	}

	//여기 까지가 점 정하기

	data0.assign(M, vector<int>(M, 0));

	while(s.size() > 0){
		s2.push_back(s.top());
		s.pop();
	}
	
	for (int x = 0; x < s2.size(); x++)
	{
		data0[s2[x].x][s2[x].y] = 1;
	}

	print1();
	
	//cout << s2.size();

	//making map

	// cout << endl;
	//cout << s.size();

}



/* 입력예시
 
5 
8
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2

*/


int main(void) {
	
	algorithm();
	return 0;
}

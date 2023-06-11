'''
https://level.goorm.io/exam/152114/%ED%98%84%EB%8C%80%EB%AA%A8%EB%B9%84%EC%8A%A4-%EC%98%88%EC%84%A0-dead-or-arrive/quiz/1
시간복잡도 O(n)
공간복잡도 O(n)
입력된 차량에 대한 선형적인 복잡도를 갖는다
'''

import sys
n = int(sys.stdin.readline())  # input보다 속도가 빠름 # input과 혼용 불가능
memo = {}  # 속도: (내구도, 차량번호)
answer = 0

for i in range(n):
	v, w = map(int, sys.stdin.readline().split())
	if not memo.get(v):
		memo[v] = [w,i+1]
		answer += i+1
		continue
	if memo[v][0] <= w:
		answer -= memo[v][1]
		memo[v] = [w, i+1]
		answer += i+1

print(answer)
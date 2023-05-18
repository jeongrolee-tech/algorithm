'''
https://school.programmers.co.kr/learn/courses/30/lessons/17679
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
2 ≦ n, m ≦ 30
board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
'''

# 시간복잡도 O(m^2 * n)
# 공간복잡도 O(m * n)


def solution(m, n, board):
    dic = {(-1, -1)}  # 제거 대상"만"
    answer = 0

    board = [list(row) for row in board]  # 전처리 (문자열은 불변성)

    while dic:  # 턴
        dic = set()
        for i in range(m - 1):
            for j in range(n - 1):
                cur = board[i][j]
                if cur != ' ' and cur == board[i][j + 1] == board[i + 1][j + 1] == board[i + 1][j]:
                    dic.add((i, j))
                    dic.add((i, j + 1))
                    dic.add((i + 1, j + 1))
                    dic.add((i + 1, j))

        answer += len(dic)
        for x, y in dic:
            board[x][y] = ' '  # 제거 대상 블록들을 "한번에" 제거

        # 모든 열에 대해 블록을 내리는 과정을 반복합니다.
        for _ in range(m):  # m번 반복
            for j in range(n):  # 각 열에 대해
                for i in range(m-1, 0, -1):  # 아래쪽부터 위쪽으로
                    if board[i][j] == ' ' and board[i-1][j] != ' ':  # 내릴게 있으면
                        board[i][j], board[i - 1][j] = board[i -
                                                             1][j], ' '  # 블록 한칸식 내리기

    return answer

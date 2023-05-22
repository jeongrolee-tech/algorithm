# 시간복잡도 O(n^2)
# 공간복잡도 O(n^2)
'''
https://leetcode.com/problems/pascals-triangle/
1 <= numRows <= 30

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

행마다 숫자가 점점 늘어나는 것을 볼 수 있습니다. 이런 규칙성 때문에 파스칼의 삼각형을 만들 때는 이전 행의 정보를 활용합니다.
코드에서 시간 복잡도는 모든 원소를 한 번씩 처리하므로 O(n^2)이며, 공간 복잡도도 모든 원소를 저장하므로 O(n^2)입니다. 여기서 n은 파스칼의 삼각형의 행의 수입니다.
간단히 말하면, 파스칼의 삼각형을 만드는 것은 각 숫자를 계산하고 저장하는 작업을 반복하는 것이므로, 시간 복잡도와 공간 복잡도 모두 행의 수에 따라 제곱에 비례하여 증가합니다.
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        answer = [[1]]
        while len(answer) < numRows:
            last_row = answer[-1]
            new_row = [1]
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row.append(1)
            answer.append(new_row)

        return answer

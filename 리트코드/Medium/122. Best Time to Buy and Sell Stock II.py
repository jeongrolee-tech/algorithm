'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=featured-list&envId=top-interview-questions

#그리디

이 문제의 핵심은 주식 가격이 오르는 "모든 시점"에 주식을 사고 파는 것 입니다
각 단계에서 이익을 최대화 하므로 전체이익도 최대화 됩니다

1. 주식 가격 배열을 처음부터 끝까지 반복합니다
2. 현재 날짜의 주식 가격이 다음 날의 주식 가격보다 낮다면, 주식을 사고 다음날에 팝니다
3. 이 과정을 배열의 끝까지 반복합니다

- 시간복잡도
    - O(n)
        - why?
            - 반복문이 입력값으로 들어오는 prices 의 원소들의 갯수에 비례해서 실행되기 때문
- 공간복잡도
    - O(1)
        - why?
            - 입력배열 외에는 상수 공간만 사용하기 때문
        - profit
            - 사칙연산만 수행하므로 상수
        - i
            - 1씩 증가만 되므로 상수
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            # i day
            # 다음날이 있고, 오늘가격이 다음날보다 저렴하면: 매수
            if i < len(prices)-1 and prices[i] < prices[i+1]:
                profit -= prices[i]
            if i-1 >= 0 and prices[i] > prices[i-1]:  # 전날이 있고, 오늘가격이 전날보다 올랐으면: 매도
                profit += prices[i]
        return profit

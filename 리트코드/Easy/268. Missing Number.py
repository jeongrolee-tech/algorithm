'''
- 문제링크
    - https://leetcode.com/problems/missing-number/description/?envType=featured-list&envId=top-interview-questions
- 한줄평
    - 
- 접근방법
    - **수학적 접근법:** 0부터 **`n`**까지의 모든 숫자의 합을 계산하고, 이 값에서 주어진 배열의 모든 원소의 합을 뺀 값이 빠진 숫자입니다. 0부터 **`n`**까지의 합은 가우스 공식 `n * (n + 1) / 2`을 사용하여 쉽게 계산할 수 있습니다.
    - **XOR 연산을 이용한 접근법:** XOR 연산은 동일한 숫자에 대해 두 번 적용되면 원래의 숫자를 0으로 만드는 특징이 있습니다. 이 특징을 이용하여, 0부터 **`n`**까지의 모든 숫자와 배열의 모든 원소에 대해 XOR 연산을 수행합니다. 이렇게 하면 배열에 없는 빠진 숫자만 남게 됩니다. 이 방법은 **추가적인 메모리 공간 없이** 문제를 해결할 수 있으며, 시간 복잡도는 O(n)입니다.
        - `xor` 변수를 초기화 할때 max(nums) 가 아닌 len(nums) 를 사용하는 이유?
            - 주어진 배열은 0부터 **`n`**까지의 수 중에 하나가 빠진 형태입니다. 그런데 배열의 길이는 빠진 수를 제외한 **`n`**개의 숫자가 있기 때문에 len(nums)는 **`n`**이 됩니다. 다시 말해, 0부터 **`n`**까지의 수 중 하나가 빠졌기 때문에 배열의 길이는 **`n`**이 됩니다.
                
                반면 max(nums)는 배열 내의 최대값이므로 빠진 숫자에 따라 **`n`**이 될 수도 있고, **`n-1`**이 될 수도 있습니다.
                
                따라서 이 문제에서는 len(nums)를 사용하여 0부터 **`n`**까지의 숫자를 대상으로 XOR 연산을 수행합니다.
                
    - 키워드
        - 배열
        - **XOR**
            - XOR 연산은 같은 숫자를 두 번 적용하면 0을 반환합니다. 즉, **`a XOR a = 0`**.
            - 0과 어떤 숫자를 XOR 연산하면 그 숫자를 반환합니다. 즉, **`0 XOR a = a`**.
            - XOR 연산은 순서에 구애받지 않습니다. 즉, **`a XOR b XOR c = a XOR c XOR b`**.
        - 수학적 접근법
            - n까지의 합
                - **가우스 정리**
- 시간복잡도
    - XOR 접근법
        - O(n)
            - 입력값의 길이에 비례하여 반복문을 실행하기 때문
    - 수학적 접근법
        - O(n)
            - 입력값의 길이에 비례하여 반복문을 실행하기 때문
- 공간복잡도
    - XOR 접근법
        - O(1)
            - 입력값의 길이와 무관하게 항상 일정한 공간을 사용하기 때문
                - `xor` , `i`
    - 수학적 접근법
        - O(1)
            - 입력값의 길이와 무관하게 항상 일정한 공간을 사용하기 때문
                - `n` , `gsum`
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # mathematical formula (gauss)
        n = len(nums)
        gsum = n * (n + 1) // 2  # 가우스 공식
        for num in nums:
            gsum -= num
        return gsum

        # XOR
        xor = len(nums)
        for i, num in enumerate(nums):
            xor = xor ^ num ^ i  # XOR 연산은 같은 숫자끼리 만나면 0이 된다
        return xor

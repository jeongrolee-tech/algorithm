# 정수인 두 자연수 사이의 최대공약수
def euclidean(a, b):
    if a % b == 0:
        return b

    return euclidean(b, a % b)

def solution(gems):
    # 투 포인터 정의
    # set 정의
    import collections
    unique_set = set(gems)
    m = len(unique_set)  # unique set 길이
    n = len(gems)  # 배열의 길이

    l = 0
    r = l + m-1  # 최소 여기서 시작

    # 원소 순회하며 인덱스 기록
    idx_dic = collections.defaultdict(list)
    check_dic = dict()
    for i, elem in enumerate(gems):
        idx_dic[elem].append(i)
        check_dic[elem] = False
    print(idx_dic, check_dic)

    def check(arr, a, b):
        count = 0
        for i in range(a, b+1):
            if check_dic[arr[i]] == False:
                count += 1
                check_dic[arr[i]] == True
        print(count)

        return count

    min_l = n
    min_r = n
    while l < n and r < n:

        if check(gems, l, r) == m:  # 최소한 모든걸 한개 다 가지고 있을 경우
            # 추가로 탐색 줄일 수 있는지
            if l < min_l:
                min_l = l
            l = l+1

        else:  # 부족할경우 범위 확장
            r = r+1

    #     answer = []
    return [l+1, r+1]

import copy


def solution(gems):
    start, end = 1, len(gems)
    category = set(gems)
    while True:
        if set(gems[start-1:end-1]) == category:
            end -= 1
            continue
        elif set(gems[start:end]) == category:
            start += 1
        else:
            break

    return [start, end]


def solution(gems):
    category = set(gems)
    end = 0
    short = [0, 100000]

    def dfs(start, idx, willBuy):
        nonlocal end
        if idx == len(gems) or idx-start > short[1]-short[0]:
            end = -1
            return
        if gems[idx] in willBuy:
            willBuy.remove(gems[idx])
        if not willBuy:
            end = idx
            return
        return dfs(start, idx+1, willBuy)

    for start in range(len(gems)):
        willBuy = copy.deepcopy(category)
        dfs(start, start, willBuy)
        if end == -1:
            continue
        if short[1]-short[0] > end-start:
            short = [start, end]
        if end-start == len(category):
            break
    return [short[0]+1, short[1]+1]

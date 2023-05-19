def k_numeral_system(num, k):
    convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 10진법 이상인 경우의 처리를 위해 필요함

    if num < k:
        return convert_string[num]
    else:
        return k_numeral_system(num // k, k) + convert_string[num % k]


def k_numeral_system(num: int, k: int):
    convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 10진법 이상인 경우의 처리를 위해 필요함
    answer = ''

    while num > 0:
        q, r = divmod(num, k)
        answer += str(convert_string[r])
        num = q

    return answer[::-1]

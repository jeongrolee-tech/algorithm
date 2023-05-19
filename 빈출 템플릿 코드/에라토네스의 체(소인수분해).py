def eratones(num):
    i = 2
    prime_numbers = []

    while i * i <= num:
        if num % i == 0:
            num //= i
            prime_numbers.append(i)
        else:
            i += 1

    if num > 1:
        prime_numbers.append(num)

    return prime_numbers

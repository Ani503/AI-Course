def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** num_len
        temp //= 10
    return total == n


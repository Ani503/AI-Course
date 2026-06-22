def is_perfect(n):
    if n < 2:
        return False
    total = 0
    i = 1
    while i <= n // 2:
        if n % i == 0:
            total += i
        i += 1
    return total == n



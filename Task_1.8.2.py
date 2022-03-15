def sqrt_3(m):
    n = 1
    for i in range(20):
        n = ((m / (n ** 2)) + (2 * n)) / 3
        if abs(n ** 3 - m) <= 0.001:
            return n

print(sqrt_3(1000))
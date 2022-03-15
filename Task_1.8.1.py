def sqrt(m):
    n = 1
    while True:
        n = (n + (m / n)) / 2
        if abs(n ** 2 - m) <= 0.001:
            print(n ** 2)
            print(abs(n ** 2 - m))
            return n

print(sqrt(100))
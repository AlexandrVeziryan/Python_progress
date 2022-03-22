# Iterative

def f(n):
    if n < 3:
        return n
    a = 0
    b = 1
    c = 2
    res = 0
    for _ in range(3, n + 1):
        res = a + b + c
        a, b, c = b, c, res
    return res

print(f(5))

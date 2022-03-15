def power(a, b):
    if a == 0:
        print("Error")
        return None
    elif b == 0 and not a == 0:
        return 1    
    n = 1
    for _ in range(abs(b)):
        n *= a

    if b > 0:
        return n
    return 1 / n

print(power(-2, 6))
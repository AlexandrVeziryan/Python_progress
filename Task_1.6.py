def summ(a, b):
    summ = 0
    while a < b:
        summ += a
        a += 1
    return summ    

def foo(a, b):
    if b > a:
        return summ(a, b)    
    return summ(b, a)

print(foo(9, 6))       



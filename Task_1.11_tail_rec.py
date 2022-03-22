# Վարժություն 1.11
# f ֆունկցիան սահմանվում է հետևայլ կերպ.
# f(n) = n, եթե n < 3
# f(n) = f(n - 1) + f(n - 2) + f(n - 3), եթե n >= 3
# n-ը կարող է լինել միայն 0 և դրական ամբողջ թիվ։ Իրականացրեք լուծումը ռեկուրսիվ, իտերատիվ և պոչավոր ռեկուրսիվ տարբերակներով։

# Tail recursion
def f(n, res):
    if n < 3:
        return n + res
    return f(n - 1, res) + f(n - 2, res) + f(n - 3, res)    

print(f(5, 0))



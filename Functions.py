def fnc1(a,b):
    result = a * b
    return result

x = fnc1(5,5)
print(x)

x = 10
factorial = 1
for i in range(1, x + 1):
    factorial *= i
    print(factorial)
print('result: ', str(factorial))
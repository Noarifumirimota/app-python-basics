n = 5
# 1.
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(factorial)
print('result: ' + str(factorial))

print('\n')

# 2.
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
    print(factorial)
print('result: ' + str(factorial))
# The upper limit of the loop is excluded.
for i in range(1,5):
    print(i)

# Arr loop.
arr1 = [2,4,8,16]
for element in arr1:
    print(element)

print('\nWhile\n')

stop = False
while stop == False:
    i += 1
    print(i)
    if i >= 5:
        stop = True

print('\n')

i = 0
stop = False
while not stop:
    i += 1
    print(i)
    if i >= 5:
        stop = True
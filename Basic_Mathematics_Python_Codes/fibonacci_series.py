num = int(input('Enter number for fibonacci series :'))

a = 0
b = 1

if num <= 0:
    print('Please enter valid positive number')
elif num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(num-2):
        c = a + b
        print(c)
        a = b
        b = c

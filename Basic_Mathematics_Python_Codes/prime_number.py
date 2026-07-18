num = int(input('enter a number :'))
count = 0
for i in range(num):
    if i == 1 or i == 0:
        print(f'{i} is a not prime number.')
        continue
    flag = False
    for j in range(2, (i//2) + 1) :
        if i % j == 0:
            flag = True
            break
        else:
            flag = False

    if flag:
        print(f'{i} is not a prime number.')
    else:
        count += 1
        print(f'{i} is a prime number')
print(f'Total prime number in range of {num} are {count}.')

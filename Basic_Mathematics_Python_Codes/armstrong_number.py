n = 10
count = 0
while n < 10000000:
    total = 0
    total_length = 0
    count_num = n
    while count_num != 0:
        total_length += 1
        count_num //= 10

    count_num = n
    while count_num != 0:
        number = count_num % 10
        total += number ** total_length
        count_num //= 10

    if total == n:
        print('armstrong number ', n)
        count += 1

    n += 1

print(f'total armstrong numbers are : {count}')

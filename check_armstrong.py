n = 153
num = n
counter = 0
while num > 0:
    last_digit = num % 10
    counter += 1
    num = num // 10
num = n
result = 0
while num > 0:
    last_digit = num % 10
    result = result + last_digit ** counter
    num = num // 10
if result == n:
    print('armstrong')
else:
    print('not armstrong')
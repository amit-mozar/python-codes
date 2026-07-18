a = int(input('enter number 1 : '))
b = int(input('enter number 2 : '))

if a > b:
    bigger = a
else:
    bigger = b
count = 1
while True:
    c = bigger * count
    if c % a == 0 and c % b == 0:
        lcm = c
        break
    else:
        count += 1

print(f'LCM of {a} and {b} is : {c}')

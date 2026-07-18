a = int(input('enter number 1 : '))
b = int(input('enter number 2 : '))

if a > b:
    bigger = a
else:
    bigger = b
for i in range(bigger, 2, -1):
    if a % i == 0 and b % i == 0:
        print(f'GCD is {i}')
        break
        

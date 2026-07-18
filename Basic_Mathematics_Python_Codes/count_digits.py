num = int(input('Enter an integer: '))
n = abs(num)
if n == 0:
  counter = 1
else:
  counter = 0
  while n > 0:
    counter += 1
    n = n // 10
print(counter)

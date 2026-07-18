#method 1 - brute force
n = int(input("Enter the number: "))
num = n
all_factors = []
for i in range(1, num+1):
  if num % i == 0:
    all_factors.append(i)

# Method 2 - better than brute force
all_factors = []
for i in range(1, num // 2 + 1):
  if num % i == 0:
    all_factors.append(i)
all_factors.append(num)

#method 3 - optimal
from math import sqrt
all_factors = []
total = int(sqrt(num))
for i in range(1, total + 1):
  if num % i == 0:
    all_factors.append(i)
    if num // i != i:
      all_factors.append(num // i)
print(all_factors)

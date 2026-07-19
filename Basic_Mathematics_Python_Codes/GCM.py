a = int(input('enter number 1 : '))
b = int(input('enter number 2 : '))

# method 1 -- brute force
if a > b:
    bigger = a
else:
    bigger = b
for i in range(bigger, 2, -1):
    if a % i == 0 and b % i == 0:
        print(f'GCD is {i}')
        break
        
# method 2 - better than brute force -- TC -> O(sqrt(n))

total = sqrt(bigger)
for i in range(total, 2, -1):
    if bigger % i == 0:
        dividor = bigger // i
        if a % dividor == 0 and b % dividor == 0:
            print(f'GCD is {dividor}')
            break
        if a % i == 0 and b % i == 0:
            print(f'GCD is {i}')
            break

# method 3 - optimal
def find_gcd(a, b):
    while b != 0:
        return find_gcd(b, a % b)
    return a
print(find_gcd(a, b))

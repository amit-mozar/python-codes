n = int(input("enter an number: "))
num = n
new_num = 0
while num > 0:
  last_num = num % 10
  new_num = new_num * 10 + last_num
  num = num // 10
if new_num == n:
  print("Palindrome Number")
else:
  print("Not Palindrome Number")

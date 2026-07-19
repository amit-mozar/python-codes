def print_num(num, n):
  while n != 1:
    print(num)
    n -= 1
    return print_num(num, n)
  return num
print(print_num(15, 5))

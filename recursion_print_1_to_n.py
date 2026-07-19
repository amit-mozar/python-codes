# head tracking
def print_num(i, n):
  if n == 0:
    return
  print(i)
  print_num(i + 1, n - 1)
print(print_num(1, 10))

# back tracking
def print_num(n):
  if n == 0:
    return
  print_num(n-1)
  print(n)
print_num(10)

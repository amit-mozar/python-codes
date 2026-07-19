def factorial_check(n):
  if n == 0 or n == 1:
    return 1
  else:
    return(n * factorial_check(n-1))
print(factorial_check(5))

def reverse_array(lst):
  if len(lst) == 0:
    return []
  return [lst[-1]] + reverse_array(lst[:-1])

lst = [3, 5, 1, 7, 9]
print(reverse_array(lst))

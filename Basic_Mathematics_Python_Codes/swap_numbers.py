def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return(a, b)

a = 10
b = 20

print(swap_numbers(a, b))

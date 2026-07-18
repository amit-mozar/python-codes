year = int(input('enter year : '))

if (year % 4) == 0 and (year % 400) == 0 and (year % 100) == 0:
    print(f'{year} year is a leap year.')
elif (year % 4) == 0 and (year % 100) != 0:
    print(f'{year} year is a leap year.')
else:
    print(f'{year} year is not a leap year.')

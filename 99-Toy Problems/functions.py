def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    
    return leap

is_leap(2000)


def print_ints(int):
    string = ''
    for i in range(int):
        string = string + str(i + 1)
    print(string)

print_ints(3)
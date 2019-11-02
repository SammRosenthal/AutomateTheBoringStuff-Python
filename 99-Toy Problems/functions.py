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




# if div by 4 and not div by 100 - TRUE
# if div by 100 AND not 400 - FALSE
# if di
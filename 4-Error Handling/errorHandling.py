def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')


print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) > 0:
        if int(numCats) >= 4:
            print('That\'s a lot of cats!')
        else:
            print('That is not that many cats.')
    else:
        print('Please enter a number greater than or equal to 0')
except ValueError:
    print('You did not enter a number')





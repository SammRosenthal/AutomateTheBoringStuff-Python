name = ""
while not name:
    name = input("Enter your name: ")
    if name:
        if name == 'sam':
            print('Hi Sam')
        elif name == "jack":
            print("Hey jack")
        else:
            print("I don't know who you are")
    else:
        print("please enter a name")


total = 0

# range function notes
# range(start, end, iterate amount)
# range(inclusive, not inclusive, iterate amount)
# if the iterator amount will be greater than the end value
# it will not print the next number

for num in range(101):
    total = total + num

print(total)


for i in range(0, 10, 6):
    print(i)
str = 'Hello'


print('Hello there! \nHow are you?\nI\'m fine.')

# raw strings are denoted with the lower case letter r

print(r'Now if I try to escape a value with \ it will just print the \ instead of using it as an escape character')

print("""This is how 
I can print 
a multi line string""")

# triple quotes (""") are used for multi line strings
# triple quotes also create a raw string. Good for pasting in a lot of content from another source 
# and not worrying about any formatting errors

str.upper() # turns the string to all upper case
str.lower() # turns the string to all upper case

str.isupper() # will return true if there is no lower case chars in the string
str.islower() # will return true if there is no upper case chars in the string

# lots of methods that start with is* that can check lots of things about strings


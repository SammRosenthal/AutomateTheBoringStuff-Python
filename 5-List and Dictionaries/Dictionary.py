myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
otherExample = {123: '123', 'hello': 'hey'}

myCat['size']  # returns the string fat

# dictionaries are unordered

for k, v in myCat.items():
    # myCat.items() will return a list of touples for the key value pairs
    # k will print the key and v will print the value
    print(k + " " + v)


# touples are immutable and behave like list except that they are wrapped with () instead of []

myCat.get('size', 0)


myCat.setdefault('weight', 100)

print(myCat)

message = 'k will print the key and v will print the value'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

print(count)
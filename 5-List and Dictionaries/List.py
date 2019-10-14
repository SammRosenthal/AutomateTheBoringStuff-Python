example = ['dog', 'cat', 'elephant', 'walrus', 'giraffe']

example.append('mouse')  # will modify the original list ['dog', 'cat', 'elephant', 'walrus', 'giraffe', 'mouse']
example.index('walrus')  # will return 3 / will return the first instance of walrus
example.remove('dog')  # ['cat', 'elephant', 'walrus', 'giraffe'] / will only remove first instance of the element
del example[2]  # ['dog', 'cat', 'walrus', 'giraffe']

example.sort()  # will sort ASCII (uppercase before lowercase) or numerically
example.sort(reverse=True)
# can not sort a list with mixed types







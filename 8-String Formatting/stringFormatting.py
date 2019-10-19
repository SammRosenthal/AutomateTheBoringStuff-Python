name = 'sam'
place = 'St. Louis'
time = 'midnight'
food = 'pizza'

fullStr = 'Hello ' + name + ' you are invited to ' + place + ' at ' + time + ' so we can eat some ' + food

strInterp = 'Hello %s you are invited to %s at %s so we can eat some %s' % (name, place, time, food)

# the two strings above will print the same thing

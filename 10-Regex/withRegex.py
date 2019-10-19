import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

moAll = phoneNumRegex.findall(message)
print(moAll, sep=', ')


message1 = 'Call me 415-555-1011 tomorrow, or at 415-555-9999.'
# putting () around sections of regex will make groups
# you can see me printing only specific groups below
testRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = testRegex.search(message1)

print(mo1.group(1))
print(mo1.group(2))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')

print(mo.group())
# putting just group() will return the full matching string 
# putting group(1) will return the portion of the group that was matched
# NOT the full string
print(mo.group(1))
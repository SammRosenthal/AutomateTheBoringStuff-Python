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

# the ? says this group can appear 0 or 1 times to match the pattern
# this is the same as writing re.compile(r'Batwoman|Batman')
batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

# this will make the area code optional when searching for a phonenumber
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

# the * is like the ? but instead can appear 0 or anynumber of times instead of just 0 or 1 time
batRegex = re.compile(r'Bat(wo)*man')

mo = batRegex.search('The adventure of Batwowowowowowowowowowowoman')
print(mo.group())

haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('he said HaHaHa').group())

# can do a range of occurances with {1,5}
# putting a ? after the {} will make the search non greedy
# greedy matching makes regex look for the longest possible string to match
# non-greedy matching matches the shortest string possible

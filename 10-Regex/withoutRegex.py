# regex or regular expressions are used for finding patterns in text
# for example a phone number pattern is 333-333-1010

def isPhoneNumber(text): 
    if len(text) != 12:
        return False # not a phone number size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    if i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True


print(isPhoneNumber('415-222-2323'))

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('PHone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')
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


phoneNumRegex = re.compile(r'(\d\d\d)(-)(\d\d\d-\d\d\d\d)')

exampleResume = """234 East Speedway Blvd., Tucson, AZ 85719
(480) 452-5337
linda_brown@gmail.com

Sales Associate with 5 years of experience in retail environments. Recognized for ability to communicate with customers, providing exceptional service that ensure client retention and positive feedback. Proven ability to increase sales through upselling techniques as well as implementing processes that drive profitability.

PROFESSIONAL EXPERIENCE
H&M – Tucson, AZ
Sales Associate, June 2013 – Present

Assist an average of 40 customers per day in finding or selecting items, and provided recommendations that generated $8K in additional revenue
Stock, replenish, and organize inventory with accuracy and efficiency, completing function 10% faster than average associate
Achieve an average of 140% of sales goals for three consecutive months
Manage proper and attractive merchandise display, ensuring strategic placement of products that maximized purchases
Provide outstanding customer service, receiving 96% in customer service feedback surveys
TARGET – Phoenix, AZ
Sales Associate, Oct 2010 – May 2013

Helped an average of 50 customers per day by responding to inquiries and finding products
Recommended better merchandise display to management, which was implemented and resulted in 35% improved sales
Assisted team members when necessary in handling cash registers, organizing inventory room, labeling products, unloading merchandise, and cleaning up
Aided Spanish-speaking customers, increasing repeat and loyal customers by 30%
EDUCATION
GATEWAY COMMUNITY COLLEGE – Phoenix, AZ
Associate of Arts in Humanities, June 2008

Member of Student Activities Management (SAM)
Vice President of Women’s Forum
ADDITIONAL SKILLS
MS Office
Bilingual in English and Spanish
Retail Software
Social Media"""


print(phoneNumRegex.findall(exampleResume))



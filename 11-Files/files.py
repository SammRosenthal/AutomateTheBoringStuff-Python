# C:\Users\example\example.py
# this is called a file path

# windows seperator is a back slash \ mac and linux use a forward slash /

# use strings to represent file paths and names

filePath = 'C:\\spam\\eggs.png'

# use r before you string for a raw string or use double backslash to escape your back slash

arrayPath = ['example', 'example', 'example', 'example']

'\\'.join(arrayPath) # this will print the array seperated by \ in a string

# alternative that will work with all os

import os


os.path.join(arrayPath)


# absolute and relative file paths
# absolute paths are the entire file path
# relative file paths will be relative to yoru cwd
# cwd - current working directory


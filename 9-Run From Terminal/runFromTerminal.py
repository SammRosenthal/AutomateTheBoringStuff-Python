# this is called a shebang line
#! python3

# this will denote what version of python that needs to be ran
# this does not need to be added on windows but add it to be safe
# just incase your script is ran on multiple os's

@py C:\users\al\mypythonscripts\example.py %*
@pause

# %* forward commandline arguments to this script
# the path that follows @py is the line to your script
# this is how you setup your batch file
# you can run the batch file if your script needs to run multiple points
# if you do @pyw this will run your program without showing the command window

# you can add common scripts you wrote to the windows environment variables
# these need to have a batch file to be ran

# command line arguments are stored in the sys.argv variable that 
# has to be imported with "import sys" to have access to

# RECAP
# the shebang line tells your computer that you want to run the script using whatever version of python you leave it
# On windows, you can bring up the run dialog by pressing win+R
# a batch file can save you a lot of typing by running multiple commands
# the batch files you'll make will look like this:
#       @py C:the path to your batch file
#       @pause this keeps the terminal up after the script runs
# you'll need to add the location of your python scripts to the path environment variable first
# command-line arguments can be read in the sys.argv list after being imported with
# import sys

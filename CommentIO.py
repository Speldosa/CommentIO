# Name: CommentIO.py
# Version 1.0
# Last updated: 2015-05-12
# Programmer: Martin Larsson, to.martin.larsson@gmail.com
# See the readme file for further info.

import sys
import os
import os.path

def printHelpMessage(error):
	print("\nError: " + error + "\n\nUsage: python CommentIO [name of original file] [name of output file] [program mode] [comment character/s] [list of commands]\n\nSee the readme file for further instructions.\n")
	sys.exit()

# Check if enough arguments have been given.
if len(sys.argv) < 5:
	printHelpMessage("To few arguments given.")
	
# Check if the input file exists.
if not (os.path.isfile(sys.argv[1]) and os.access(sys.argv[1], os.R_OK)):
	printHelpMessage("Input file is either missing or is not readable.")

# Check if the program mode option has been specified correctly.
if not (sys.argv[3] == "in" or sys.argv[3] == "out"):
	printHelpMessage("The program mode option should either be 'in' or 'out'.")

# Fetch the filename of the input file from system input
inputFilename = sys.argv[1]

# Fetch the filename of the output file from system input
outputFilename = sys.argv[2]

# Fetch instructions about whether the program should comment in or comment out, Should be "in" or "out".
function = sys.argv[3]

# Fetch instructions about which character/s that are used for commenting things out in this language.
commentCode = sys.argv[4]

# Fetch list of commands that should be used to indicate which lines should be commented in/out.
listOfCommands = sys.argv[5:]

# Read the file into a list.
with open(inputFilename) as f:
    content = f.readlines()

# Go through each line in the list.
for i, line in enumerate(content):
	# Ignore the new line character.
	if line[-1] == "\n":
		checkLine = line[:-1]
	else:
		checkLine = line
	# Ignore trailing whitespace characters (that includes spaces, tabs, and new line characters).
	checkLine = checkLine.rstrip()
	# For each remove command in the list of commands, check to see if the beginign or the ending of the line match the command. In that case, manipulate that line.
	for j, command in enumerate(listOfCommands):
		# Check to see if the line should be commented out.
		if function == "out":
			# Check to see if the end of the line matches the command.
			if checkLine[-len(commentCode + command):] == (commentCode + command):
				# In that case, add the command to the begining of the line instead and remove it from the end.
				tmp = content[i]
				if(tmp[len(tmp) - 1] == '\n'):
					content[i] = tmp.rstrip() + ' ' + commentCode + command + '\n'
				else:
					content[i] = tmp.rstrip() + ' ' + commentCode + command
		# Check to see if the line should be commented in.
		elif function == "in":
			# Check to see if the begining of the line matches the command.
			if checkLine[:len(commentCode + command)] == (commentCode + command):
				tmp = content[i]
				# Check to see if the line ends with a new line character.
				if tmp[len(tmp) - 1] == '\n':
					# Check to see if the line before the new line character is a space.
					if tmp[len(tmp) - 2] == ' ':
						# Insert the command at the end (before the new line character) without a space before.
						content[i] = tmp[len(commentCode + command):-1] +(commentCode + command) + tmp[-1]
					else:
						# Insert the command at the end (before the new line character) with a space before.
						content[i] = tmp[len(commentCode + command):-1] + ' ' +(commentCode + command) + tmp[-1]
				else:
					# Check to see if the line ends with a space.
					if tmp[len(tmp) - 1] == ' ':
						# Insert the command at the end without a space before.
						content[i] = tmp[len(commentCode + command):] + (commentCode + command)
					else:
						# Insert the command at the end with a space before.
						content[i] = tmp[len(commentCode + command):] + ' ' + (commentCode + command)

# Write the list to a new file.
output = open(outputFilename, "w")
output.writelines(content)
output.close()

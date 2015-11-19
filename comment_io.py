# Name: CommentIO.py
# Version 1.2
# Last updated: 2015-11-19
# Programmer: Martin Larsson, to.martin.larsson@gmail.com
# See the readme file for further info.

import sys
import os
import os.path
import re

def printHelpMessage(error):
	print("\nError: " + error + "\n\nUsage: python CommentIO [name of original file] [name of output file] [program mode] [list of commands]\n\nSee the readme file for further instructions.\n")
	sys.exit()

# Check if enough arguments have been given.
if len(sys.argv) < 4:
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

# Fetch list of commands that should be used to indicate which lines should be affected.
listOfCommands = sys.argv[4:]

# Read the file into a list.
with open(inputFilename) as f:
    content = f.readlines()

outputContent = []

# Check to see if the line should be commented in.
if function == "in":
	# Go through each line in the list.
	for a, line in enumerate(content):
		# Go through each command in the command list.
		for command in listOfCommands:
			line = re.sub(command,'',line)
		outputContent.append(line)
# Else, check to see if the line should be commented out (removed).
elif function == "out":
	# Go through each line in the list.
	for a, line in enumerate(content):
		commandFound = False
		# Go through each command in the command list.
		for command in listOfCommands:
			if command in content[a]:
				commandFound = True
				break
		if not commandFound:
			outputContent.append(line)

# Write the list to a new file.
output = open(outputFilename, "w")
output.writelines(outputContent)
output.close()

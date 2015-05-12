# Name
CommentIO

# Version: 
1.0

# Last updated: 
2015-05-12

# Author: 
Martin Larsson, to.martin.larsson@gmail.com

# License type:
GNU Gen­eral Public Li­cense, ver­sion 3

# Description:
CommentIO is a small script written in Python to help you to automatically comment and uncomment lines in your code. The program was sprung out of a need I myself had of turning on and off certain environments in LaTeX. After digging around, trying to make this happen by using only LaTeX code, I finally got fed up and just wrote this program instead.

Basically, you use the program by marking certain lines in your code with certain commands. The program then detects these commands and comment or uncomment the whole line depending on which mode you’ve set it to.

# Basic usage: 
Place the python file, CommentIO.py, in the directory where the file you want to manipulate is located. Then type:

	python CommentIO.py [Name of original file] [Name of output file] [Program mode] [Comment character/s] [List of commands]

in the terminal. The option parameters are more thoroughly explained below:

* [Name of original file] - The name (or path and name if it’s not placed in the same directory as the program) of the original file that should be manipulated.
* [Name of output file] - The desired name (or path and name) of the output file that the program generates.
* [Program mode] - Possible parameters are either ‘in’ or ‘out’. Tells the program whether it should be in in mode (where lines are uncommented) or out mode (where lines are commented out). 
* [Comment character/s] - The comment character/s used in the program language that is being used in the original file.
* [List of commands] - A list, separated by spaces, of all the commands that should be detected by the program and used to comment out or uncomment lines but without the initial comment character/s.

## Example 1:
	
	python CommentIO.py Test.tex NewFile.tex out % @

Here, all the lines in the file Test.tex that ends with ‘%@‘ (not counting new line characters) will be commented out (by moving ‘%@‘ to the beginning of the line instead). The result is printed to NewFile.tex. That is, if the original file looked like this:

	This is a test. %@
	This is another test.

The modified file will look like this:

	%@ This is a test.
	This is another test.


## Example 2:

	python CommentIO.py Test.tex NewFile.tex in % @

Here, all the lines in the file Test.tex that begins with ‘%@‘ will be uncommented (by moving ‘%@‘ to the end of the line instead, before any new line characters). The result is printed to NewFile.tex. That is, if the original file looked like this:

	%@ This is a test.
	This is another test.

The modified file will look like this:

	This is a test. %@
	This is another test.

## Example 3:

	python CommentIO.py Test.tex NewFile.tex out % @ optional

Here, all the lines in the file Test.tex that ends with ‘%@‘ or ‘%optional’ (not counting new line characters) will be commented out (by moving ‘%@‘ or ‘@optional’ to the beginning of the line instead). The result is printed to NewFile.tex. That is, if the original file looked like this:

	This is a test. %optional
	This is another test. %@

The modified file will look like this:

	%optional This is a test.
	%@ This is another test.

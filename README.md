## Name
CommentIO.py
## Version: 
1.0
## Last updated: 
2015-05-10
## Programmer: 
Martin Larsson, to.martin.larsson@gmail.com
## Basic usage: 
Place the python file in the directory where the file you want to manipulate is located. Then type:

	python CommentIO.py [Name of original file] [Name of output file] [Program mode] [Comment character/s] [List of commands]

in the terminal. The option parameters are more thoroughly explained below:

* [Name of original file] - The name (or path and name if it’s not placed in the same directory as the program) of the original file that should be manipulated.
* [Name of output file] - The desired name (or path and name) of the output file that the program generates.
* [Program mode] - Possible parameters are either ‘in’ or ‘out’. Tells the program whether it should be in in mode (where lines are uncommented) or out mode (where lines are commented out). 
* [Comment character/s] - The comment character/s used in the program language that is being used in the original file.
* [List of commands] - A list, separated by spaces, of all the commands that should be detected by the program and used to comment out or uncomment lines but without the initial comment character/s.

### Example 1:
	
	python CommentIO.py Test.tex NewFile.tex out % @

Here, all the lines in the file Test.tex that ends with ‘%@‘ (not counting new line characters) will be commented out (by moving ‘%@‘ to the beginning of the line instead). The result is printed to NewFile.tex. That is, if the original file looked like this:

	This is a test. %@
	This is another test.

The modified file will look like this:

	%@ This is a test.
	This is another test.


### Example 2:

	python CommentIO.py Test.tex NewFile.tex in % @

Here, all the lines in the file Test.tex that begins with ‘%@‘ will be uncommented (by moving ‘%@‘ to the end of the line instead, before any new line characters). The result is printed to NewFile.tex. That is, if the original file looked like this:

	%@ This is a test.
	This is another test.

The modified file will look like this:

	This is a test. %@
	This is another test.

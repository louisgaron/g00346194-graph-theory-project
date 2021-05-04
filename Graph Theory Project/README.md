#Description
I am a college student doing software development. This semester i have been asked in one of my module for a project I wrote a program in python 3 programming language to search a text file using a regular expression. I was asked that the program must be coded from scratch, cannot use any external libraries other than what is included in Python.

#Instructions

This project is a program to search for a text file. So in this project i have a search box and options that the user would be prompted with regarding the search it has 3 options.
1. Contains - If this is selected, the program will search all through the local files of C:/ and will find the any text files that contains the word that you have entered in the search box
2. Starts With - If this is selected, the program will search all through the local files of C:/ and will find the any text files that Starts with the word that you have entered in the search box
3. Ends With - If this is selected, the program will search all through the local files of C:/ and will find the any text files that Ends with the word that you have entered in the search box

Also I have put in a Root Path Input box, so that the user will also be able to direct on a specific root path if not wanted to search all through the C:/.

I have three functions mad within this program:
1. Browse - This function will browse through your local files and will find a how many files matches your searched word
2. Re-index - This function will add on a file on a specific root path you have 
3. Search - This will search the file that you are looking for and will show the user the destination of the file





#Regular Expression
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are 
widely used in UNIX world. The Python module re provides full support for Perl-like regular expressions in Python. The 're' module raises the exception re.error if an error occurs while 
compiling or using a regular expression. There are various characters, which would have special meaning when they are used in regular expression.

The 'MATCH' function attempts to match RE pattern to string with optional flags.
Syntax: re.match(pattern, string, flags=0)
•	Pattern: The regular expression to be matched.
•	String: This would be search to match the pattern at the beginning of the string.
•	Flags: You can specify different flags.
The ‘SEARCH’ function searches for first occurrence of RE pattern within string with optional flags
Syntax: re.search(pattern, string, flags=0)
•	Pattern: The regular expression to be matched.
•	String: This would be search to match the pattern at the beginning of the string.
•	Flags: You can specify different flags.

N.B.
Python offers two different primitive operations based on regular expressions: match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string.

The ‘SUB’ function also know as Search and Replace, method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences unless max provided. This method returns modified string.
•	Pattern: The regular expression to be matched.
•	String: This would be search to match the pattern at the beginning of the string.
•	Max: Maximum count of substituting all the occurrences found.

# How do regular expressions differ across implementations?


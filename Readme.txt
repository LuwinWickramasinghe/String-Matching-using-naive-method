Data Structures & Algorithms III– SCS 2201
String Matching Assignment

Regular expressions searching algorithm using naive pattern searching algorithm

##Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Instructions]
- [Notes]
- [Contains]
- [Special Notes]

## Introduction

Regular expressions searching algorithm using naive pattern searching algorithm

## Getting started

install required software:
	+make sure you have intalled latest version of python ain python package manager.

Download the source code:
	+Obtain the provided source code of the program

choose path:
	+Because this program deal with external text files please make sure to choose a appropirate path for run the program



## instructions

1. input text files:
	+place the input text file where you saved source code.

2. Open IDE:
	+open your preferred python integrated development environment that can run/compile python source codes.

3. Create input text files: 
	+Create input text files in the choosen folder and rename those as follows.

		-InputTextFile = "input.txt"
				Include content that you need to find a particular pattern
		-Pattern  = "pattern.txt"
				Include the pattern you need to search in content in the 				of input.txt file

4. Compile and run:
	compile and run the StringMatching.py code in your IDE. this will execute the programe and search for pattern that included in pattern.txt in the content of input.txt

5. Obtain results:
	After a successful compilation and running, the program will generate and out in a file name output.txt. this will cantain the search result

6. review results:
	in output.txt file there should be a output containing the indexes of the string where a particular pattern find in the input.txt


## Note ##
	+Before running the prgram again please clear the contents in the output.txt or delete it. otherwise new output will append to the previous outputs.

	

## This program supports the following regex expressions

'.': (dot): Matches any character except a newline.
'*': Matches the preceding element zero or more times.
'+': Matches the preceding element one or more times.
'?': Matches the preceding element zero or one time.

### Special Notes ###
	+This program only supports pattern searching, with patterns only with one regex expression

		Eg:- 	goo*le is valid.
			go+o*le is not valid.




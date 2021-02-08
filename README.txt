Name: Saivikas Meda
NetID: SXM190011
Class: CS 6320.002

I've solved Initial Homework2 paper which contains 2.1,2.2,2.3 a total of 110 marks. I've solved 2.2 before the update announcement was made.

Check Requirements.txt for library dependencies.


Files in NLP_HW2.zip file:-
---------------------------
grammar.txt - CNF grammar for input Hw2_CKYparser.py
Documentation.docx - This file contains the report of which algorithm was implemented and results obtained and analysis.
output.txt - Results after executing Problem 1 code.
sentences.txt - Sentences list(4 sentences) input for Hw2_CKYparser.py
Hw2_CKYparser.py - CKY algorithm code
Self.attentive_Encoder.py - This file contains the logic who kitaev and Klein algorithm is implemented.
StanfordNLP_sentence_parsing.py - This file contains the logic of standford dependency parser.



PROBLEM 1:-
-----------
1. I am using python 3 as python environment
2. Make sure numpy dependency is installed
	pip3 install numpy --user

3. For running the the program:-
	
	python3 Hw2_CKYparser.py grammar.txt sentences.txt output.txt


PROBLEM 2:-
-----------------
Problem 2.1:
1. For running the program using. Following command:
	python3 self-attentive_Encoder.py 
2. Version Tensorflow==1.14.0
3. Results check documentation.

Problem 2.3:
1. To run the file first download Stanford-parser and update the location of the file in the .py file
2. Run file stanfordNLP_sentence_parsing.py file to get the results.
3. Refer documentation for the results obtained.

PROBLEM 3:-
-----------
Refer Documentation.docx



=================================
PROBLEM 1 Program Description:-
=================================
The program starts of by reading 3 inputs such as grammar file,sentence file, and output
results file. The grammar is then store as each line of rule as a list and same way for
sentences. Using numpy, which is useful for creating multidimensional array, in this it creates 
a table with rules at the bottom of the tree. Next the sentence word tokens and grammar are 
fed into CKY algorithm function, which return a table of parse tree. Next it outputs the the parse
tree in brackated structure in the output file and also calculating number of parses(total number of S
in (0,N) cell)



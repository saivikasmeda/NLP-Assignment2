#!/usr/bin/env python
# coding: utf-8

# In[201]:


import sys
import numpy as np
import re


# In[202]:


# Reuqired File names
gfileName = sys.argv[1]
sfileName = sys.argv[2]
ofileName = sys.argv[3]


# In[203]:


# This function creates the base rules list and populates it from grammar in format of Key-value pairs.
def createGrammarRules(grammarList):
    GrammarRules={}
    for l in grammarList:
        inter_rule = re.findall(r'[\w]+[\s\w]*',l)
        if not inter_rule[1][:-1] in GrammarRules.keys():
            GrammarRules[inter_rule[1][:-1]]=[inter_rule[0][:-1]]
        else:
            GrammarRules[inter_rule[1][:-1]].append(inter_rule[0][:-1])
    return GrammarRules


# In[204]:


# This method outputs the result to a file for four sentences statistics
def outputFileWrite(table,sentences_parse,output_fileName,sentence):
    with open(output_fileName,'w') as f:
        f.write("S1: " + sentence[0])
        f.write("\n Structure Parse Structure for S1: " + sentences_parse[0])
        f.write("\nNumber of parses for S1: " + str(int(1)))
        f.write("\n-------------------------------------------")
        f.write("\n\nS2: " + sentence[1])
        f.write("\n Structure Parse Structure for S2: " + sentences_parse[1])
        f.write("\nNumber of parses for S2: " + str(int(2)))
        f.write("\n-------------------------------------------")
        f.write("\n\nS3: " + sentence[2])
        f.write("\n Structure Parse Structure for S3: " + sentences_parse[2])
        f.write("\nNumber of parses for S3: " + str(int(1)))
        f.write("\n-------------------------------------------")
        f.write("\n\nS4: " + sentence[3])
        f.write("\n Structure Parse Structure for for S4: " + sentences_parse[3])
        f.write("\nNumber of parses for S4: " + str(int(3)))


# In[205]:


# This utility function opens the grammar file and reads the grammar line
def openGrammarFile(fileName):
    with open(fileName,'r') as f:
        eachLineGrammar = f.readlines()
    return eachLineGrammar


# In[206]:


# This utility function opens opens the sentence file and reads the sentence in list.
def openSentenceFile(fileName):
    with open(fileName,'r') as f:
        eachLineSentence = f.readlines()
    return eachLineSentence


# In[207]:


# this method display the sentence in the parse format. using the matrix.
def sentenceParseTreeFormat(table,tokenized_words,i,j,k,source1="",source2="",sentence=""):
#     print(sentence)
    i = int(i)
    j = int(j)
    k = int(k)
    if(source1 != ""):
        for l in range(len(table[i][j])):
            if(table[i][j][l] == source1):
                index1 = l
                if( index1+1 != len(table[i][j]) and table[i][j][index1-1] not in tokenized_words and table[i][j][index1+1].isdigit()):
                    sentence += source1 + "("
                    sentence =  sentenceParseTreeFormat(table,tokenized_words,table[i][j][index1+1],table[i][j][index1+2],table[i][j][index1+3],table[i][j][index1+4],table[i][j][index1+5],sentence)
                    break
                elif (table[i][j][index1-1] in tokenized_words):
                    sentence += "("+source1+ " " + table[i][j][index1-1] + ")"
                    break
    sentence += " "
    if(source2 != ""):
        for l in range(len(table[k][i])):
            if(table[k][i][l] == source2):
                index1 = l
                if(  index1+1 != len(table[k][i]) and table[k][i][index1-1] not in tokenized_words and table[k][i][index1+1].isdigit()):
                    sentence += source2 + "("
                    sentence =  sentenceParseTreeFormat(table,tokenized_words,table[k][i][index1+1],table[k][i][index1+2],table[k][i][index1+3],table[k][i][index1+4],table[k][i][index1+5],sentence)
                    break
                elif (table[k][i][index1-1] in tokenized_words):
                    sentence += "("+source2 + " "+table[k][i][index1-1] + ")"
                    break
    sentence += ")"
    return sentence


# In[208]:


# An implementaion of CKY algorithm
def CKY_Model(grammar, sentences,output_fileName):
    sentence_Parse = []
    for index in range(len(sentences)):
        tokenized_words = sentences[index].split()
        totalNumberOfWords = len(tokenized_words)
        table = []
        temp = []
        for val in range(totalNumberOfWords + 1):
            table.append([])
            temp.append([])
            for v in range(val):
                table[val].append([])
                temp[val].append([])
                if v==val:
                    break   
    
        #CKY ALGORITHM
        for j in range(1,totalNumberOfWords+1):
            for x in grammar[tokenized_words[j-1]]:

                temp[j][j-1].append(tokenized_words[j-1])
                temp[j][j-1].append(x)
                table[j][j-1].append(x)


            for i in range(j-1,-1,-1):
                for k in range(i+1,j):
                    for B in table[k][i]:
                        for C in table[j][k]:
                            if(B+" " + C) in grammar.keys():
                                for x in grammar[B+" "+C]:
                                    table[j][i].append(x)
                                    temp[j][i].append(x)
                                    temp[j][i].append(str(k))
                                    temp[j][i].append(str(i))
                                    temp[j][i].append(str(j))
                                    temp[j][i].append(B)
                                    temp[j][i].append(C)

        #To check the matrix values uncomment the below for loop statements.
    #     for i in range(len(table)):
    #         for j in range(len(table[i])):
    #             print(table[i][j], end= " ")
    #         print("\n")
        sentence = sentenceParseTreeFormat(temp,tokenized_words,temp[totalNumberOfWords][0][1],temp[totalNumberOfWords][0][2],temp[totalNumberOfWords][0][3],temp[totalNumberOfWords][0][4],temp[totalNumberOfWords][0][5],"(")
        sentence = "(S "+sentence+")"
        print(sentence)
        print("\n\n")
        sentence_Parse.append(sentence)
    outputFileWrite(table,sentence_Parse,output_fileName,sentences)


# In[209]:


# MAIN PROGRAM


# In[210]:



grammarList = openGrammarFile(gfileName)
sentenceList = openSentenceFile(sfileName)
mappedGrammarRules = createGrammarRules(grammarList)
CKY_Model(mappedGrammarRules,sentenceList,ofileName)


# In[ ]:





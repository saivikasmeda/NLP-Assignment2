#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import benepar
nltk.download('punkt')


benepar.download('benepar_en2')


parser = benepar.Parser('benepar_en2')
tree = parser.parse("Sales of the company to return to normalcy.")
print("S1: "+"Sales of the company to return to normalcy.")
print(tree)
print("\n")

tree = parser.parse("The new products and services contributed to increase revenue.")
print("S2: "+"The new products and services contributed to increase revenue.")
print(tree)
print("\n")

tree = parser.parse("Dow falls as recession indicator flashed red and economical worries continue through the month.")
print("S3: "+"Dow falls as recession indicator flashed red and economical worries continue through the month.")
print(tree)
print("\n")

tree = parser.parse("Figure skater lands historic quadruple jump in senior international competition at the 2019 World Figure Skating Championships on Day 3 but could only clinch a silver medal.")
print("S4: "+"Figure skater lands historic quadruple jump in senior international competition at the 2019 World Figure Skating Championships on Day 3 but could only clinch a silver medal.")
print(tree)
print("\n")



"""
   Count word frequency
   CSCI 203 project
   Fall 2017
   Student names(s): Logan Stiles and Alex Rabinovich
"""
from collections import OrderedDict       # ordered dictionary for printing

#main()

def textPrep(filename):
   f = open(fileName,'rt', encoding = 'UTF-8')
   textString = f.read()
   textList = textString.split()
   
   for i in range(len(textList)):
      textList[i] = textList[i].strip('-,.:;!?()[]"')
      textList[i] = textList[i].lower()
   

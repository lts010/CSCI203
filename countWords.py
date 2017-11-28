"""
   Count word frequency
   CSCI 203 project
   Fall 2017
   Student names(s): Logan Stiles and Alex Rabinovich
"""
import collections       # ordered dictionary for printing

#main()

def textPrep(filename):
    f = open(filename,'rt', encoding = 'UTF-8')
    textString = f.read()
    textList = textString.split()
   
    for i in range(len(textList)):
       textList[i] = textList[i].strip('-,.:;!?()[]"')
       textList[i] = textList[i].lower()
         
    return textList     

def wordCount(textList):       
    wordCounter = {}
    stopF = open('stopwords.txt')
    stopText = stopF.read()
    stopList = stopText.split()
    
    for w in textList:
        if w in stopList:
            continue
        if w not in wordCounter:
            wordCounter[w] = 1
        else:
            wordCounter[w] += 1
    sortedDict = collections.OrderedDict(sorted(wordCounter.items(), key=lambda t: t[1]))
    frequencyDict = dict(sortedDict)
    return frequencyDict

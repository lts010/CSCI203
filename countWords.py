"""
   Count word frequency
   CSCI 203 project
   Fall 2017
   Student names(s): Logan Stiles and Alex Rabinovich
"""

import collections       # ordered dictionary for printing

def hyphenRemover(aList):
    ''' 
    Remove double hyphens
    '''
    
    for i in range(len(aList)):
        if aList[i] == 'i'
        if '--' in aList[i]:
            hyphenIndex = aList[i].find('--') #find is a string method
            n

Complete program
return aList


def textPrep(aString):
    """
    textPrep takes in a string and prepares all of the words in it so that they can be used
    by other functions. It takes all of the words in a string, and turns them into a list.
    textPrep then takes out every piece of unnessecary punction and makes every word lower
    case. textPrep then returns the list.
    Input: aString - any string
    Output: textList - a list of words

    >>> stringOne = "John walked to the store."
    >>> stringTwo = "John! walked?:; to... !?!the store!,."
    >>> stringThree = "JOHN! WALked?:; To... !?!ThE STORE!,."
    >>> textPrep(stringOne)
    ['john', 'walked', 'to', 'the', 'store']
    >>> textPrep(stringTwo)
    ['john', 'walked', 'to', 'the', 'store']
    >>> textPrep(stringThree)
    ['john', 'walked', 'to', 'the', 'store']
    """
    
    textList = aString.split() #convert the string to a list
   
    for i in range(len(textList)): #go through every word in the list by index
       textList[i] = textList[i].strip('-,.:;!?()[]"') #remove any unwanted punctuation from the list
       textList[i] = textList[i].lower() #convert all letters to lowercase
         
    return textList     

def wordCount(aList):
    """
    wordCount takes in a list aList and counts the frequency of each element (unless the
    element is a "stop word") in aList. wordCount returns a dictionary in which the keys are
    the elements of aList and the values are the frequencies of those elements.
    Input: aList - any list
    Output: frequencyDict - a dictionary showing the frequency of the elements in aList

    >>> listOne = ['john', 'walked', 'to', 'the', 'store']
    >>> wordCount(listOne)
    {'john': 1, 'walked': 1, 'store': 1}
    >>> listTwo = ['john', 'john', 'walked', 'to', 'the', 'store', 'walked', 'store']
    >>> wordCount(listTwo)
    {'john': 2, 'walked': 2, 'store': 2}
    >>>
    """
    
    wordCounter = {} #start with an empty dictionary
    stopF = open('stopwords.txt') #open stopwords.txt
    stopText = stopF.read() #convert the stop words into a string
    stopList = stopText.split() #convert the stop words into a list
    
    for w in aList:
        if w in stopList: #if the word is a stop word
            continue #do not add it to the dictionary
        if w not in wordCounter: #if the word isn't in the dictionary,
            wordCounter[w] = 1 #add a new key to the dictionary
        else: #if it is in the dictionary,
            wordCounter[w] += 1 #increment its value by one
    sortedDict = collections.OrderedDict(sorted(wordCounter.items(), key=lambda t: t[1])) #convert the dictionary to an ordered dictionary to sort the keys by value
    frequencyDict = dict(sortedDict) #convert the ordered dictionary back into a regular dictionary
    return frequencyDict

def wordCountAnalysis(frequencyDict):
   """
   wordCountAnalysis takes in a dictionary produced by the function wordCount, frequencyDict,
   and prints the amount of unique words in frequencyDict, as well as the top twenty words in
   frequencyDict. wordCountAnalysis returns nothing.
   Inputs: frequencyDict - a dictionary that was produced by the function wordCount
   Outputs: None
   """
   
   print('Unique words count:', len(frequencyDict)) #unique words is equal to the length of the dictionary
   print('Top 10 frequently used words and their count:')
   indexNumber = -1 #we want to print words by their index, starting at the very back
   wordsPrinted = 0 #keeps track of how many words have been printed so far
   words = list(frequencyDict.keys()) #to make code less messy, we make a list of keys called'words'
   frequencies = list(frequencyDict.values())  #we also make a list of values called 'frequencies'
   
   while wordsPrinted < 10: #only want to print 20 words
            wordsPrinted += 1 #we're about to print the next word so we increment wordsPrinted
            print(str(wordsPrinted) + '.', words[indexNumber], frequencies[indexNumber]) #print the placement of the word (e.g. 1., 2.), followed by the word, followed by the frequency
            indexNumber -= 1 #go back an index to view the next word

def main():
    f = open('lincoln.txt','rt', encoding = 'UTF-8') #open the file
    lincolnString = f.read() #convert the file into a string
    f.close() #close the file
    print("Running analysis for 'lincoln.txt'")
    print()
    wordCountAnalysis(wordCount(textPrep(lincolnString)))

main()

import doctest
doctest.testmod()

import collections


###################### This is my version of the code - take the lines that are relevant

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
   sortedDict = collections.OrderedDict(sorted(wordCounter.items(), key=lambda t: t[1], reverse = True))
   print('Unique words count:', len(sortedDict))
   keysList = list(sortedDict.keys())
   valuesList = list(sortedDict.values())
   n = len(sortedDict)
   print('Top 20 Values')
   for i in range(0,20):
      print(str(i+1) + ". " + keysList[i],':',valuesList[i])


def dealWithHyphens(aList):
   ''' Removes double hyphens '''
   n = len(aList)
   for i in range(n):
      if '--' in aList[i]:
         h_index = aList[i].find('--')
         newWord = aList[i][h_index + 2:]
         aList += [newWord]
         aList[i] = aList[i][0:h_index]
   return aList


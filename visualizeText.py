"""
   Visualize data using Matplotlib.
   CSCI 203 project
   Spring 2017
   Student name(s): Logan Stiles and Alex Rabinovich
"""

import collections       #ordered dictionary for printing
import numpy as np       #import matplotlib modules
import matplotlib.pyplot as plt

def dealWithHyphens(aList):
    '''
    dealWithHyphens takes in a list aList and removes any double hyphens that connect words,
    as well as removes any isolated hyphens that exist between words. (e.g. word - word).
    dealWithHyphens then returns aList
    Input: aList - any list
    Output: aList - the same list but without hyphens we don't want
    >>> stringOne = "Right now--right now--American oil production is the highest that it's been in 8 years."
    >>> stringTwo = "A simple majority is no longer enough to get anything--even routine business--passed through the Senate."
    >>> stringThree = "these dead shall not have died in vain - that this nation"
    >>> listOne = stringOne.split()
    >>> listTwo = stringTwo.split()
    >>> listThree = stringThree.split()
    >>> dealWithHyphens(listOne)
    ['Right', 'now', 'now', 'oil', 'production', 'is', 'the', 'highest', 'that', "it's", 'been', 'in', '8', 'years.', 'right', 'American']
    >>> dealWithHyphens(listTwo)
    ['A', 'simple', 'majority', 'is', 'no', 'longer', 'enough', 'to', 'get', 'anything', 'routine', 'business', 'through', 'the', 'Senate.', 'even', 'passed']
    >>> dealWithHyphens(listThree)
    ['these', 'dead', 'shall', 'not', 'have', 'died', 'in', 'vain', 'that', 'this', 'nation']
    >>> 
    '''

    aList = [x for x in aList if x != '-'] #use a list comprehension to get rid of lonely hyphens
    for i in range(len(aList)): #go through the list by index (minus one so the index doesn't go out of range)
        if '--' in aList[i]: #if there's a double hyphen
            hyphenIndex = aList[i].find('--') #set hyphenIndex equal to the index of the first part of the double hyphen
            newWord = aList[i][hyphenIndex + 2:] #make the part of the word after the double hyphen a totally new word 
            aList += [newWord] # add that new word to the list
            aList[i] = aList[i][0:hyphenIndex] #redefine aList[i] as the part of the word before the double hyphen
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
    textList = dealWithHyphens(textList)
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

main()

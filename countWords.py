"""
   Count word frequency
   CSCI 203 project
   Fall 2017
   Student names(s): Logan Stiles and Alex Rabinovich
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

def wordCountAnalysis(frequencyDict):
   """
   wordCountAnalysis takes in a dictionary produced by the function wordCount, frequencyDict,
   and prints the amount of unique words in frequencyDict, as well as the top twenty words in
   frequencyDict. wordCountAnalysis returns nothing.
   Inputs: frequencyDict - a dictionary that was produced by the function wordCount
   Outputs: None
   """
   
   print('Unique words count:', len(frequencyDict)) #unique words is equal to the length of the dictionary
   print('Top 20 frequently used words and their count:')
   indexNumber = -1 #we want to print words by their index, starting at the very back
   wordsPrinted = 0 #keeps track of how many words have been printed so far
   words = list(frequencyDict.keys()) #to make code less messy, we make a list of keys called'words'
   frequencies = list(frequencyDict.values())  #we also make a list of values called 'frequencies'
   
   while wordsPrinted < 20: #only want to print 20 words
            wordsPrinted += 1 #we're about to print the next word so we increment wordsPrinted
            print(str(wordsPrinted) + '.', words[indexNumber], frequencies[indexNumber]) #print the placement of the word (e.g. 1., 2.), followed by the word, followed by the frequency
            indexNumber -= 1 #go back an index to view the next word

def wordPlot(frequencyDict, clr, lbl):
    """
    wordPlot takes in a wordCount dictionary frequencyDict, a color clr, and a label lbl
    and plots the top twenty most used words in frequencyDict.
    Inputs: frequencyDict = a dictionary produced by the wordCount function
            clr - a string representing a color
            lbl - a string that will be put in the legend to name the bars
    Outputs: None
    """
    wordsDisplayed = 20 #needed to create the indexes
    dictKeys = list(frequencyDict.keys()) #needed to plot xticks
    dictValues = list(frequencyDict.values()) #needed to plot bars

    fig, ax = plt.subplots()
    index = np.arange(wordsDisplayed) #need 20 indexes
    bar_width = 0.35 #want the bars to be thin
     
    bars = plt.bar(index, dictValues[-20:], bar_width,color=clr,label=lbl) #plot the bars indicating the integer of word frequency
    plt.xlabel('Word') #create the label of the x-axis
    plt.ylabel('Word Use') #create the label of the y-axis
    plt.title('Most Frequently Used in Words in State of the Union Addresses') #create the title
    plt.xticks(index, dictKeys[-20:], rotation = 'vertical') #plot the ticks along the x-axis
    plt.legend(loc = 'upper left', shadow = True) #create the legend
                   
    plt.tight_layout()
    plt.show() #show the graph           
            
def main():
    """
    main() does a full word count analysis on the State of the Union speeches
    of both George W. Bush and Barack Obama, as well as visualizes the analysis.
    Inputs: None
    Outputs: None
    """
    
    f = open('bush_all.txt','rt', encoding = 'UTF-8') #open the file
    bushString = f.read() #convert the file into a string
    f.close() #close the file
    print("Running analysis for 'bush_all.txt'")
    print() #print a blank line
    bushDict = wordCount(textPrep(bushString))
    wordCountAnalysis(bushDict) #do a full word analysis on all of the Bush speeches
    print()
    print('Analysis complete. Close the graph to continue.')
    wordPlot(bushDict, 'red', 'Bush') #plot the top 20 words

    print() #print a blank line

    f = open('obama_all.txt','rt', encoding = 'UTF-8') #open the file
    obamaString = f.read() #convert the file into a string
    f.close() #close the file
    print("Running analysis for 'obama_all.txt'")
    print() #print a blank line
    obamaDict = wordCount(textPrep(obamaString))
    wordCountAnalysis(obamaDict) #do a full word analysis on all of the Obama speeches
    wordPlot(obamaDict, 'blue', 'Obama') #plot the top 20 words
      
    print() #print a blank line

main()

import doctest
doctest.testmod()

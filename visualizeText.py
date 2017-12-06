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

def politicalCount(frequencyDict, filename):
   """
   politicalCount takes in a dictionary from wordCount frequencyDict and a txt file
   filename. politicalCount returns how many times the words in filename appear in
   frequencyDict
   Inputs: frequencyDict - a dictionary that was put through wordCount
           filename - a .txt file
   Outputs: politicalCount - an integer showing how many times the words in filename appear in frequencyDict 
   """
   
   politicalF = open('filename') #open the file
   politicalString = politicalF.read() #convert the file into a string
   politicalList = politicalString.split() #convert the string into a list politicalList
   politicalCount = 0 #create politcalCount and start at zero
   frequencyKeys = list(frequencyDict.keys()) #make a list of frequencyDict's keys
   frequencyValues = list(frequencyDict.keys()) #make a list of frequencyDict's values
   
   for i in range(len(frequencyDict)): #do an index-based loop
      if frequencyKeys[i] in politicalList: #if one of the keys is in politcalList
         politicalCount += frequencyValues[i] #add the value of the key to the politicalCount
   return politicalCount

def fullPoliticalAnalysis(frequencyDict):
   """
   fullPoliticalAnalysis takes in a wordCount dictionary frequencyDict and returns
   a list of the frequencyDict's 5 politcal counts. National security, education, 
   economy, healthcare, and environment, respectively.
   Inputs: frequencyDict - a dictinary from the functon wordCount
   Outputs: aList - a list of frequencyDict's 5 politicalCounts
   """
   
   security = politicalCount(frequencyDict, 'nationalsecurity.txt') #find the national security politcalCount
   education = politicalCount(frequencyDict, 'education.txt') #find the education politcalCount
   economy = politicalCount(frequencyDict, 'economy.txt') #find the economy politcalCount
   healthcare = politicalCount(frequencyDict, 'healthcare.txt') #find the healthcare politicalCount
   environment = politicalCount(frequencyDict, 'environment.txt') #find the environment politcalCount
   aList = [security, education, economy, healthcare, environment] #make a list of the 5 politicalCounts
   return aList

def plotPoliticalDiff(bushAnalysis, obamaAnalysis):
    """
    plotPoliticalDiff takes in two lists bushAnalysis and obamaAnalysis and plots them on a bar
    graph.
    Inputs: bushAnalysis - the fullPoliticalAnalysis of President Bush's SoU speeches
            obamaAnalysis - the fullPoliticalAnalysis of President Obama's SoU speeches
    Outputs: None
    """
    
    # data to plot
    politicalCategories = 5 #needed to create the indexes
 
    fig, ax = plt.subplots()
    index = np.arange(politicalCategories) #create the indexes
    bar_width = 0.45 
    
    rects1 = plt.bar(index, bushAnalysis, bar_width, color='red', label='Bush') #plot the bars relevant to Bush
    rects2 = plt.bar(index + bar_width, obamaAnalysis, bar_width, color='blue', label='Obama') #plot the bars relevant to Obama
    
    plt.xlabel('Political Issues') #label the x-axis
    plt.ylabel('Number of Times Talked About the Issue') #label the y-axis
    plt.title('Political Issues by President (SOU Speeches)') #create the title
    plt.xticks(index + bar_width, ('National Security', 'Education', 'Economy', 'Healthcare', 'Environment')) #plot the ticks along the x-axis
    plt.legend(loc = 'upper right', shadow = True) #create the legend
      
    plt.tight_layout()
    plt.show() #create the graph
 
def main():
    """
    main() puts bush_all.txt and obama_all.txt through all of the functions and then
    graphs the results
    Inputs: None
    Outputs: None
    """
    
    f = open('bush_all.txt','rt', encoding = 'UTF-8') #open the file
    bushString = f.read() #convert the file into a string
    f.close() #close the file
    bushAnalysis = fullPoliticalAnalysis(wordCount(textPrep(bushString))) #do a full political analysis on President Bush
    f = open('obama_all.txt','rt', encoding = 'UTF-8') #open the file
    obamaString = f.read() #convert the file into a string
    f.close() #close the file
    obamaDict = fullPoliticalAnalysis(wordCount(textPrep(obamaString))) #do a full political analysis on President Obama
    plotPoliticalDiff(bushAnalysis, obamaAnalysis) #plot the graph
      
print() #print a blank line

main()

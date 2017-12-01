"""
   Count word frequency
   CSCI 203 project
   Fall 2017
   Student names(s): Logan Stiles and Alex Rabinovich
"""
import collections       # ordered dictionary for printing

#main()

def textPrep(filename):
    """
    textPrep takes in a .txt file and prepares all of the words so that they can be used
    by other functions. It takes all of the words in a file, and turns them into a list.
    textPrep then takes out every piece of unnessecary punction and makes every word lower
    case. textPrep then returns the list.
    Input: filename - a .txt file
    Output: textList - a list of words
    """
    
    f = open(filename,'rt', encoding = 'UTF-8') #open the file
    textString = f.read() #convert the file into a string
    textList = textString.split() #convert the string to a list
   
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

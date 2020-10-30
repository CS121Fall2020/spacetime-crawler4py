#owner : Jacob Martinez 
#authorized use is for cs121 soley and nothing else :-)
# testing to see if this works?

import sys
import re
from collections import defaultdict

'''
runtime complexity O(n^2)

removes non alphanumeric chars from each token if they arent already removed
'''
def stripUnderscores(text: list):
    return [i.strip('_][{}^!@#$%&*()</\\|-=+>? `~/*-') for i in text]

''' 
runtime complexity is O(n^3)*O(n*log(n)) because a list comprehension to remove all characters not 
removed from re.findall

a file is opened and each line is searched for all possible alphanumeric matches
After, is sent through another function that iterates through each token in the line removing 
non alphanumeric characters that got through the regular expression

'''
def tokenizer(fileName: str) -> list:
    try:
        t = []
        with open(fileName, encoding="utf-8") as open_file:
            for line in open_file: #O(n)
                x = re.findall(r"[a-zA-z0-9]+", line) #O(n*log(n))
                x = stripUnderscores(x) #O(n^2)
                t += x #O(1)

        return t
    except:
        print("Error in Tokenizer! File does not exist!")

'''
runtime complexity is O(n^2) because the dictionary makes all keys lowercase in order to 
make sure each key is can be the same case

Each word is put into lowercase and added to the defaultdict which increments using int class
'''
def computeWordFrequencies(tokenList: list) -> defaultdict:
    wordDict = defaultdict(int) # O(1)
    for i in tokenList: # O(n)
        wordDict[i.lower()] += 1 # O(1) + O(N)
    return wordDict # O(1)

'''
The run time complexity is O(n*log(n)) because I have to sort the dictionary into a list of tuples
in order to print the frequencies out in order

Each key and value is turned into a tuple in order from greatest value to lowest value of the tuples
and going from a to z for keys (with exception to numbers based on ascii values)

'''
def printFrequencies(Frequencies: defaultdict):
    sorted_dict = sorted(Frequencies.items(),key = lambda x : x[1], reverse = True) # O(n*log(n))
    for t in sorted_dict: # O(n)
        print(t[0],"-> ",t[1]) # O(1) + O(1) + O(1) + O(1) = O(1)

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise OSError("You have not input the proper amount of files.")
        tokens = tokenizer(sys.argv[1])
        wordDictionary = computeWordFrequencies(tokens)
        printFrequencies(wordDictionary)

    except:
        print("An error has occurred... Please try again with a different file")




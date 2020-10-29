#owner : Jacob Martinez 
#authorized use is for cs121 soley and nothing else :-)
from PartA import tokenizer,computeWordFrequencies
import sys
from collections import defaultdict


'''
runtime complexity would be O(len(m)+(len(n)) because two sets are being compared for similar values

each dictionary is turned int a set and compared with which values they have similar and the length of 
the set is printed out
'''
def compareDicts(words1: defaultdict, words2: defaultdict):
    print(len(set(words1.keys()).intersection(set(words2.keys())))) # O(1) + O(len(m)) + O(len(m)+len(n) + O(len(n))






if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise OSError("You have not input the proper amount of files.")
        tokenset1 = tokenizer(sys.argv[1])
        wordDictionary1 = computeWordFrequencies(tokenset1)
        tokenset2 = tokenizer(sys.argv[2])
        wordDictionary2 = computeWordFrequencies(tokenset2)
        compareDicts(wordDictionary1,wordDictionary2)

    except:
        print("An error has occurred...")

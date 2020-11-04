#owner : CS121 gang yeeeeeet
#authorized use is for cs121 soley and nothing else :-)
# testing to see if this works?

import sys
import re
from collections import defaultdict

#All the stop words... painfully hardcoded :')
stop_words = [
    "a","about","above","after","again","against","all","am","an",
    "and","any","are","aren't","as","at","be","because","been","before",
    "being","below","between","both","but","by","can't","cannot",
    "could","couldn't","did","didn't","do","does","doesn't","doing",
    "don't","down","during","each","few","for","from","further","had",
    "hadn't","has","hasn't","have","haven't","having","he","he'd",
    "he'll","he's","her","here","here's","hers","herself","him","himself",
    "his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is",
    "isn't","it","it's","its","itself","let's","me","more","most",
    "mustn't","my","myself","no","nor","not","of","off","on","once",
    "only","or","other","ought","our","ours","ourselves","out","over",
    "own","same","shan't","she","she'd","she'll","she's","should",
    "shouldn't","so","some","such","than","that","that's","the","their",
    "theirs","them","themselves","then","there","there's","these","they",
    "they'd","they'll","they're","they've","this","those","through","to",
    "too","under","until","up","very","was","wasn't","we","we'd","we'll",
    "we're","we've","were","weren't","what","what's","when","when's",
    "where","where's","which","while","who","who's","whom","why","why's",
    "with","won't","would","wouldn't","you","you'd","you'll","you're",
    "you've","your","yours","yourself","yourselves"
]
'''
runtime complexity O(n^2)

removes non alphanumeric chars from each token if they arent already removed
'''
def stripUnderscores(text: list):
    return [i.strip('_][{}^!@#$%&*()</\\|=+>?`~/*') for i in text]

 
'''
a file is opened and each line is searched for all possible alphanumeric matches
After, is sent through another function that iterates through each token in the line removing 
non alphanumeric characters that got through the regular expression

runtime complexity is O(n^3)*O(n*log(n)) because a list comprehension to remove all characters not 
removed from re.findall
'''
def tokenizer(fileName: str) -> list:
    try:
        t = []
        with open(fileName, encoding="utf-8") as open_file:
            for line in open_file: #O(n)
                x = re.findall(r"\w+['\w+]", line) #O(n*log(n))
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
    # for t in sorted_dict: # O(n)
    #     print(t[0],"-> ",t[1]) # O(1) + O(1) + O(1) + O(1) = O(1)
    print(sorted_dict)
    file = open("outputA.txt","w")
    for t in sorted_dict: # O(n)
        s  = t[0] + "-> " + str(t[1]) + '\n'
        file.write(s) # O(1) + O(1) + O(1) + O(1) = O(1)
    file.close()


#if a stop word exists in the dictionary, then remove it 
# as safe guard to prevent key error, I pop it and return None as value if it does not exist
def removeStopWords(Frequencies: defaultdict):
    for i in stop_words:
        Frequencies.pop(i,None)

#gets all 50 words after removing stop words
def topFifty(Frequencies:defaultdict):
    sorted_dict = sorted(Frequencies.items(),key = lambda x : x[1], reverse = True)
    Fifty = sorted_dict[0:50]
    newDic = defaultdict(int)
    for i in Fifty:
        newDic[i[0]] = i[1]
    return newDic

#writes to separate file so you can examine them
def printFifty(Frequencies:defaultdict):
    file = open("outputA.txt","w")
    sorted_dict = sorted(Frequencies.items(),key = lambda x : x[1], reverse = True)
    for t in sorted_dict: # O(n)
        s  = str(t[0]) + "-> " + str(t[1]) + '\n'
        file.write(s) # O(1) + O(1) + O(1) + O(1) = O(1)
    file.close()

if __name__ == '__main__':
    # string2 = '<p>Contents :</p><a href="https://uci.w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a></script>\n    <script src="bin/js/btt.js" type="text/javascript">\n    </script>\n    <script src="bin/js/menu_hover.js" type="text/javascript">\n    </script>\n    <!-- Accessibilty - START -->\n    <script type="text/javascript">\n    var _userway_config = {\n        /* uncomment the following line to override default position*/\n        /* position: \'2\', */\n        /* uncomment the following line to override default size (values: small, large)*/\n        /* size: \'small\', */\n        /* uncomment the following line to override default language (e.g., fr, de, es, he, nl, etc.)*/\n        /* language: \'en-US\', */\n        /* uncomment the following line to override color set via widget (e.g., #053f67)*/\n        /* color: \'#0064a4\', */\n        /* uncomment the following line to override type set via widget(1=person, 2=chair, 3=eye)*/\n        /* type: \'1\', */\n        /* uncomment the following line to override support on mobile devices*/\n        /* mobile: true, */\n        account: \'GTYOD4aROB\'\n    };\n    </script>\n    <script src="https://cdn.userway.org/widget.js" type="text/javascript">\n    </script>\n    <!-- Accessibilty - END -->\n</body>\n\n</html>'
    # tokens = tokenizer(string2)
    tokens = tokenizer("chunky.txt")
    dic = computeWordFrequencies(tokens)
    removeStopWords(dic)
    newFrequencies = topFifty(dic)
    printFifty(newFrequencies)
    



      

#returns updated l
# def getLinks(copy_line:str,links:list) -> list:
#     if (copy_line == ''):
#         return links
#     while("\'http" in copy_line or "\"http" in copy_line):
#         if("\'http" in copy_line):
#             link_index = copy_line.find("\'http")
#         elif("\"http" in copy_line):
#             link_index = copy_line.find("\"http")
#         sub_while = link_index
#         while (link_index < len(copy_line)):
#             if copy_line[i] == "\"" or copy_line[i] == "\'":
#                     links.append(line[link_index + 1 : i])
#                     copy_line = copy_line[i::]

# <![CDATA[\n!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=\'https://weatherwidget.io/js/widget.min.js\';fjs.parentNode.insertBefore(js,fjs);}}(document,\'script\',\'weatherwidget-io-js\');\n// ]]></script>\n END/weather widget -->
# def tokenizer(fileName: str) -> list:
#     links = list()
#     lines = fileName.split('\n')
#     for line in lines:
#         print(links)
#         urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
#         links += urls

#             #send to another function to get link
            
#     # for l in links:
#     #     print(l)
#     # return links
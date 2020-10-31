#owner : CS121 gang yeeeeeet
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
def tokenizer(fileName: str) -> list:
    links = list()
    lines = fileName.split('\n')
    for line in lines:
        print(links)
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
        links += urls

            #send to another function to get link
            
    # for l in links:
    #     print(l)
    # return links
   

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
    string2 = '<p>Contents :</p><a href="https://uci.w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a></script>\n    <script src="bin/js/btt.js" type="text/javascript">\n    </script>\n    <script src="bin/js/menu_hover.js" type="text/javascript">\n    </script>\n    <!-- Accessibilty - START -->\n    <script type="text/javascript">\n    var _userway_config = {\n        /* uncomment the following line to override default position*/\n        /* position: \'2\', */\n        /* uncomment the following line to override default size (values: small, large)*/\n        /* size: \'small\', */\n        /* uncomment the following line to override default language (e.g., fr, de, es, he, nl, etc.)*/\n        /* language: \'en-US\', */\n        /* uncomment the following line to override color set via widget (e.g., #053f67)*/\n        /* color: \'#0064a4\', */\n        /* uncomment the following line to override type set via widget(1=person, 2=chair, 3=eye)*/\n        /* type: \'1\', */\n        /* uncomment the following line to override support on mobile devices*/\n        /* mobile: true, */\n        account: \'GTYOD4aROB\'\n    };\n    </script>\n    <script src="https://cdn.userway.org/widget.js" type="text/javascript">\n    </script>\n    <!-- Accessibilty - END -->\n</body>\n\n</html>'
    tokens = tokenizer(string2)



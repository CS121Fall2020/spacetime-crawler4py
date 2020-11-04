'''
[X]Honor the politeness delay for each site
[]Crawl all pages with high textual information content
[]Detect and avoid infinite traps
[]Detect and avoid sets of similar pages with no information
[]Detect and avoid dead URLs that return a 200 status but no data (click here to see what the different HTTP status codes mean (Links to an external site.))
[]Detect and avoid crawling very large files, especially if they have low information value
'''
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from PartA import *
from PartB import *
import sys

#def allTags(url):
#tags_html = BeautifulSoup(html_url,"html.parser")
#tags = [tag.name for tag in tags_html.find_all()]
#global var holds urls we've been too
already_visted = set()
word_frequency_dict = dict()


'''
checks to make sure we are only adding domains to extracted links
if they are relvant to any of these sub domains 
'''
def checkDomain(extracted_links):
    valid_links = []
    for link in extracted_links:
        if link:
            # if link[0:4] != 'http':
            #     link = link[2:]
            #     print("!!!!!!!!!!! I made it here", link)
            if '.ics.uci.edu' in link:
                valid_links.append(link)
            elif '.cs.uci.edu' in link:
                valid_links.append(link)
            elif '.informatics.uci.edu' in link:
                valid_links.append(link)
            elif '.stat.uci.edu' in link:
                valid_links.append(link)
            elif 'today.uci.edu/department/information_computer_sciences' in link:
                valid_links.append(link)
    # for link in range 
    return valid_links
    

def url_texts(url,resp):
    stringy = ""
    try:
        data = resp.raw_response.content
        soup = BeautifulSoup(data, 'lxml')
        stringy = soup.get_text()
        print("@@@@@@@@@I am stringy" , stringy)
    except:
        print("This also didn't work")
    return stringy

'''
F(x) call(s):
    - extract_next_link
    - checkSubDomain
    - is_valid
we created a global set for all sites added to the extracted links
    - holds all unique websites that fit subdomain requirement
    - is used to cross compare with new extracted links to prevent pushing the same page info

Purpose: to get all info from a url possible
'''
def scraper(url, resp):    
    try:
        #adds url to a list of urls that have been visited
        #global already_visted
        print('we are in scraper')
        print('this is the type', resp.status)
        if(resp.status == 200 or resp.status == 601):
                
        #print(resp.error)
        #200 or 202
            print('checking content')
            soup = BeautifulSoup(resp.raw_response.content,'lxml')
            size_url_text = sys.getsizeof(soup.get_text())
            if(size_url_text <= 20000):
                print("SIZE OF THE TEXT AREA STUFF WITH THE PLACE AND WHAT NOT",size_url_text)
                #print(soup.get_text())
                url_text = soup.get_text()
                tokens = tokenizer(url_text)
                word_frequency = computeWordFrequencies(tokens)

                print('done checking')
        #call part A on the soup.get_text
        #something regarding valid HTTP response code
        #its contents
        #its sizeof()
        #see how many pages it has
        #get word count for each page
        # put all words together
        # extract next links
        
            url_texts(url, resp)
            already_visted.add(url)
            
            links = extract_next_links(url, resp)
            if not links:
                return []
            #returning the valid links
            valid_links = checkDomain(links)
            for l in valid_links:
                print("^^^^^^^^", l)

            return [link for link in valid_links if is_valid(link)]
        return []
    except:

        return []


'''
gets all of the links in the url and then gets rid of the links that have already 
been visited in extracted_links. Then updates the visited links to have the newly
extracted links.

Purpose: to get and return a list of the new links in the current url
'''
def extract_next_links(url, resp):
    # Implementation requred.
    extracted_links = []
    # ----------
    try:
        data = resp.raw_response.content
        soup = BeautifulSoup(data, 'lxml')
        # Extracting all the <a> tags into a list.
        tags = soup.find_all('a')
        # print(tags)
        # Extracting URLs from the attribute href in the <a> tags.
        for tag in tags:
            # print('in for') 
            extracted_links.append(tag.get('href'))
            # print(tag.get('href'))
        extracted_links = set(extracted_links)
        for i in already_visted:
            if i in extracted_links:
                extracted_links.remove(i)
        already_visted.union(set(extracted_links))
        extracted_links = list(extracted_links)
    
    except:
        print("It didn't work")
    # ----------
        
    return extracted_links

'''
Purpose: checks to make sure the url is valid.
    - valid sites are NOT special file types, such as: pdf,gif,png,mp4,etc.

Proposals: REDACTED
    
'''
def is_valid(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise

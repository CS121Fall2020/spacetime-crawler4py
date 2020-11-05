'''
[X]Honor the politeness delay for each site
[X]Crawl all pages with high textual information content
[X]Detect and avoid infinite traps
[-]Detect and avoid sets of similar pages with no information
[X]Detect and avoid dead URLs that return a 200 status but no data (click here to see what the different HTTP status codes mean (Links to an external site.))
[X]Detect and avoid crawling very large files, especially if they have low information value
'''
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from PartA import *
from PartB import *
import sys
from collections import defaultdict
#def allTags(url):
#tags_html = BeautifulSoup(html_url,"html.parser")
#tags = [tag.name for tag in tags_html.find_all()]
#global var holds urls we've been too
'''
checks to make sure we are only adding domains to extracted links
if they are relvant to any of these sub domains 
'''
def checkDomain(extracted_links):
    valid_links = []
    for link in range(0,len(extracted_links)):
        if extracted_links[link]:
            if ('http' not in extracted_links[link]):
                extracted_links[link] = extracted_links[link][2:]
            if("#" in extracted_links[link]):
                removeThisend = extracted_links[link].find("#")
                extracted_links[link] = extracted_links[link][:removeThisend]

    for link in extracted_links:
        if link:
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
    
    return valid_links

def scraper_text(url,resp):
    try:
            #application/pdf
            print('this is the type', resp.status)
            if(resp.raw_response.headers.get("content-type") == None or 'application' in resp.raw_response.headers.get("content-type")):
                return defaultdict(int)
            if((resp.status >= 200 and resp.status < 400) or (resp.status == 601)):
                print('checking text content')
                soup = BeautifulSoup(resp.raw_response.content,'lxml')
                url_text = soup.get_text()
                tokens = tokenizer(url_text)
                page_word_frequency_dict = defaultdict(int)
                page_word_frequency_dict = computeWordFrequencies(tokens)
                return page_word_frequency_dict
            return defaultdict(int)
    except AttributeError:
        return defaultdict(int)

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
#scraper_url
#You can check resp.raw_response.headers.get("content-type") to filter out pdf
def scraper(url, resp):    
    try:
        #application/pdf
        #adds url to a list of urls that have been visited
        #global already_visted
        print("***********************************")
        print("WEBSITE SCRAPING THROUGH",str(url))
        print('this is the type', resp.status)
        print("***********************************")
        if(resp.raw_response.headers.get("content-type") == None or 'application' in resp.raw_response.headers.get("content-type")):
                return []
        if((resp.status >= 200 and resp.status < 400) or (resp.status == 601)):
            print('checking link content')
            links = extract_next_links(url, resp)
            if not links:
                return []
            #returning the valid links
            valid_links = checkDomain(links)
            valid_links_set = set(valid_links)
            valid_links = list(valid_links_set)
            # for l in valid_links:
            #     print("^^^^^^^^", l)
            return [link for link in valid_links if is_valid(link)]
        return []
    except AttributeError:

        return []


'''
gets all of the links in the url and then gets rid of the links that have already 
been visited in extracted_links. Then updates the visited links to have the newly
extracted links.

Purpose: to get and return a list of the new links in the current url
'''
def extract_next_links(url, resp):
    extracted_links = []
    try:
        # Implementation requred.
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
        extracted_links = checkDomain(extracted_links)
        return extracted_links
    
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
            r".*\.(css|js|bmp|gif|jpeg|jpg|ico"
            + r"|png|r|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise

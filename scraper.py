import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from PartA import *
from PartB import *

#def allTags(url):
#tags_html = BeautifulSoup(html_url,"html.parser")
#tags = [tag.name for tag in tags_html.find_all()]
#global var holds urls we've been too
already_visted = set()

#scraper finds net urls to go to from current url
#things to check:
    #that we arent adding a link we started with
    #change is_valid to check the robot text
    #remove urls that are banned

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
    #*.ics.uci.edu/*
    #*.cs.uci.edu/*
    #*.informatics.uci.edu/*
    #*.stat.uci.edu/*
    #today.uci.edu/department/information_computer_sciences/*
    
    
def scraper(url, resp):    
    #adds url to a list of urls that have been visited
    #global already_visted
    already_visted.add(url)
    
    links = extract_next_links(url, resp)
    if not links:
        return []
    #returning the valid links
    valid_links = checkDomain(links)
    for l in valid_links:
        print("^^^^^^^^", l)

    return [link for link in valid_links if is_valid(link)]

#scrape the entire page for any other urls. 
#needs to not grab link that is the parameter 
def extract_next_links(url, resp):
    # Implementation requred.
    #
    extracted_links = []
    # return extracted_links
 
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
    except:
        print("It didn't work")
    # ----------

    # if resp.raw_response:
    #     resp = requests.get(url)
    # soup = BeautifulSoup(resp.text, 'lxml')

    # urls = []
    # for h in soup.find_all('h3'):
    # a = h.find('a')
    # urls.append(a.attrs['href'])


        # lines = resp.raw_response.content.decode("utf-8","ignore")
        # lines = lines.split('\n')
        # #print("Lines type is",type(lines[0]))
        # for line in lines:
        #     urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
        #     #urls = re.findall('http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\'', line)
            
        #     #if(urls[0]):
        #         #print("*********************:  " ,urls[0][:-1])
        #     extracted_links += urls
        
        # #resp.raw_response.content
        # #if url not in already_visted:
        #     # return extracted_links
    already_visted
    extracted_links = set(extracted_links)
    for i in already_visted:
        if i in extracted_links:
            extracted_links.remove(i)
    # for l in extracted_links:
    #     print("****", l)
    already_visted.union(set(extracted_links))
    extracted_links = list(extracted_links)
        
    return extracted_links

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
import re
from urllib.parse import urlparse
from PartA import *
from PartB import *

#global var holds urls we've been too
already_visted = set()

#scraper finds net urls to go to from current url
#things to check:
    #that we arent adding a link we started with
    #change is_valid to check the robot text
    #remove urls that are banned
    
def scraper(url, resp):
    print("*                                                                  *")
    
    ## the scraper is being called and raw_response.content prints the resp of the url
    #print(resp.raw_response.content)
    
    #adds url to a list of urls that have been visited
    global already_visted
    already_visted.add(url)
    
    links = extract_next_links(url, resp)
    if not links:
        return []
    #returning the valid links
    return [link for link in links if is_valid(link)]

#scrape the entire page for any other urls. 
#needs to not grab link that is the parameter 
def extract_next_links(url, resp):
    # Implementation requred.
    #
    extracted_links = []
    #links = list()
    #print("Type of response ", type(resp.raw_response.content))
    if resp.raw_response:
        lines = resp.raw_response.content.decode("utf-8","ignore")
        lines = lines.split('\n')
        #print("Lines type is",type(lines[0]))
        for line in lines:
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
            extracted_links += urls

        
        #resp.raw_response.content

        #if url not in already_visted:
            # return extracted_links
        
        global already_visted
        extracted_links = set(extracted_links)
        for i in already_visted:
            if i in extracted_links:
                extracted_links.remove(i)
        for l in extracted_links:
            print(l)
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
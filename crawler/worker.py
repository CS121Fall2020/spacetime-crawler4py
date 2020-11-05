from threading import Thread
from scraper import scraper_text
from utils.download import download
from utils import get_logger
from scraper import scraper
import time
from collections import defaultdict
from PartA import *

class Worker(Thread):
    def __init__(self, worker_id, config, frontier):
        self.logger = get_logger(f"Worker-{worker_id}", "Worker")
        self.config = config
        self.frontier = frontier
        self.set_of_links = set()
        self.url_dicts = dict()
        self.largest_page = ('',0)
        self.test_dic = defaultdict(int)
        super().__init__(daemon=True)
        
    def run(self):
        while True:
            # if (len(self.set_of_links) > 50):
            #     removeStopWords(self.test_dic)
            #     printFifty(topFifty(self.test_dic))
            #     Uniquepages = open("numUniquePages.txt",'w')
            #     s = 'The number of unique pages is '+ str(len(self.set_of_links))
            #     Uniquepages.write(s)
            #     Uniquepages.close()
            #     Largestpage = open("LargesPage.txt", 'w')
            #     l = 'The largest page is ' + str(self.largest_page[0]) + ' with a length of ' + str(self.largest_page[1])
            #     Largestpage.write(l)
            #     Largestpage.close()
            #     break

            removeStopWords(self.test_dic)
            printFifty(topFifty(self.test_dic))
            Uniquepages = open("numUniquePages.txt",'w')
            s = 'The number of unique pages is '+ str(len(self.set_of_links))
            Uniquepages.write(s)
            Uniquepages.close()
            Largestpage = open("LargesPage.txt", 'w')
            l = 'The largest page is ' + str(self.largest_page[0]) + ' with a length of ' + str(self.largest_page[1])
            Largestpage.write(l)
            Largestpage.close()
            tbd_url = self.frontier.get_tbd_url()

            if not tbd_url:
                removeStopWords(self.test_dic)
                printFifty(topFifty(self.test_dic))
                Uniquepages = open("numUniquePages.txt",'w')
                s = 'The number of unique pages is '+ str(len(self.set_of_links))
                Uniquepages.write(s)
                Uniquepages.close()
                Largestpage = open("LargesPage.txt", 'w')
                l = 'The largest page is ' + str(self.largest_page[0]) + ' with a length of ' + str(self.largest_page[1])
                Largestpage.write(l)
                Largestpage.close()
                self.logger.info("Frontier is empty. Stopping Crawler.")
                #this is where we print result of top 50 words
                #this is where we write a file of all sub domains in each domain
                break
            resp = download(tbd_url, self.config, self.logger)
            self.logger.info(
                f"Downloaded {tbd_url}, status <{resp.status}>, "
                f"using cache {self.config.cache_server}.")
            #print("herrrrrrooooooo                  *")
            scraped_urls = scraper(tbd_url, resp) # -- This gets the the url Links
            scraped_text = scraper_text(tbd_url,resp)
            self.url_dicts[str(tbd_url)] = scraped_text
            self.allWords(scraped_text)
            print('len(URLS)')
            print("========================================================")
            print(len(scraped_urls))
            print('len(TEXT)')
            print('========================================================')
            print(len(scraped_text))
            print('len(ALL TEXT)')
            print('========================================================')
            print(len(self.test_dic))
            if(sum(self.url_dicts[str(tbd_url)].values()) > self.largest_page[1]):
                self.largest_page = (str(tbd_url),sum(self.url_dicts[str(tbd_url)].values()))
            print('LARGEST PAGE')
            print('========================================================')
            print(self.largest_page[0],self.largest_page[1])
            for i in self.set_of_links:
                if i in scraped_urls:
                    scraped_urls.remove(i)
            self.set_of_links = self.set_of_links.union(set(scraped_urls))
            print('len(ALL URLS)')
            print('========================================================')
            print(len(self.set_of_links))
            #print("herrrrrrooooooo                  *")
            #this is where we add to our already visited set to stop repeats with 
            for scraped_url in scraped_urls:
                self.frontier.add_url(scraped_url)
            self.frontier.mark_url_complete(tbd_url)
            time.sleep(self.config.time_delay)

        
    def allWords(self,page_dict):
        print('inside allwords')
        for k,v in page_dict.items():
            self.test_dic[k] += v

     


            
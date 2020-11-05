from threading import Thread

from utils.download import download
from utils import get_logger
from scraper import scraper
import time


class Worker(Thread):
    def __init__(self, worker_id, config, frontier):
        self.logger = get_logger(f"Worker-{worker_id}", "Worker")
        self.config = config
        self.frontier = frontier
        self.set_of_links = set()
        super().__init__(daemon=True)
        
    def run(self):
        while True:
            tbd_url = self.frontier.get_tbd_url()
            if not tbd_url:
                #print("nothing                  *")
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
            #scraper_text = scraper_text(tbd_url,resp) -- This gets the text for that page
            #print("herrrrrrooooooo                  *")
            #this is where we add to our already visited set to stop repeats with 
            for scraped_url in scraped_urls:
                self.frontier.add_url(scraped_url)
            self.frontier.mark_url_complete(tbd_url)
            time.sleep(self.config.time_delay)

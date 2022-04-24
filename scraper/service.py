from bs4 import BeautifulSoup
from itertools import zip_longest
from googlesearch import search
import requests
import csv
import uuid

class ScrapeData(object):

    _HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def __init__(self, querystring) -> None:
        self.query = querystring
        self._urls_to_scrape = None

    def list_of_urls(self):
        raw_urls = set(search(self.query, tld= "co.in", num=20, start =0, stop=20, pause=2))
        scraped_urls = list([url for url in raw_urls if ("glassdoor.com" in url and "SRCH_KT" in url)])
        if scraped_urls:
            self._urls_to_scrape = scraped_urls[-1]

    def scrapingdata(self, scrapepage):
        '''scrapes data after takes html page as argument'''
        if not scrapepage:
            return []
        soup = BeautifulSoup(scrapepage, 'html.parser')
        results = soup.find(id='InterviewsSearchResults')
       

        if results:
            return None

        authordata = results.find_all(class_='authorInfo')  # company names
        quedata = results.find_all(class_='questionText')   # interview questions
        print(authordata, quedata)
        zipped = zip_longest(authordata, quedata, fillvalue='?')
        final_result = [(company_name.text, question.text) for company_name, question in list(zipped)]
        print(final_result)
        return final_result


    def scraped(self):
        '''function to give scrape_page takes url to scrape as argument'''
        
        scrapedpage = requests.get(self._urls_to_scrape, headers= ScrapeData._HEADERS)	
        if scrapedpage.status_code == 200:
            return scrapedpage.content

    def start_scraping(self):
        self.list_of_urls()
        print(self._urls_to_scrape)
        self.scrapingdata(self.scraped())


        
        


class FileWriter(object):

    def __init__(self, data, delimitter=",", quotechar='"') -> None:

        self.delimitter = delimitter
        self.quotechar = quotechar 
        self.filename = uuid.uuid4().hex + ".csv"
        self.scraped_data = data
    
    def _write_file(self):
        csvheader = ['Company name', 'Question']
        with open(self.filename, encoding="utf-8") as file:
            file_writer = csv.writer(file, self.delimitter, self.quotechar, quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(csvheader)
            file_writer.writerows(self.scraped_data)


if __name__ == "__main__":
    scraping = ScrapeData("python glassdoor interview questions")
    scraping.start_scraping()
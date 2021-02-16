# get serach results from google than work on urls
import argparse
import sys
import asyncio
import requests
import csv
from itertools import zip_longest
import socket


try: 
    from googlesearch import search as gsearch
    from bs4 import BeautifulSoup
except ImportError:  
    print("No module named 'google' found") 
    print("Exiting")
    sys.exit(0)



parser = argparse.ArgumentParser()
parser.add_argument("keyword", help="enter the keywords to scrape")
parser.add_argument("num", type = int, help="number of pages to scrape")
parser.add_argument("-tld", "--topleveldomain", type = str, help="Top level domain for google by default .com would be used")
args = parser.parse_args()

print(args.topleveldomain)


HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

  
# to search passing keyword to search

query = args.keyword  + "glassdoor interview questions"  



REMOTE_SERVER = "www.google.com"
def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

if is_connected(REMOTE_SERVER):
	pass
else:
	print("Net not connected")
	sys.exit(0)


#using set to remove duplicacy in urls
scrapeurls = list(set([url for url in gsearch(query, tld= args.topleveldomain or "co.in", num=20, start =0, stop=20, pause=2) if ("glassdoor.com" in url and "SRCH_KT" in url)]))






print(scrapeurls)

sys.exit(0)

def scraped(urltoscrape, headers):
	'''function to give scrape_page takes urlto escape as argument'''
	scrapedpage = requests.get(urltoscrape, headers= header)	
	if scrapedpage.status_code == 200:
		return scrapedpage.content
	return None



def scrapingdata(scrapepage):
	'''scrapes data after takes html page as argument'''
	soup = BeautifulSoup(scrapepage, 'html.parser')
	results = soup.find(id='InterviewsSearchResults')

	if results:
		return None

	authordata = results.find_all(class_='authorInfo')  # company names
	quedata = results.find_all(class_='questionText')   # interview questions
	zipped = zip_longest(authordata, quedata, fillvalue='?')
	final_result = [(company_name.text, question.text) for company_name, question in list(zipped)]

	return final_result




def filewrite(data, csvheader = ['Company name', 'Question'], filename= args.keyword+".csv"):
	''' Writes data to csv file. takes argument of filename and header list'''

	with open("filename", encoding="utf-8") as ftowrite:

		file_writer = csv.writer(ftowrite, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		file_writer.writerow(csvheader)
		file_writer.writerows(data)



def testfun(scrapeurls):

	for urltoscrape in scrapeurls:
		scrapepage = scraped(urltoscrape, headers= HEADER)
		if scrapepage:
			data = scrapingdata(scrapepage)
			if data:
				
		"https://www.glassdoor.co.in/Interview/python-interview-questions-SRCH_KO0,6.htm"
		"https://www.glassdoor.co.in/Interview/python-interview-questions-SRCH_KO0,6_IP"+str(i) +".htm"

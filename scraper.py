#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests



url = 'https://www.glassdoor.co.in/Interview/python-interview-questions-SRCH_KO0,6.htm'
url2 ='https://www.glassdoor.co.in/Interview/python-interview-questions-SRCH_KO0,6_IP3.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url2, headers=headers)


# In[ ]:


class ScrapeInterview:
    def __init__(self, url, multipage =False, pages = None)
        self.__header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.multipage = multipage
        self.url = url
        self.numpages = pages
    def scrapedata(self, url = None):
        if self.multipage and (self.numpages is not None):
            itvar= self.numpages
            while itvar >0:
                self.makerequest()
            
        
    
    def makerequest(self,):
        try:
            scrapedpage = requests.get(url2, headers=self.__header)
            if result.status_code == 200:
                return result
        except:
            return False
            


# In[21]:



type(result.status_code)


# In[14]:


from bs4 import BeautifulSoup


soup = BeautifulSoup(result.content, 'html.parser')


# In[15]:


results = soup.find(id='InterviewsSearchResults')


# In[16]:


authordata = results.find_all(class_='authorInfo')


# In[17]:


authordata[0].text


# In[ ]:





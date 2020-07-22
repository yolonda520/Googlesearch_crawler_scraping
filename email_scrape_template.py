# %%
# This problem will be tackled in 5 steps:
# 1 — Extract websites from google with googlesearch
# 2— Make a regex expression to extract emails
# 3 — Scrape websites using a Scrapy Spider
# 4 — Save those emails in a CSV file
# 5 — Put everything together

# %%
import logging
import os
import pandas as pd
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from googlesearch import search
logging.getLogger('scrapy').propagate = False

# %%
def get_urls(tag, n, language):
    urls = [url for url in search(tag, stop=n, lang=language)][:n]
    return urls

# %%
google_urls = get_urls('Boston tour', 300 , 'en')

# %%
# Scrape websites using a Scrapy Spider
class MailSpider(scrapy.Spider):
    
    name = 'email'
    
    def parse(self, response):
        
        links = LxmlLinkExtractor(allow=()).extract_links(response)
        links = [str(link.url) for link in links]
        links.append(str(response.url))
        
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_link) 
            
    def parse_link(self, response):
        
        for word in self.reject:
            if word in str(response.url):
                return
            
        html_text = str(response.text)
        mail_list = re.findall('\w+@\w+\.{1}\w+', html_text)

        dic = {'email': mail_list, 'link': str(response.url)}
        df = pd.DataFrame(dic)
        
        df.to_csv(self.path, mode='a', header=False)
        df.to_csv(self.path, mode='a', header=False)


# %%
def ask_user(question):
    response = input(question + ' y/n' + '\n')
    if response == 'y':
        return True
    else:
        return False
def create_file(path):
    response = False
    if os.path.exists(path):
        response = ask_user('File already exists, replace?')
        if response == False: return 
    
    with open(path, 'wb') as file: 
        file.close()

# %%
def get_info(tag, n, language, path, reject=[]):
    
    create_file(path)
    df = pd.DataFrame(columns=['email', 'link'], index=[0])
    df.to_csv(path, mode='w', header=True)
    
    print('Collecting Google urls...')
    google_urls = get_urls(tag, n, language)
    
    print('Searching for emails...')
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
    process.crawl(MailSpider, start_urls=google_urls, path=path, reject=reject)
    process.start()
    
    print('Cleaning emails...')
    df = pd.read_csv(path, index_col=0)
    df.columns = ['email', 'link']
    df = df.drop_duplicates(subset='email')
    df = df.reset_index(drop=True)
    df.to_csv(path, mode='w', header=True)
    
    return df

# %%
bad_words = ['facebook', 'instagram', 'youtube', 'twitter', 'wiki']
df = get_info('Boston tour', 300 , 'en', 'vendors_email_boston.csv', reject=bad_words)
  # %%
df.head()

# %%

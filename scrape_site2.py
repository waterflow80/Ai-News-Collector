# this script will scrape the site:
# https://news.mit.edu/topic/artificial-intelligence2
from news import News
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from datetime import datetime

url = "https://news.mit.edu/topic/artificial-intelligence2?page="
page_num = 0
base_url = "https://news.mit.edu"
# depth is the number of pages to go through in the site(1,2,3,...)

def get_news2(depth=1):
  #options = Options()
  #options.add_argument('--headless') # run selenium in the background
  driver = webdriver.Firefox()
  news_list = [] # list of News objects
  
  for i in range(depth):
    driver.get(url + str(i)) 
    
    items = driver.find_elements(By.CLASS_NAME, "page-term--views--list-item")
    for item in items:
      title = item.find_element(By.CLASS_NAME, "term-page--news-article--item--title--link").find_element(By.TAG_NAME, "span").text
      source_link = str(item.find_element(By.CLASS_NAME, "term-page--news-article--item--title--link").get_attribute("href"))
      content = item.find_element(By.CLASS_NAME, "term-page--news-article--item--dek").text
      date = item.find_element(By.CLASS_NAME, "term-page--news-article--item--publication-date").text
      image =str(item.find_element(By.TAG_NAME, "img").get_attribute("src"))
      
      # Converting the date into a python datetime object
      date = date.replace(",", "")
      dt_lst = date.split(" ")
      date2 = "/".join(dt_lst)
      date2 = datetime.strptime(date2, '%B/%d/%Y')
      news = News(title, content, date2, image, source_link)
      news_list.append(news)
      
  return news_list


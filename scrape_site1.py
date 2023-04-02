# This script will scrape the website 'https://www.sciencedaily.com/news/computers_math/artificial_intelligence/' and look for news
from news import News
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from datetime import datetime

url = "https://www.sciencedaily.com/news/computers_math/artificial_intelligence/#page="
base_url = "https://www.sciencedaily.com"

def get_news(depth:int=1):
  options = Options()
  options.add_argument('--headless') # run selenium in the background
  driver = webdriver.Firefox(executable_path='./firefox',options=options)  
  driver.get(url + str(depth))  

  news_list = [] # list of News objects
  time.sleep(3)
  # top headlines
  top_headlines_elements = driver.find_elements(By.CLASS_NAME, "col-sm-6")
  i = 0
  for element in top_headlines_elements:
    #print("iteration", i)
    i += 1
    title = element.find_element(By.TAG_NAME, "a").text
    content = element.find_element(By.CLASS_NAME, "latest-summary").text
    date = element.find_element(By.CLASS_NAME, "story-date").text
    image = None
    source_link = str(element.find_element(By.TAG_NAME, "a").get_attribute('href'))
    
    # Converting the date into a python datetime object
    date = date.replace(",", "")
    date = date.replace(".", "")
    date = date.rstrip('—')
    dt_lst = date.split(' ')
    date = '/'.join(dt_lst)
    date = date.rstrip('/')
    date2 = datetime.strptime(date, '%b/%d/%Y')
    news = News(title, content, date2, image, source_link)
    news_list.append(news)
    i += 1
  # Earlier Headlines
  latest_heads = driver.find_elements(By.CLASS_NAME, "latest-head")
  latest_summaries = driver.find_elements(By.CLASS_NAME, "latest-summary")
  i = 0
  for summary in latest_summaries:
    title = latest_heads[i].text
    content = summary.text
    date = summary.find_element(By.CLASS_NAME, 'story-date').text
    source_link =str(latest_heads[i].find_element(By.TAG_NAME, "a").get_attribute('href'))
    image = None
    # Converting the date into a python datetime object
    try:
      date = date.replace(",", "")
      date = date.replace(".", "")
      date = date.rstrip('—')
      dt_lst = date.split(' ')
      date = '/'.join(dt_lst)
      date = date.rstrip('/')
      date2 = datetime.strptime(date, '%b/%d/%Y')
      news = News(title, content, date2, image, source_link)
      news_list.append(news)
      i += 1
    except:
      continue
  
  return news_list

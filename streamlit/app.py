import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from scrape_site1 import get_news
from news import News
from scrape_site2 import get_news2
import random
from datetime import datetime
import calendar

st.set_page_config(page_title="My Webpage", layout="wide")

@st.experimental_singleton
def get_news_list():
      depth = 3 # for each site
      news_list = get_news(depth)   
      news_list.extend(get_news2(depth))
      random.shuffle(news_list)
      print("length is: ", len(news_list))
      return news_list


def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()


text = None
chosen_date = ['Any', 'Any', 'Any']

with st.sidebar:
  st.write("Filter By Date:")
  day = st.selectbox(
    'Day',
    ('Any','1', '2', '3', '4','5','6','7','8','9','10',
     '11','12','13','14','15','16','17','18','19','20'
     '21','22','23','24','25','26','27','28','29','30','31'))
  month = st.selectbox(
      'Month',
      ('Any','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))

  year = st.selectbox(
      'Year',
      ('Any','2023', '2022', '2021', '2020'))

  chosen_date = [day, month, year]
  st.write('Get News From:', "-".join(chosen_date))

  


# load assests
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_pJvtiSVyYH.json")
img_contact_form = Image.open("images/coding1.jpg")
img_lottie_animation = Image.open("images/coding2.jpg")


# header section
with st.container():
  st.subheader("Hi, I am Haroun :wave:")
  st.title("A Sofwtare Engineering Student From Tunisia")
  st.write("This website aims at collecting the latest ai news from different websites across the internet")

# How it wprks
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("How It Works ?")
    st.write("##")
    st.write("""
             This website searches for different ai news across multiple websites, including
             - https://www.sciencedaily.com/news
             - https://news.mit.edu/topic/artificial-intelligence2
             - More Websites will be added soon...""")
  with right_column:
    st_lottie(lottie_coding, height=300, key="coding")  

# # PROJECTS
# with st.container():
#   st.write("---")
#   st.header("My Projects")
#   st.write("##")
#   image_column, text_column = st.columns((1,2))
#   with image_column:
#     st.image(img_lottie_animation)
#   with text_column:
#     st.subheader("Integrate Lottie Animations Inside your Streamlit App")
#     st.write("""
#              learn bhow sdfo  dflnds odfn lsdkf dsf lkdjsf ldskfj oijdsfo dlfk dsofi jos jdfoj odjf .
#              sdf dslfjl ksdjf """)

# convert mmonth 


news_list = get_news_list() 


if chosen_date[0] != 'Any' and chosen_date[1] != 'Any' and chosen_date[2] != 'Any':
  day = chosen_date[0]
  month = chosen_date[1]
  year = chosen_date[2]
  with st.container():
    for i in range(len(news_list)):
      news = news_list[i]
      # Comparing datetime
      filter_date = datetime(int(year), list(calendar.month_name).index(month),int(day))
      if news.content and news.date >= filter_date:
        with st.container():
          st.write("---")
          st.write("##")
          image_column, text_column = st.columns((1,2))
          with image_column:
            if news.image == None:
              st.image(img_lottie_animation)
            else:
              st.image(news.image)
          with text_column:
            st.subheader(news.title)
            st.write("[Original Link >]("+ news.sourceLink +")")
            st.write(news.content)
            st.write(news.date)
else:
  for i in range(len(news_list)):
    news = news_list[i]
    if news.content:
      with st.container():
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
          if news.image == None:
            st.image(img_lottie_animation)
          else:
            st.image(news.image)
        with text_column:
          st.subheader(news.title)
          st.write("[Original Link >]("+ news.sourceLink +")")
          st.write(news.content)
          st.write(news.date.date())


# The filter option

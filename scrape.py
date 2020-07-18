
## My attempt at using twitterscraper ~~ Github
from twitterscraper import query_tweets 
import pandas as pd 
import datetime as dt


begin_date = dt.date(2020, 4, 15)
end_date = dt.date(2020, 4, 16)

limit = 1000
lang = 'english'

tweets = query_tweets("Seattle", begindate = begin_date, enddate = end_date, limit = limit, lang = lang)

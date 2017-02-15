import pandas as pd
import time
from twitter import *

##
#This is use to create the file Modesto.csv for this first time.   
###

config = {}
execfile("config.py", config)
filename = "Modesto.csv"

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

N =800   # just a big number. It should terminate before this.  



last_id = 874708522281689089
cols = ['screen_name', 'created_at', 'id', 'text', 'source', 'quote_from', 'user_mention0','retweeted_from', 'followers','friends','tweets','member_since','coordinates','place','user_location']
df = pd.DataFrame(columns = cols)




latitude = 37.578551	# geographical centre of search
longitude = -120.966177	# geographical centre of search
max_range = 15			# search range in kilometres

for n in range(N):

    query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)
    time.sleep(5)
    response = query['statuses']
    if len(response)<3 : break   #After the oldest available status has been obtained, the response should be the same tweet.  This should terminate the process once this happens
    for status in response:
            c0 = status["user"]["screen_name"]
            c1 = status["created_at"]
            c2 = str(status["id"])
            c3 = status["text"]
            c4 = status["source"]
            try : c5 = status["quoted_status"]["user"]["screen_name"]
            except : c5 = ""
            try : c6 = status["entities"]['user_mentions'][0]["screen_name"]  #reply to goes here, but also other mentions go here, so does retweeted
            except : c6 = ""
            try : c7 = status["retweeted_status"]["user"]["screen_name"]
            except : c7 = ""

            c8 = status["user"]["followers_count"]
            c9 = status["user"]["friends_count"]
            c10 = status["user"]["statuses_count"]
            c11 = status["user"]["created_at"]
            try: c12 = status["coordinates"]["coordinates"]
            except :c12 =''
            try : c13 = status["place"]["full_name"]
            except : c13 = ''

            c14 = status["user"]["location"]

            df.loc[len(df)]=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14]
    try : last_id = response[len(response)-1]['id']
    except : pass 


print "created dataframe with ", len(df), " total tweets.  Oldest is ", df.iloc[len(df)-1]["created_at"]
print "\n"
df.to_csv(filename, sep = '\t', index=False, encoding='utf-8')

quit()
      

#Use this stuff below near the top if you want to pick up where you left off

df = pd.read_csv(filename, sep = '\t',  encoding='utf-8')

last_id = df.iloc[len(df)-1]["id"]


import pandas as pd
import time
from twitter import *
#from collections import Counter


config = {}
execfile("config.py", config)
filename = "ModestoBeeFollowers.csv"

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))



#########  Used to create ModestoBeeFollowers. 
cols = ['screen_name', 'description', 'name','followers', 'friends', 'user_location', 'created_at','statuses_count','verified','id']
df = pd.DataFrame(columns = cols)
next = -1
n = 1 
error = 0
while (next!=0):
    if error==8 : break
    print "round: ", n, "\n"
    n = n+1
    print "total of  ", len(df), "added \n"
   
    try : m = twitter.followers.list(screen_name="modbee", count = 200, cursor = next)
    except :
        time.sleep(60)
        error = error + 1
        print "error ", error
        continue
    next = m['next_cursor']
    users = m['users']
    for u in users:
        c0 = u['screen_name']
        c1 = u['description']
        c2 = u['name']
        c3 = u['followers_count']
        c4 = u['friends_count']
        c5 = u['location']
        c6 = u['created_at']
        c7 = u['statuses_count']
        c8 = u['verified']
        c9 = u['id']
        df.loc[len(df)]=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]
    
    time.sleep(60)  #rate limit is 15 / 15 minute window

df.to_csv(filename, index=False, encoding='utf-8', sep='\t')

quit()
   











  

import pandas as pd
import time
from twitter import *

##
#This is used to take the big file and compare which users   
###

config = {}
execfile("config.py", config)
filename = "Modesto.csv"

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


df  = pd.read_csv("Modesto.csv", sep='\t')

dfm = df.groupby('screen_name').first()
dfm = dfm[['followers','friends','tweets','place','user_location']]
followers = [float(l) if type(l)==str and len(l)<10 else 0 for l in dfm.followers]   #followers is string for some reason. 
dfm.followers = followers
dfm.sort_values(by ='followers', ascending=False, inplace = True)
dfm.to_csv("Modesto_by_popular.csv")
quit()



  

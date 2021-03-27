import praw
import pandas as pd
from urllib.request import urlopen
import json
import requests
import datetime
import yfinance as yf

subreddit = 'pennystocks'
limit = 1000
timeframe = 'month'  # hour, day, week, month, year, all
listing = 'new'  # controversial, best, hot, new, random, rising, top

class Check:

    def get_reddit(self, subreddit, listing, limit, timeframe):
        try:
            base_url = f'https://www.reddit.com/r/{subreddit}/.json?limit={limit}&t={timeframe}'
            request = requests.get(base_url, headers={'User-agent': 'yourbot'})
        except:
            print('An Error Occured')
        return request.json()


    # def get_post_titles(self, r):
    #     posts = []
    #     for post in r['data']['children']:
    #         x = post['data']['title']
    #         posts.append(x)
    #     return posts


    def get_results(self, r):
        myDict = {}
        val1 = 0
        flairs = ["DD", "Catalyst", "Megathread", "Stock Info"]
        for post in r['data']['children']:
            '''
            This down here is to get the data using the flair, I will only filter those posts which have DD on their flair
            '''
            #print(post)
            if (post['data']['link_flair_richtext']):
                # print(post['data']['link_flair_richtext'][0]['t'])
                #print(post['data']['link_flair_richtext'][0])
                if ('t' in post['data']['link_flair_richtext'][0]):

                    if (post['data']['link_flair_richtext'][0]['t'] in flairs):
                        val1 = val1+1
                        print(post['data']['link_flair_richtext'][0]['t'])
                        # Converting the UTC time to the US/Eastern time zone to get the date in EST

                        print("Time:", datetime.datetime.fromtimestamp(post['data']['created_utc']))
                        print("Title:", post['data']['title'])
                        print("Score:", post['data']['score'])
                        print("Awards:", post['data']['total_awards_received'])
                        print("Upvote Ratio:", post['data']['upvote_ratio'])
                        print("____________________________________________________________________________________")


                        # myDict[post['data']['link_flair_richtext'][0]['t']] = {
                        #     'Time': datetime.datetime.fromtimestamp(post['data']['created_utc']),
                        #     'Title': post['data']['title'],
                        #     'Score': post['data']['score'],
                        #     'Awards': post['data']['total_awards_received'],
                        #     'Upvote Ratio': post['data']['upvote_ratio']
                        # }


        print(val1)
        df = pd.DataFrame.from_dict(myDict, orient='index')
        # df.to_csv('initial.csv')
        # print(df)
        return df




if __name__ == '__main__':
    firstOne = Check()
    # firstOne.firstStep()
    #r = firstOne.get_reddit(subreddit, listing, limit, timeframe)
    #df = firstOne.get_results(r)
    # print(df)
    # firstOne.usingAPI()



'''
Fixing the time frame on which I am going to analyse the stock after it was posted on reddit.

Lot of comparison time frame.

Controlled experimental frame (was it ever mentioned vs when it was mentioned)

A, B, C were mentioned and D, E, F, G weren't mentioned at all. 

General trend in market move. 
Restrict myself to the some 
'''
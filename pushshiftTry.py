import praw
import pandas as pd
from urllib.request import urlopen
import json
import requests
import datetime
import csv
import robin_stocks as rb

metaDict = {'id': [], 'created_utc': []}

class pushShift:

    def getStockSymbol(self, title):
        text = title.split()
        i = 0
        toprint = ""
        arrayoftickers = []

        while i < (len(text)):
            if text[i].isupper():

                toprint = text[i]
                if toprint[0] == "$" or toprint[0] == "“":
                    toprint = toprint[1:]

                if (toprint[len(toprint) - 1] == "." or toprint[len(toprint) - 1] == "?" or toprint[
                    len(toprint) - 1] == "!" or toprint[len(toprint) - 1] == "\""):
                    toprint = toprint[:-1]

                if len(toprint) < 2 or len(toprint) > 5:
                    toprint = ""

                if len(toprint) > 0:
                    return toprint
            i = i + 1
            toprint = ""

    def get_reddit(self, before):
        try:
            base_url = f'https://api.pushshift.io/reddit/search/submission/?&size=10000&before={before}&subreddit=pennystocks'
            request = requests.get(base_url)
        except:
            print('An Error Occured')
        return request.json()


    print("heloo")

    def checking(self):
        time = 1586447087
        #time = 1615717822
        #time1 = 0
        r = firstOne.get_reddit(time)

        while time > 1577924404:
            for post in r['data']:
                if ("removed_by_category" not in post):
                    if self.getStockSymbol(post['title']) is not None:
                        title = self.getStockSymbol(post['title'])
                        # rb.robinhood.stocks.get_name_by_symbol(title)

                        ticker = title
                        name = rb.robinhood.stocks.get_name_by_symbol(ticker)

                        if name == "":
                            name = ticker

                        flaired = ""
                        if 'link_flair_text' in post:
                            flaired = post['link_flair_text']

                        authorName = ""
                        if 'author_fullname' in post:
                            authorName = post['author_fullname']

                        upvoteRatio = 0.0
                        if 'upvote_ratio' in post:
                            upvoteRatio = post['upvote_ratio']

                        fields = [title, name, flaired, post['score'], upvoteRatio, post['num_comments'],
                                  post['created_utc'], post['id'], authorName, post['total_awards_received']]


                        #fields = [post['id'], post['created_utc']]
                        metaDict['id'].append(post['id'])
                        metaDict['created_utc'].append(post['created_utc'])

                        #time = post['created_utc']

                        with open(r'check1.csv', 'a') as f:
                            writer = csv.writer(f)
                            writer.writerow(fields)

            time = metaDict['created_utc'][-1]
            #print(datetime.datetime.fromtimestamp(time))

            r = firstOne.get_reddit(time)


if __name__ == '__main__':
    firstOne = pushShift()

    "DON'T RUN THIS, DON'T RUN THIS, DON'T RUN THIS"


    #r = firstOne.get_reddit()
    #firstOne.checking()
    #print(metaDict)
    #df = pd.DataFrame.from_dict(data1)

    # dataDict = {"Symbol": [], "Stock": [], "Post Flair": [], "Score": [], "Upvote ratio": [], "Number of Comments": [],
    #              "Post Date": [], "Post Id": [], "Posted by": [], "Total Awards Received": []}
    #
    # df = pd.DataFrame.from_dict(dataDict)
    # df.to_csv("check1.csv")

    #df.to_csv("postId.csv", index = True)


    #1606721644: Nov 25 2020
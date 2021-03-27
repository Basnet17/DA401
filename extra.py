import praw
import pandas as pd
from urllib.request import urlopen
import json
import requests
import datetime
import yfinance as yf
from datapackage import Package
import robin_stocks as rb
import csv

subreddit = 'pennystocks'
limit = 1000
timeframe = 'month'  # hour, day, week, month, year, all
listing = 'new'  # controversial, best, hot, new, random, rising, top
blacklistWords = ["THE", "None"]
mainDict = {}
dataDict = {"Symbol": [], "Stock": [], "Post Flair": [], "Score": [], "Upvote ratio": [], "Number of Comments": [], "Post Date": []}

#flairListRob = ["DD/Research", "", "Megathread", "Bullish"]

class UsingPraw:

    # Binary Search to find the stock symbol on the very long list
    def binary_search(self, arr, low, high, x):
        # Check base case
        if high >= low:

            mid = (high + low) // 2
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return self.binary_search(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1

    def getNASDAQ(self):
        package = Package('https://datahub.io/core/nasdaq-listings/datapackage.json')
        mainList = []
        insideList1 = []
        insideList2 = []

        for resource in package.resources:
            if resource.descriptor['datahub']['type'] == 'derived/csv':
                for stck in resource.read():
                    insideList1.append(stck[0])
                    insideList2.append(stck[1])

        mainList.append(insideList1)
        mainList.append(insideList2)
        return mainList

    def findStock(self):
        mainList = self.getNASDAQ()
        insideList1 = mainList[0]
        len1 = len(insideList1)-1
        insideList2 = mainList[1]

        print(self.binary_search(insideList1, 0, len1, "EEENF"))
        #print(insideList1[5])
        #print(insideList2)

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


    def firstStep(self):
        reddit = praw.Reddit(client_id="irz9TYR3Q-Z6ow",  # my client id
                             client_secret="yKrnoH42fdtuuIpQmjKjLwLgTnKoEQ",  # your client secret
                             user_agent="DA401 script",  # user agent name
                             username="Basnet17",  # your reddit username
                             password="")  # your reddit password

        sub = ['']  # make a list of subreddits you want to scrape the data from
        idData = pd.read_csv("DataCollected/finalId.csv")
        print(idData)

        # print(row[0])

        #for ind in idData.index:
        #    print(idData[id][ind])

        for index, row in idData.iterrows():

            submissionId = row[0]
            post = reddit.submission(id=submissionId)

            if self.getStockSymbol(post.title) is not None:
                title = self.getStockSymbol(post.title)
                #rb.robinhood.stocks.get_name_by_symbol(title)

                ticker = title
                name = rb.robinhood.stocks.get_name_by_symbol(ticker)

                fields = [title, name, post.link_flair_text,post.score, post.upvote_ratio,post.num_comments,post.created_utc]

                with open(r'DataCollected/FinalData.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)


if __name__ == '__main__':
    #firstOne = UsingPraw()

    "DON'T RUN THIS, DON'T RUN THIS, DON'T RUN THIS"


    #firstOne.firstStep()
    # dataDict = {"Symbol": [], "Stock": [], "Post Flair": [], "Score": [], "Upvote ratio": [], "Number of Comments": [],
    #             "Post Date": []}
    # df = pd.DataFrame.from_dict(dataDict)
    # df.to_csv("FinalData.csv")
    #print(dataDict)
    #print(data)
    #df = pd.DataFrame.from_dict(dataDict)

    #df.to_csv("mainData.csv", index = True)


    #rb.tda.authentication.login_first_time()
    #print(rb.tda.stocks.get_instrument("EEENF"))
    #firstOne.firstStep()

    #val1 = "$PRI"
    #print(val1.isupper())
    # r = firstOne.get_reddit(subreddit, listing, limit, timeframe)
    # df = firstOne.get_results(r)
    # print(df)
    # firstOne.usingAPI()

    # print("-------------------------------------------------------")
    # print(post.score)
    # print(post.upvote_ratio)
    # print(post.num_comments)
    # print(post.link_flair_text)
    # print(datetime.datetime.fromtimestamp(post.created_utc))

    '''
            # submission = reddit.submission(id="m4stih")
            # print(submission.title)
            # print(datetime.datetime.fromtimestamp(submission.created_utc))
            # print(submission.link_flair_text)
            # print("Here are the penny stocks new posts")
            # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            # all_posts = reddit.subreddit('robinhoodpennystocks').hot(limit=10)
            # for post in all_posts:
            #     print(post.id)

            for s in sub:
                # subreddit = reddit.subreddit(s)  # Chosing the subreddit
                all_posts = reddit.subreddit('robinhoodpennystocks').hot(limit=10000)
                for post in all_posts:
                    #print(post.link_flair_text)
                    if self.getStockSymbol(post.title) != None:

                        title = self.getStockSymbol(post.title)
                        rb.robinhood.stocks.get_name_by_symbol(title)

                        ticker = title
                        name = rb.robinhood.stocks.get_name_by_symbol(ticker)
                        dataDict["Symbol"].append(title)

                        dataDict["Stock"].append(name)
                        print(post.created_utc)
                        time = datetime.datetime.fromtimestamp(post.created_utc).strftime("%m/%d/%Y %H:%M:%S")
                        print(time)
                        dataDict["Post Date"].append(time)
                        dataDict["Post Flair"].append(post.link_flair_text)
                        dataDict["Score"].append(post.score)
                        dataDict["Upvote ratio"].append(post.upvote_ratio)
                        dataDict["Number of Comments"].append(post.num_comments)
    '''
    # dataDict["Symbol"].append(title)

    # dataDict["Stock"].append(name)

    # time = datetime.datetime.fromtimestamp(post.created_utc).strftime("%m/%d/%Y %H:%M:%S")

    # dataDict["Post Date"].append(time)
    # dataDict["Post Flair"].append(post.link_flair_text)
    # dataDict["Score"].append(post.score)
    # dataDict["Upvote ratio"].append(post.upvote_ratio)
    # dataDict["Number of Comments"].append(post.num_comments)
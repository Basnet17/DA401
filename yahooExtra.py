import yfinance as yf
import praw
import pandas as pd
from urllib.request import urlopen
import json
import requests
import datetime
from datetime import timedelta
from datetime import timezone
import yfinance as yf
from datapackage import Package
import robin_stocks as rb
import re
import csv

import requests
import investpy

from googlefinance import getQuotes
import json


class Extra:
    def getData(self):
        # r = requests.get('https://finnhub.io/api/v1/search?q=apple&token=c1fn8jv48v6r34ehftkg')
        # print(r.json())

        # df = investpy.get_stock_historical_data(stock='AAPL',
        #                                         country='United States',
        #                                         from_date='01/01/2020',
        #                                         to_date='01/20/2020')
        #
        # for i in range(1, 15):
        #    print(df['Open'][i])

        company_profile = investpy.get_stock_company_profile(stock='ZOM',
                                                             country='United States')
        print(company_profile)


    def makeDictionary(self):
        megaDict = {}

        megaDict["Date"] = []
        megaDict["Present Day"] = []
        for i in range(1, 15):
            megaDict["-" + str(i)] = []
            megaDict["+" + str(i)] = []
        df = pd.DataFrame.from_dict(megaDict)
        df.to_csv("14daysTest.csv", index=False)

    def checkYahoo(self):
        mainData = pd.read_csv("biggerFile.csv")
        stoppedIndex = 0
        for index, row in mainData.iterrows():
            if index > stoppedIndex:
                value1 = re.sub('[^A-Za-z0-9.]+', '', row[0])

                print(value1)

                #ticker = yf.Ticker(value1)

                #hist = ticker.history(period="day")

                # onlyDate = datetime.datetime.fromtimestamp(row[6]).date()

                dateTime = datetime.datetime.fromtimestamp(row[6])

                dateOnly = dateTime.strftime("%Y-%m-%d")

                priceList = []

                priceList.append(dateOnly)

                if value1 == "HOT" or value1 == "DD":
                    for i in range(1, 15):
                        priceList.append(-1)

                try:
                    subDays = dateTime - timedelta(days=14)
                    addDays = dateTime + timedelta(days=14)

                    subbedDate = subDays.strftime("%Y-%m-%d")
                    addedDate = addDays.strftime("%Y-%m-%d")

                    df1 = investpy.get_stock_historical_data(stock=value1,
                                                            country='United States',
                                                            from_date=subbedDate,
                                                            to_date=dateOnly)


                    df2 = investpy.get_stock_historical_data(stock=value1,
                                                            country='United States',
                                                            from_date=dateOnly,
                                                            to_date=addedDate)



                except:
                    print("Error")
                #
                # else:
                #     if (len(hist.index) > 0):
                #         dataThatDay = yf.download(value1, dateOnly)
                #         priceList.append(round(dataThatDay['Close'][0], 4))
                #     else:
                #         priceList.append(-1)
                #
                #     for i in range(1, 15):
                #         subDays = dateTime - timedelta(days=i)
                #         addDays = dateTime + timedelta(days=i)
                #
                #         subbedDate = subDays.strftime("%Y-%m-%d")
                #         addedDate = addDays.strftime("%Y-%m-%d")
                #
                #         if (len(hist.index) > 0):
                #             dataSub = yf.download(value1, subbedDate)
                #
                #             if (len(dataSub.index) > 0):
                #
                #                 priceList.append(round(dataSub["Close"][0], 4))
                #
                #                 timestamp = addDays.replace(tzinfo=timezone.utc).timestamp()
                #
                #                 if (timestamp > 1616714404):
                #                     priceList.append(-1)
                #
                #                 else:
                #                     dataAdd = yf.download(value1, addedDate)
                #
                #                     priceList.append(round(dataAdd["Close"][0], 4))
                #
                #             else:
                #                 priceList.append(-1)
                #
                #         else:
                #             priceList.append(-1)

                with open(r'14daysTest.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(priceList)


if __name__ == '__main__':
    firstCall = Extra()
    firstCall.getData()
    #firstCall.makeDictionary()
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

class Yfin:
    def removeBadNames(self):
        #msft = yf.Ticker("FUCK")
        #hist = msft.history(period="day")
        #info = msft.info
        #print(info)

        mainData = pd.read_csv("cleaned1.csv")
        #print(mainData["Unnamed: 0"])
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[DD]"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[DD"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[EU]"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[PSA]"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[NOOB"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[US]"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[OTC"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[PART"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[NEW"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[NEW]"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[OTC:"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[DD,"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[FOR"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[UK"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[A"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[WELL"]
        # mainData = mainData[mainData["Unnamed: 0.1"] != "[UK]"]
        # mainData.to_csv("cleaned1.csv")
        #mainData = mainData.drop("Unnamed: 0.1", 1)

        # count = 0
        # for index, row in mainData.iterrows():
        #     value1 = re.sub('[^A-Za-z0-9.]+', '', row[0])
        #     mainData.at[index, row[0]] = value1
        #
        # mainData.to_csv("cleaned2.csv", index = False)
        #df_updated = mainData["Unnamed: 0"].replace(to_replace= , value = )



        # symbolDict = {}
        # for index, row in mainData.iterrows():
        #     # if row[3] == "Catalyst":
        #     #     count = count +1
        #     if row[1][0] == '[':
        #         if row[1] not in symbolDict:
        #             symbolDict[row[1]] = 1
        #         else:
        #             symbolDict[row[1]] += 1
        #
        # print(symbolDict)
        #return mainData

    def makeDictionary(self):
        megaDict = {}

        megaDict["Date"] = []
        megaDict["Present Day"] = []
        for i in range(1, 15):
            megaDict["-" + str(i)] = []
            megaDict["+" + str(i)] = []
        df = pd.DataFrame.from_dict(megaDict)
        df.to_csv("14days.csv", index = False)

    def checkYahoo(self):
        mainData = pd.read_csv("cleaned1.csv")
        stoppedIndex = 8275
        for index, row in mainData.iterrows():
            if index > stoppedIndex:
                value1 = re.sub('[^A-Za-z0-9.]+', '', row[0])

                print(value1)

                ticker = yf.Ticker(value1)

                hist = ticker.history(period="day")

                #onlyDate = datetime.datetime.fromtimestamp(row[6]).date()

                dateTime = datetime.datetime.fromtimestamp(row[6])

                dateOnly = dateTime.strftime("%Y-%m-%d")

                priceList = []

                priceList.append(dateOnly)

                if value1 == "HOT" or value1 == "DD":
                    for i in range(1, 15):
                        priceList.append(-1)

                else:
                    if (len(hist.index) > 0):
                        dataThatDay = yf.download(value1, dateOnly)
                        priceList.append(round(dataThatDay['Close'][0],4))
                    else:
                        priceList.append(-1)

                    for i in range(1,15):
                        subDays = dateTime - timedelta(days = i)
                        addDays = dateTime + timedelta(days = i)

                        subbedDate = subDays.strftime("%Y-%m-%d")
                        addedDate = addDays.strftime("%Y-%m-%d")


                        if (len(hist.index) > 0):
                            dataSub = yf.download(value1, subbedDate)

                            if (len(dataSub.index) > 0):

                                priceList.append(round(dataSub["Close"][0],4))

                                timestamp = addDays.replace(tzinfo=timezone.utc).timestamp()

                                if (timestamp > 1616714404):
                                    priceList.append(-1)

                                else:
                                    dataAdd = yf.download(value1, addedDate)

                                    priceList.append(round(dataAdd["Close"][0],4))

                            else:
                                priceList.append(-1)

                        else:
                            priceList.append(-1)


                with open(r'14days.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(priceList)


if __name__ == '__main__':
    #financials = Yfin()
    #financials.extractInfo()
    firstOne = Yfin()
    #firstOne.removeBadNames()

    '''
    Run this function to grab data from Yahoo finance related to that specific stock
    '''
    firstOne.checkYahoo()

    # ticker = yf.Ticker("ADOM")
    # old = yf.download("AITX", "2020-12-30")
    # print(old['Close'][0])



    # checkData = pd.read_csv("cleaned1.csv")
    # for index, row in checkData.iterrows():
    #     if index == 8276:
    #         print(row[0])


    #print(data1)

    #3979
    # print(mainData)
    # mainData = mainData[(mainData["Unnamed: 0"] != "DD") | (mainData["Unnamed: 0"] != "DD:") | (mainData["Unnamed: 0"] != "US") |
    #                     (mainData["Unnamed: 0"] != "[New") | (mainData["Unnamed: 0"] != "OTC") | (mainData["Unnamed: 0"] != "(US)")]

    # mainData = mainData[mainData["Unnamed: 0"] != "DD"]
    # mainData = mainData[mainData["Unnamed: 0"] != "DD:"]
    # mainData = mainData[mainData["Unnamed: 0"] != "US"]
    # mainData = mainData[mainData["Unnamed: 0"] != "[New"]
    # mainData = mainData[mainData["Unnamed: 0"] != "OTC"]
    # mainData = mainData[mainData["Unnamed: 0"] != "(US)"]

    # mainData = mainData[mainData["Unnamed: 0"] != "DD"]
    # mainData.to_csv("cleaned1.csv")

    # checccc = {'Close':[], 'Open': []}
    # df = pd.DataFrame.from_dict(checccc)
    # df.to_csv("crap.csv", index=False)
    #
    # ticker = yf.Ticker("SNWR")
    # old = yf.download("SNWR", "2020-10-01")
    # print(old['Close'][0])
    #
    # old1 = yf.download("SNWR", "2020-10-02")
    # print(old1['Close'][0])
    #
    # old2 = yf.download("SNWR", "2020-10-04")
    # print(old2['Close'][0])
    #
    # old4 = yf.download("SNWR", "2020-09-30")
    # print(old4['Close'][0])
    #
    # old5 = yf.download("SNWR", "2020-09-29")
    # print(old5['Close'][0])
    #
    # list1 = []
    # with open(r'crap.csv', 'a') as f:
    #     writer = csv.writer(f)
    #     list1.append(old['Close'][0])
    #     list1.append(old['Open'][0])
    #     writer.writerow(list1)
    #     #writer.writerow(old['Open'])





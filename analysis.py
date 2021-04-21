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

class Analysis:
    def mergeTwoDatasets(self):
        print("Combining total dataset")
        redditData = pd.read_csv('FirstDraft/draftReddit.csv')
        stockData = pd.read_csv('FirstDraft/14days.csv')

        # Subsetting the reddit data for early results
        #subsetReddit = redditData[0:28227]
        #subsetReddit.to_csv('FirstDraft/draftReddit.csv', index=False)
        #redditData = redditData.reset_index()

        #combinedDataSet = pd.concat([redditData, stockData], axis = 1)

        #combinedDataSet.to_csv('FirstDraft/combinedDataset.csv')

        #totalDataSet = pd.read_csv('FirstDraft/combinedDataset.csv')
        #print(totalDataSet)
        #totalDataSet = totalDataSet.drop('Total Awards Received', axis=1)
        #totalDataSet.to_csv('totalDataSet.csv', index=False)

    def cleaningTotalDataset(self):
        print("Cleaned the dataset and removed all symbols which couldn't be found")
        #totalData = pd.read_csv('EarlyResultsData/totalDataSet.csv')
        #print(totalData['Number of Comments'].mean())
        #totalData = totalData[totalData['Present Day'] != -1]
        #totalData.to_csv('FinalDataForEarly.csv', index=False)

        draftData = pd.read_csv('FirstDraft/combinedDataset.csv')
        draftData = draftData[draftData['Present Day'] != -1]
        draftData.to_csv('FirstDraft/FinalDataForDraft.csv', index=False)

    def workingWithActual(self):
        actualData = pd.read_csv('EarlyResultsData/FinalDataForEarly.csv')
        print(actualData)

    def smalldataset(self):
        smallData = pd.read_csv('FirstDraft/fixColumn.csv')
        smallData = smallData.drop('Unnamed: 0', axis = 1)
        smallData.to_csv('FirstDraft/fixColumn.csv', index = False)


if __name__ == '__main__':
    analysis = Analysis()
    #analysis.mergeTwoDatasets()
    analysis.cleaningTotalDataset()
    #analysis.workingWithActual()
    #analysis.smalldataset()
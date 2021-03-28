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
        #redditData = pd.read_csv('EarlyResultsData/earlyReddit.csv')
        #stockData = pd.read_csv('EarlyResultsData/14days.csv')

        # Subsetting the reddit data for early results
        #subsetReddit = redditData[0:14268]
        #subsetReddit.to_csv('EarlyResultsData/earlyReddit.csv')

        #combinedDataSet = pd.concat([redditData, stockData], axis = 1)

        #combinedDataSet.to_csv('EarlyResultsData/combinedDataset.csv')

        #totalDataSet = pd.read_csv('EarlyResultsData/combinedDataset.csv')
        #totalDataSet = totalDataSet.drop('Total Awards Received', axis=1)
        #totalDataSet.to_csv('totalDataSet.csv', index=False)

    def cleaningTotalDataset(self):
        print("Cleaned the dataset and removed all symbols which couldn't be found")
        #totalData = pd.read_csv('EarlyResultsData/totalDataSet.csv')
        #print(totalData['Number of Comments'].mean())
        #totalData = totalData[totalData['Present Day'] != -1]
        #totalData.to_csv('withoutNegOnes.csv', index=False)

    def workingWithActual(self):
        actualData = pd.read_csv('EarlyResultsData/withoutNegOnes.csv')
        print(actualData)

if __name__ == '__main__':
    analysis = Analysis()
    #analysis.mergeTwoDatasets()
    #analysis.cleaningTotalDataset()
    analysis.workingWithActual()
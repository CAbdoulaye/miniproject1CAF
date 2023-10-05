# INF601 - Advanced Programming in Python
# Cheikh Abdoulaye Faye
# Mini Project 1

import numpy
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def selectStockTicker(list):
    # function returns list of valid stock ticker objects
    tickers = []
    '''
    print("Enter 5  stocks to graph:")
    for i in range(5):
        while True:
            stockName = input("Enter stock ticker number " + str(i + 1) + ": ")
            try:
                stock = yf.Ticker(stockName)
                stock.info
                tickers.append(stock)
                break
            except:
                print("The stock ticker you have entered is not valid")
    '''
    for name in list:
        stock = yf.Ticker(name)
        tickers.append(stock)
    return tickers



def getHistInfo(stockList):
    # function returns list of stock ticker history for last 10 days
    hist = []
    for i in range(5):
        history = stockList[i].history(period="10d")
        hist.append(history)
    return hist

def getClosingPrice(histList):
    # function returns list of stocks prices for last 10 days
    priceList = []
    for date in histList:
        prices = []
        for price in date['Close']:
            prices.append(round(price, 2))
        priceList.append(prices)
    return priceList

def listToNumpyArray(priceList):
    # function to return list of prices in numpy array
    listOfNumpyArrays = []
    for companyStock in priceList:
        arr = numpy.array(companyStock)
        listOfNumpyArrays.append(arr)

    return listOfNumpyArrays

def plotAndShowGraphAndTurnToPNG(stockArrList, names):
    # function to plot and show array
    i = 0
    xAxes = numpy.array([1,2,3,4,5,6,7,8,9,10])
    for arr in stockArrList:
        # Plot each graph
        sortedPrices = list(arr)
        sortedPrices.sort()
        min = sortedPrices[0]
        max = sortedPrices[-1]
        plt.plot(xAxes, arr)
        plt.axis([1, 10, (min - (max - min) / 2), (max + (max - min) / 2)])
        plt.xlabel("Days")
        plt.ylabel("Closing Price")
        plt.title("Close price for " + names[i])

        # Save graphs to png files
        fileName = "Charts/" + names[i] + ".png"
        plt.savefig(fileName)

        #show graph
        plt.show()
        i = i + 1

# Created Chart Folder if it doesn't exist already
try:
    Path("Charts").mkdir()
except:
    pass

stockNames = ["MSFT", "DELL", "AAPL", "NKE", "SONY"]

stockList = selectStockTicker(stockNames)

histList = getHistInfo(stockList)

priceList = getClosingPrice(histList)

listOfArrays = listToNumpyArray(priceList)

plotAndShowGraphAndTurnToPNG(listOfArrays, stockNames)


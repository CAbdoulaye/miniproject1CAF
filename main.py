#(5/5 points) Proper import of packages used.
#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
#(10/10 points) Store this information in a list that you will convert to a array in NumPy.
#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.
import numpy
# INF601 - Advanced Programming in Python
# Cheikh Abdoulaye Faye
# Mini Project 1



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


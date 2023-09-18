#(5/5 points) Proper import of packages used.
#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
#(10/10 points) Store this information in a list that you will convert to a array in NumPy.
#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.


# INF601 - Advanced Programming in Python
# Cheikh Abdoulaye Faye
# Mini Project 1



import yfinance as yf

def selectStockTicker():
    tickers = []
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
    return tickers

def getHistInfo(stockList):
    hist = []
    for i in range(5):
        history = stockList[i].history(period="10d")
        hist.append(history)
    return hist



stockList = selectStockTicker()
#print(stockList)
histList = getHistInfo(stockList)
#print(histList)

# get historical market data
#hist = msft.history(period="1mo")
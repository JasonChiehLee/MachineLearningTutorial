import urllib.request

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BNS.TO&apikey=44HXP3G43NNQ1MAP&datatype=csv&outputsize=full"
testfile = urllib.request.URLopener()

testfile.retrieve(url, "ScotiaBankData.csv")
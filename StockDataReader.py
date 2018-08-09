import pandas as pd
import urllib.request


def get_stock_data(ticker):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey=44HXP3G43NNQ1MAP&datatype=csv&outputsize=full'.format(ticker)
    urlOpener = urllib.request.URLopener();
    urlOpener.retrieve(url, "{}.csv".format(ticker))
    return pd.read_csv("{}.csv".format(ticker))     
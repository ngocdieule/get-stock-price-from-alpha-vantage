import pandas as pd
import requests
from config import settings

class AlphaVantageAPI:
    def __init__(self, api_key=settings.ALPHA_API_KEY):
        self.__api_key = api_key

    def get_daily(self, ticker, output_size = "full"):
        """Get daily time series of an equity from AlphaVantage API.

        Parameters
        ----------
        ticker : str
            The ticker symbol of the equity.
        output_size : str, optional
            Number of observations to retrieve. "compact" returns the
            latest 100 observations. "full" returns all observations for
            equity. By default "full".

        Returns
        -------
        pd.DataFrame
            Columns are 'open', 'high', 'low', 'close', and 'volume'.
            All columns are numeric.
        """
        # Create URL
        url = (
            "https://www.alphavantage.co/query?"
            "function=TIME_SERIES_DAILY&"
            f"symbol={ticker}&"
            f"outputsize={output_size}&"
            f"datatype=json&"
            f"apikey={self.__api_key}"
        )
    
        # Send request to API 
        response = requests.get(url=url)
    
        # Extract JSON data from response 
        response_data = response.json()
        
        # Check if there's been an error
        if "Time Series (Daily)" not in response_data.keys():
            raise Exception(
                f"Invalid API call. Check if that ticker {ticker} is correct"
            )
        
        # Read data into DataFrame 
        stock_data = response_data["Time Series (Daily)"]
        df = pd.DataFrame.from_dict(stock_data, orient="index", dtype=float)
    
        # Convert index to `DatetimeIndex` named "date" 
        df.index = pd.to_datetime(df.index)
        df.index.name = "date"
    
        # Remove numbering from columns 
        df.columns = [c.split(". ")[1] for c in df.columns]
    
        # Return DataFrame
        return df
    

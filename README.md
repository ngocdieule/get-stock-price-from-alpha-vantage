# get-stock-price-from-alpha-vantage
I created a module with a get_daily function that automates the retrieval of daily stock price data from the Alpha Vantage API.

## Setup

1. Clone the repository (or download the files).

2. Create a `.env` file in the project root directory. Add your Alpha Vantage API key inside:

```env
# Store API Keys from Alpha Vantage
ALPHA_API_KEY="INSERT_YOUR_REAL_API_KEY_HERE"
```

3. Install dependencies:
Required packages include:
- pandas
- requests
- pydantic
- pydantic-settings

## Module Overview

The project includes a module `data.py` with the function:

`get_daily(ticker, output_size="full")`:
Retrieves daily stock prices (open, high, low, close, volume) for the given ticker from Alpha Vantage.

## Sample Usage

Open the `etf_prices.ipynb` notebook.

Run the notebook cells step by step. The workflow will:
- Load your API key from `.env`
- Fetch daily close prices for ETFs (SPY, VEA, EEM, IWM, VNQ, IEF, LQD)
- Merge them into a single DataFrame
- Filter the date range (e.g., 2013-01-01 to 2024-08-01)

Example usage from the module:

```python
from data import AlphaVantageAPI

av = AlphaVantageAPI()
spy = av.get_daily(ticker="SPY")
print(spy.head())
```

Example output:

```
             open    high     low   close     volume
date                                              
2025-09-02  637.50  640.49  634.92  640.27  81983545.0
2025-08-29  647.47  647.84  643.14  645.05  74522192.0
...
```

## Notes

- The free Alpha Vantage API allows up to 25 requests per day
- Save downloaded data locally (e.g., to `.csv`) to avoid hitting daily limits
- Use `"compact"` mode if you only need the latest 100 days (faster and lighter)

# conditional install yfinance
def install_yfinance():
  try:
    import yfinance as yf
  except ModuleNotFoundError:
    import os
    os.system('pip install yfinance --upgrade --no-cache-dir')

    import yfinance as yf

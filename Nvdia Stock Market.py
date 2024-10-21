import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sea

''' Replace 'nvidia_stock_price.csv' with the actual file name or path '''

df = pd.read_csv('nvidia_stock_price.csv')

''' Calculate the Averaage movement'''
df['A_100'] = df['Close'].rolling(window=50).mean()
df['A_365'] = df['Close'].rolling(window=50).mean()



plt.figure(figsize=(15, 10))

plt.title('Nvidia Stock Price with EMA, SMA 50')
plt.xlabel('Date')
plt.ylabel('Price')

# Show the legend
plt.legend()
from coinmarketcap_ranking.config import API_KEY
from coinmarketcap import Market




print ("hello world!")
print(API_KEY)


print("----------------retrieve data from API--------------------")
coinmarketcap = Market()
coinmarketcap.listings()


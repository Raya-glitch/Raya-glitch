import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv("weather.csv")

data.plot(type=True, x = "Season")
fig, ax = plot.subplots(7, 1, figsize=(5, 25))


ax[0].barh(data["Temperature"], data["Weather Type"] )
ax[0].set_xlabel("Temparature")
ax[0].set_ylabel("Season")
ax[0].set_title("Correlation of Temparature to Season")
plot.savefig("weather.png")

df = pd.read_csv('weather.csv')
print(df) 













































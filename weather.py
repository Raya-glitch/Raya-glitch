import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv("weather.csv")

data.plot(subplots=True, x = "Season")

plot.savefig("weather.png")

temperature = data['Temperature']

fig, ax = plot.subplots(7, 1, figsize=(6, 10))

ax[0].plot(data, temperature, color='tab:red')

df = pd.read_csv('weather.csv')
print(df) 













































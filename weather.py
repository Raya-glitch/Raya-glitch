import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv("weather.csv")
data.plot(kind="bar", y = "Location", x = "Weather Type")
plot.savefig("weather.png")


















































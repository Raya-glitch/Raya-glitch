import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv("weather.csv")

print(data.dtypes)

# Create subplots for each of the 7 charts
fig, ax = plot.subplots(6, 1, figsize=(6, 25))

# First Chart: Scatter plot between Cloud Cover and Precipitation
ax[0].scatter(data["Cloud Cover"], data["Precipitation (%)"], marker="*", color="r")
ax[0].set_xlabel("Cloud Cover", size="13")
ax[0].set_ylabel("Precipitation", size="13")
ax[0].set_title("Correlation of Cloud Cover to Precipitation", size="16")

# Second Chart: Boxplot for Humidity by Location
if data["Location"].dtype == 'object':  # Check if Location is string or categorical
    data["Location"] = data["Location"].astype('category')

ax[1].boxplot([data["Humidity"][data["Location"] == loc] for loc in data["Location"].cat.categories])
ax[1].set_xticklabels(data["Location"].cat.categories, rotation=45)
ax[1].set_xlabel("Location", size="13")
ax[1].set_ylabel("Humidity", size="13")
ax[1].set_title("Correlation of Location to Humidity", size="16")

# Third Chart
ax[2].plot(data.groupby("Season")["Temperature"].mean(), marker='o', linestyle="dashdot", color="r")
ax[2].set_xlabel("Season", size="13")
ax[2].set_ylabel("Average Temperature", size="13")
ax[2].set_title("Average Temperature by Season", size="16")

# Fourth Chart
ax[3].hist(data["Precipitation (%)"], color="r")
ax[3].set_xlabel("Precipitation", size="13")
ax[3].set_title("Correlation of Precipitation", size="16")

#Fifth Chart
ax[4].hist(data["Visibility (km)"], color="r")
ax[4].set_xlabel("Visibility", size="13")
ax[4].set_title("How is Visibility affected?", size="16")

ax[5].hist(data["UV Index"], color="r")
ax[5].set_xlabel("UV Index Numbers", size="13")
ax[5].set_title("How is Weather affected by UV rays?", size="16")

print(data)

# Adjust layout to prevent overlap
plot.tight_layout()

# Save the figure as a PNG file
plot.savefig("weather.png")

# Print the data to inspect
print(data)













































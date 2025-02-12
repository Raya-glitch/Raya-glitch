import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv("weather.csv")

print(data.dtypes)

# Create subplots for each of the 7 charts
fig, ax = plot.subplots(7, 1, figsize=(6, 25))

# First Chart: Scatter plot between Cloud Cover and Precipitation
ax[0].scatter(data["Cloud Cover"], data["Precipitation (%)"])
ax[0].set_xlabel("Cloud Cover")
ax[0].set_ylabel("Precipitation (%)")
ax[0].set_title("Correlation of Cloud Cover to Precipitation")

# Second Chart: Boxplot for Humidity by Location
if data["Location"].dtype == 'object':  # Check if Location is string or categorical
    data["Location"] = data["Location"].astype('category')

ax[1].boxplot([data["Humidity"][data["Location"] == loc] for loc in data["Location"].cat.categories])
ax[1].set_xticklabels(data["Location"].cat.categories, rotation=45)
ax[1].set_xlabel("Location")
ax[1].set_ylabel("Humidity")
ax[1].set_title("Correlation of Location to Humidity")

ax[2].plot(data.groupby("Season")["Temperature"].mean(), marker='o')
ax[2].set_xlabel("Season")
ax[2].set_ylabel("Average Temperature")
ax[2].set_title("Average Temperature by Season")


# Adjust layout to prevent overlap
plot.tight_layout()

# Save the figure as a PNG file
plot.savefig("weather.png")

# Print the data to inspect
print(data)













































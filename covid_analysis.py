import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("day_wise.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Check data
print(df.tail())

# Plot COVID trends
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Confirmed"], label="Confirmed")
plt.plot(df["Date"], df["Deaths"], label="Deaths")
plt.plot(df["Date"], df["Recovered"], label="Recovered")

plt.title("COVID-19 Global Trends")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()
plt.show()

df["New_Confirmed"] = df["Confirmed"].diff()
df["New_Deaths"] = df["Deaths"].diff()
df["New_Recovered"] = df["Recovered"].diff()

df["Confirmed_7day_avg"] = df["New_Confirmed"].rolling(7).mean()

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["New_Confirmed"], alpha=0.4, label="Daily Cases")
plt.plot(df["Date"], df["Confirmed_7day_avg"], linewidth=2, label="7-Day Average")
plt.legend()
plt.show()

peak_day = df.loc[df["New_Confirmed"].idxmax()]
print("Highest spike on:", peak_day["Date"])

df["Death_Rate"] = (df["Deaths"] / df["Confirmed"]) * 100
df["Recovery_Rate"] = (df["Recovered"] / df["Confirmed"]) * 100

plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig("covid_trends.png")
df.to_csv("processed_covid_data.csv", index=False)

# Check missing values
print(df.isnull().sum())

# Fill or drop missing values
df = df.fillna(0)

import seaborn as sns

corr = df[["Confirmed", "Deaths", "Recovered"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of COVID-19 Cases")
plt.show()

import seaborn as sns

corr = df[["Confirmed", "Deaths", "Recovered"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of COVID-19 Cases")
plt.show()

# Basic data inspection
print(df.info())
print(df.isnull().sum())

# Handle missing values
df = df.fillna(0)

# Remove duplicates if any
df = df.drop_duplicates()

df["New_Confirmed"] = df["Confirmed"].diff()
df["New_Deaths"] = df["Deaths"].diff()
df["New_Recovered"] = df["Recovered"].diff()

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["New_Confirmed"], label="Daily Confirmed")
plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()
plt.show()

df["Confirmed_7day_avg"] = df["New_Confirmed"].rolling(7).mean()

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["New_Confirmed"], alpha=0.4, label="Daily Cases")
plt.plot(df["Date"], df["Confirmed_7day_avg"], linewidth=2, label="7-Day Avg")
plt.legend()
plt.show()

import seaborn as sns

corr = df[["Confirmed", "Deaths", "Recovered"]].corr()

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("COVID-19 Case Correlation Heatmap")
plt.show()

plt.savefig("covid_trends.png")
df.to_csv("cleaned_covid_data.csv", index=False)


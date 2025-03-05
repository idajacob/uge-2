#opgave4uge2

import csv
import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


#gruppering af data

df = pd.read_csv("DKHousingPricesSample100k(in).csv")

print(df.head(10))

df_grouped = df.groupby("region")["purchase_price"].mean()

print(df_grouped)
df_grouped.to_csv("region_avg_prices.csv", index=True)

df_grouped_advanced = df.groupby(["house_type", "region"])["purchase_price"].mean()

print(df_grouped_advanced)
df_grouped_advanced.to_csv("house_type_region_avg_prices.csv", index=True)


#plot af data i linjediagram

df_grouped_advanced = df.groupby(["house_type", "region"])["purchase_price"].mean().reset_index()

pivot_df = df_grouped_advanced.pivot(index="region", columns="house_type", values="purchase_price")

pivot_df.plot(kind="line", marker="o", figsize=(15, 10))

plt.title("Gennemsnitlig købspris per hustype og region")
plt.xlabel("Region")
plt.ylabel("Gennemsnitspris")
plt.xticks(rotation=45)
plt.legend(title="Hustype")

plt.show()


#plot af data i søjlediagram

df_grouped_advanced = df.groupby(["house_type", "region"])["purchase_price"].mean().reset_index()

pivot_df = df_grouped_advanced.pivot(index="region", columns="house_type", values="purchase_price")

pivot_df.plot(kind="bar", figsize=(15, 10))

plt.title("Gennemsnitlig købspris per hustype og region")
plt.xlabel("Region")
plt.ylabel("Gennemsnitspris")
plt.xticks(rotation=45)
plt.legend(title="Hustype")

plt.show()







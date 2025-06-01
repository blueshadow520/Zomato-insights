import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (20, 12)
plt.rcParams["figure.autolayout"] = True

# Load data
df = pd.read_csv('zomato.csv', encoding='ISO-8859-1')  # Try ISO-8859-1 if latin-1 fails
print(df.shape)
print(df.head())

print(df.columns)

print(df.info())

print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Columns with missing values
print([features for features in df.columns if df[features].isnull().sum() > 0])

# Plot missing values
plt.bar(df.columns, df.isnull().sum())
plt.xlabel("Columns")
plt.ylabel("Null Count")
plt.xticks(rotation=45)
plt.show()

# Load country codes
df_country = pd.read_excel('Country-Code.xlsx')
print(df_country.head())

# Merge with country codes
final_df = pd.merge(df, df_country, on="Country Code", how="left")
print(final_df.head())

# Check for missing values after merge
print([f for f in final_df.columns if final_df[f].isnull().sum() > 0])

# Checking data type of country code
print(df['Country Code'].dtype)

# Final columns in the dataframe
print(final_df.columns)

# Country value counts
print(final_df.Country.value_counts())

# Correlation of numerical columns
final_df_numec = final_df.select_dtypes(exclude='object')
print(final_df_numec.corr())

# Plotting top three countries by ratings
Country_name = final_df.Country.value_counts().index
Country_val = final_df.Country.value_counts().values
plt.pie(Country_val[:3], labels=Country_name[:3], autopct='%.2f%%')
plt.show()

# Group ratings by aggregate rating, rating color, and text
ratings = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0: 'Rating count'})
print(ratings.head())

# Bar plot for aggregate ratings
plt.bar(ratings['Aggregate rating'], ratings['Rating count'], width=0.07, color='blue')
plt.xlabel("Aggregate rating")
plt.ylabel("Rating count")
plt.show()

# Rating color counts
rating_color_count = final_df.groupby(['Rating color']).size().reset_index().rename(columns={0: "Count"})
print(rating_color_count)

# Bar plot for rating colors
colors = ['darkgreen', 'green', 'orange', 'red', 'white', 'yellow']
plt.bar(rating_color_count['Rating color'], rating_color_count['Count'], color=colors, edgecolor='black')
plt.show()

# Histogram of rating colors
plt.hist(final_df['Rating color'], color='blue')
plt.show()

# Country with zero ratings
country_with_zero_rating_count = final_df[final_df['Rating color'] == 'White'].groupby(['Country']).size().reset_index().rename(columns={0: 'Country count'})
print(country_with_zero_rating_count)

plt.bar(country_with_zero_rating_count['Country'], country_with_zero_rating_count['Country count'], color='red')
plt.xlabel("Countries")
plt.ylabel("Count")
plt.show()

# Currency of each country
currency_of_countries = final_df.groupby(['Country', 'Currency']).size().reset_index()
print(currency_of_countries.columns)

currency_of_countries = currency_of_countries.drop(0, axis=1)
print(currency_of_countries)

# Countries with online delivery options
online_delivery_countries = final_df.groupby(['Country', 'Has Online delivery']).size().reset_index()
print(online_delivery_countries)

# Filter for countries with online delivery
availiblity_online_delivery_option = online_delivery_countries[online_delivery_countries['Has Online delivery'] == 'Yes'].reset_index(drop=True)
print(availiblity_online_delivery_option)

print(final_df[final_df['Has Online delivery'] == 'Yes'].Country.value_counts())

# Pie chart for cities
cities_name = final_df.City.value_counts().index
cities_val = final_df.City.value_counts().values
plt.pie(cities_val[:5], labels=cities_name[:5], autopct='%.2f%%')
plt.show()

# Top 10 cuisines
cuisines_count = final_df.groupby(['Cuisines']).size().reset_index().rename(columns={0: 'Cuisines count'})
cuisines_count = cuisines_count.sort_values(by='Cuisines count', ascending=False).reset_index(drop=True)
print(cuisines_count.head(10))

plt.bar(cuisines_count['Cuisines'][:10], cuisines_count['Cuisines count'][:10], color='blue')
plt.xticks(rotation=45)
plt.show()

# Data for India
india_df = final_df[final_df['Country'] == 'India']
print(india_df)
# # Histogram for average cost for two in India
# plt.hist(india_df['Average Cost for two'], bins=10, color='green')
# plt.show()
# Histogram for average cost for two in India
plt.hist(india_df['Average Cost for two'], bins=10, color='green')
plt.show()

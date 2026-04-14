#!/usr/bin/env python
# coding: utf-8

# # importing the neccessary libraries

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # Reading the data from the csv file 

# In[4]:


df=pd.read_csv("C:/Users/44755/Desktop/stock market/stock_market_2016_2024_weekdays.csv")


# # First 5 rows of the dataframe

# In[5]:


df.head(5)


# # columns of the dataframe

# In[6]:


df.columns


# # Summarie of the numerical columns

# In[7]:


df.describe()


# # Data type of each column

# In[8]:


df.dtypes


# # Converting data type of "Date" column from object to datetime

# In[9]:


df['Date'] = pd.to_datetime(df['Date'],errors='ignore')


# In[10]:


df.dtypes


# # Extracting and creating an "year" , "month" and "day" columns

# In[11]:


df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['Day_Name'] = df['Date'].dt.day_name()


# In[12]:


df.head(5)


# In[13]:


df.Year.unique()


# # Average closing over the years

# In[14]:


dt=df.groupby("Year")["Close"].mean().reset_index(name='Avrg_closing')


# In[15]:


dt


# # Lineplot for average closing over the years

# In[16]:


plt.plot(dt["Year"],dt["Avrg_closing"])
plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Average  Value Per Share")
plt.show()


# # Rolling average close for 200 days

# In[17]:


df['MA_200'] = df['Close'].rolling(window=200).mean()


# In[18]:


df.head(50)


# # Bargraph for rolling average close for 200 days

# In[19]:


plt.bar(df["Date"], df["MA_200"])
plt.show()


# In[20]:


# daily return
df["daily_return"] = df["Close"].pct_change()



# annual volatility
annual_volatility = df["daily_return"].std() * np.sqrt(252)

print("Annual Volatility:", annual_volatility)


# In[21]:


df


# # Lineplot for  returns over the years

# In[22]:


df.groupby('Year')['daily_return'].mean().plot()
plt.xlabel("Year")
plt.ylabel("% change in Value")
plt.title("returns over the years")
plt.show()


# # Average number of shares traded over the years

# In[23]:


yearly_avg_volume = df.groupby("Year")["Volume"].mean().reset_index(name='total volume')

print(round(yearly_avg_volume,2))


# # Lineplot for the number of shares traded over the years

# In[24]:


plt.plot(yearly_avg_volume["Year"],yearly_avg_volume["total volume"])
plt.xlabel("Year")
plt.ylabel("Volume")
plt.title("Average no of shares traded over the years")
plt.show()


# In[25]:


df["Volume_MA20"] = df["Volume"].rolling(window=20).mean()


# In[26]:


df


# # lineplot for traded shares over time

# In[27]:


plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Volume"])
plt.title("Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()


# # bargraph for average daily return over the years

# In[28]:


df.groupby('Year')['daily_return'].mean().plot(kind='bar')
plt.show()


# # bargraph for average daily return over the months

# In[29]:


df.groupby('Month')['daily_return'].mean().plot(kind='bar')
plt.show()


# # bargraph for average daily return over the weekdays

# In[30]:


df.groupby('Day_Name')['daily_return'].mean().plot(kind='bar')
plt.title('Average daily returns on the days')
plt.ylabel('Value')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





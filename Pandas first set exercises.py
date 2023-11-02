#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Open the video game sales using pandas. 
#Check characteristics of the dataset. 
#What is the shape of the dataset, what are the statistics of the columns, are there any NaNs?

import pandas as pd
import numpy as np


# Load a csv file
df=pd.read_csv("vgsales.csv")


# In[2]:


df.info()


# In[3]:


df.shape


# In[4]:


df.describe()


# In[5]:


# Check for NaN values 
df.isna().sum()


# In[6]:


# Check for NaN values in a specific column (e.g., 'column_name')
df['Year'].isna().sum()


# In[7]:


df['Publisher'].isna().sum()


# In[8]:


#Clean the dataset (if you find any NaNs)
new_df=df.dropna()
new_df


# In[9]:


#Which game has the highest global sales? What is its platform?
new_df.sort_values("Global_Sales",ascending=False)
highest_sales_game=new_df["Name"][0]
game_platform=new_df['Platform'][0]
print(highest_sales_game)
print(game_platform)


# In[10]:


#Which are the platforms in the dataset?
df["Platform"].unique()


# In[11]:


#Replace where XOne with ‘X Box One’
df.replace('XOne','X Box One')


# In[12]:


#(a)Which are the top ten selling games for PS4 (Global sales)?
#(b)Is this the same for Europe and Japan sales combined?


#(a)
ps4_games = new_df[new_df["Platform"] == "PS4"]
top_10_ps4_games = ps4_games.sort_values(by="Global_Sales", ascending=False).head(10)

print(top_10_ps4_games[["Name", 'Platform', "Year", "Global_Sales"]])


# In[13]:


#(b)


# In[14]:


#How many games were released for XOne in 2016? Which was the top selling game in Europe?
games_2016=new_df[new_df["Year"]==2016.0]
Xone_games_2016=games_2016[new_df["Platform"]=="XOne"]
Xone_games_2016


# In[15]:


Xone_games_2016=new_df[new_df["Year"]==2016.0][new_df["Platform"]=="XOne"]
Xone_games_2016


# In[ ]:





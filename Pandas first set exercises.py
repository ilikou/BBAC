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
Xone_games_2016=games_2016[games_2016["Platform"]=="XOne"]
Xone_games_2016


# In[15]:


#second solution
Xone_games_2016=new_df[(new_df["Year"]==2016.0) & (new_df["Platform"]=="XOne")]
Xone_games_2016


# In[16]:


#In which year the most games were released?
year_most_games=df.groupby("Year").count().sort_values("Name",ascending=False).head(1).index[0]
print("Year the most games were released is :",year_most_games)


# In[17]:



#Which platform had the most releases that year?
games_in_most_releases_year = df[df['Year'] == year_most_games]
platform_counts = games_in_most_releases_year['Platform'].value_counts()
most_releases_platform = platform_counts.idxmax()
most_releases_count = platform_counts.max()
print(f"Platform had the most releases is {most_releases_platform} with {most_releases_count}" )


# In[18]:


#Which are the top 5 selling platforms (games global sales) of all time? Plot your results in a graph
top5_selling_platform=new_df.groupby("Platform").sum().sort_values("Global_Sales",ascending=False).head(5)
top5_selling_platform


# In[19]:


top5_selling_platform["Global_Sales"].plot(kind="bar")


# In[20]:


#Which are the top three publishers in EU game sales? 
#Use a pie plot to show their contribution. 
#How is it compared with their global sales? Use plots to show your results.


#Which are the top three publishers in EU game sales?
top3_selling_EUpublishers=new_df.groupby("Publisher").sum().sort_values("EU_Sales",ascending=False).head(3)
top3_selling_EUpublishers
#print("The top three publishers in EU game sales is :",top3_selling_EUpublishers.index[:4])



# In[21]:


#Use a pie plot to show their contribution. 

top3_selling_EUpublishers["EU_Sales"].plot(kind="pie")


# In[22]:


#How is it compared with their global sales? Use plots to show your results.
top3_selling_Globalpublishers=new_df.groupby("Publisher").sum().sort_values("Global_Sales",ascending=False).head(3)
top3_selling_Globalpublishers

top3_selling_Globalpublishers["Global_Sales"].plot(kind="pie")


# In[23]:


compare_eu_vs_global=df("Publisher")(["EU_Sales","Global_Sales"].sum().sort_values("EU_Sales",ascending=False).head(3)
                                    


# In[24]:


#Use map and the following dictionary to replace the genres.
dic = {
1:'Sports',
2:'Platform',
3:'Racing',
4:'Role-Playing',
5:'Puzzle',
6:'Misc',
7:'Shooter',
8:'Simulation',
9:'Action',
10:'Fighting',
11:'Adventure',
12:'Strategy'}

def convert_gerne(x):
    return dic[x]
df['Genre'] = list(map(convert_gerne, df['Genre']))
df


# In[25]:


#Which action game has the highest global sales?
df[df['Genre'] == 'Action']


# In[26]:


df[df['Genre'] == 'Action'].sort_values('Global_Sales', ascending = False)


# In[27]:


#Which are the top 5 most mentioned genres of all time? Is this different in 2014, 2015, 2016?
top_genres = df.groupby('Genre').count().sort_values(['Name'], ascending = False)
top_genres.head()


# In[28]:


top_genres.head()['Name'].plot.bar(rot = 45)
None


# In[29]:


df_2014 = df[df['Year'] == 2014]
df_2014.head()


# In[30]:


top_genres_2014 = df_2014.groupby('Genre').count().sort_values(['Name'], ascending = False).head()
top_genres_2014


# In[31]:


df_2015 = df[df['Year'] == 2015]
df_2015.head()


# In[32]:


top_genres_2015 = df_2015.groupby('Genre').count().sort_values(['Name'], ascending = False).head()
top_genres_2015


# In[33]:


df_2016 = df[df['Year'] == 2016]
df_2016.head()


# In[34]:


top_genres_2016 = df_2016.groupby('Genre').count().sort_values(['Name'], ascending = False).head()
top_genres_2016


# In[35]:


top_genres_2016['Name'].plot.bar(rot = 45)
None


# In[ ]:





# In[ ]:





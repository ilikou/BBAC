#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import csv
import sys
import pymongo
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint
import json
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt


# In[2]:


client = MongoClient('mongodb://bigblue_user:3MmY2&PE@49.12.227.17:27017/?authSource=admin')


# In[3]:


#Connect to the learn database and use the business collection for the following tasks:
#db = client['learn']


# In[4]:


#collection = db['business']


# In[5]:


collection = client['learn']['business']


# In[6]:


#How many pizza places are open on Sundays exactly between 11:0-21:0?

collection.find({})


# In[7]:


cursor=collection.find({'hours.Sunday':'11:0-21:0'})
result=list(cursor)
result


# In[8]:


len(result)


# In[9]:


cursor = collection.find({'hours.Sunday':'11:0-21:0','categories': {'$regex': r"(?i)pizza"}})
final_result=list(cursor)


# In[10]:


len(final_result)


# In[11]:


#How many of those serve Ice Cream?
cursor = collection.find({'hours.Sunday':'11:0-21:0', 
                          "$and":
                          [{"categories": {'$regex': r"(?i)pizza"}},
                                                            {"categories":{'$regex': r"(?i)ice cream"}}]},)
final_result1=list(cursor)
final_result1


# In[12]:


len(final_result1)


# In[13]:


#Are steakhouses higher rated than Italian restaurants?


# In[14]:


cursor = collection.aggregate([
    {'$match': {'categories': {
        "$regex": r"^(?!.*(?i)steakhouses).*(?i)italian.*$"
    }}},
   { '$group': { '_id': 'null', 'average rating Italian': { '$avg': '$stars' }}}, 
    {
    "$project": {'_id': 0}
   }
])
result = list(cursor)
pprint(result)


# In[15]:


cursor = collection.aggregate([
    {'$match': {'categories': {
        "$regex": r"^(?!.*(?i)italian).*(?i)steakhouses.*$"
    }}},
   { '$group': { '_id': 'null', 'average rating Steakhouses': { '$avg': '$stars' }}}, 
    {
    "$project": {'_id': 0}
   }
])
result = list(cursor)
pprint(result)


# In[16]:


#alternative solution


# In[17]:


cursor = collection.find(
    {'categories': {"$regex": r"^(?=.*?(?i)italian)((?!(?i)steakhouses).)*$"}},
    {'_id': 0, 'stars':1}
  
)
result = list(cursor)
pprint(result[:1])


# In[18]:


df = pd.DataFrame(result)
df['stars'].mean()


# In[19]:


cursor = collection.find(
    {'categories': {"$regex": r"^(?=.*?(?i)steakhouses)((?!(?i)italian).)*$"}},
    {'_id': 0, 'stars':1}
  
)
result = list(cursor)
pprint(result[:1])


# In[20]:


df = pd.DataFrame(result)
df['stars'].mean()


# In[21]:


#4. Plot the average rating of the most expensive restaurants in each city.


# In[22]:


cursor = collection.distinct('attributes.RestaurantsPriceRange2')
result = list(cursor)
pprint(result)


# In[23]:


cursor = collection.aggregate([
    {'$match': {'attributes.RestaurantsPriceRange2': '4', 'categories': {
        "$regex": r"(?i)restaurants"
    }}},
   { '$group': { '_id': '$city', 'average rating': { '$avg': '$stars' }} },
    {
        '$sort': {'average rating': -1}
    }
])
result = list(cursor)
pprint(result)


# In[24]:


city = []
rating = []

for entry in result:
    city.append(entry['_id'])
    rating.append(entry['average rating'])


# In[25]:


plt.figure(figsize=[15, 10])
sns.set_theme()
chart = sns.barplot(x=city, y=rating)
chart.set_xticklabels(
    chart.get_xticklabels(), 
    rotation=45)
None


# In[ ]:





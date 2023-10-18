#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Which of the months has the hottest day and which has the coldest?
temperature = {
        'June': [25,25,26,27,25,25,24,27,28,28,31,32,33],
        'July': [34,34,36,39,39,38,39,37,39,41,41,39,37],
        'August': [37,37,36,37,35,35,34,37,38,34,32,33,31],
}

hottest = [0,0]

for key, value in temperature.items():
    if max(value) > hottest[1]:
        hottest[0] = key
        hottest[1] = max(value)

hottest


# In[27]:


coldest = ['start',0]

for key, value in temperature.items():
    if min(value) < coldest[1] or coldest[0] == 'start':
        coldest[0] = key
        coldest[1] = min(value)

coldest


# In[ ]:





# In[ ]:





# In[1]:


#From the two following lists: x = [2,4,5,6,7,1,6,8], y = [3,4,5,6,0,3,9] 
#create a new list with the non common elements using sets.
x = [2,4,5,6,7,1,6,8]
y = [3,4,5,6,0,3,9]
new_list=list(set(x)^set(y))
new_list


# In[2]:


#Make a list of the squares of the even numbers between 1 to 10.  Convert your code to a list comprehension afterwards.
sq=[x**2 for x in range(1,11) if x%2==0]
print(sq)


# In[22]:


#Make a list of cubes that are evenly divisible by four from a list of numbers between 1 and 12. 
#Convert your code to a list comprehension afterwards.
cube=[x**3 for x in range(1,13) if x**3%4==0]
print(cube)


# In[4]:


#Create a function that takes a list of numbers and returns a list with only the ones that are even.
def list(list1):
    even_list=[i for i in list1 if i%2==0]
    return even_list
list([1,2,3,4,5])


# In[5]:


#Multiply by 4 each element from a list and store it in another list. Use list comprehension. lst = [2,4,5,7,1,5,7,4,2,9,8,6]
lst = [2,4,5,7,1,5,7,4,2,9,8,6]
new_list=[x*4 for x in lst]
print(new_list)


# In[6]:


#Use list comprehension to filter numbers above 60 and append them to another list.
#lst = [66,53,23,67,77,86,88,34,78,99,100,45,93]
lst = [66,53,23,67,77,86,88,34,78,99,100,45,93]
new_list=[x for x in lst if x>60]
print(new_list)


# In[19]:


#d = {'milk': 1.65, 'coffee': 4.5, 'bread': 2.75, 'sugar': 0.55} 
#Create a new dictionary with converted values to CHF (swiss francs, rate 1 EUR = 1.18 CHF). Use dictionary comprehension.
d = {'milk': 1.65, 'coffee': 4.5, 'bread': 2.75, 'sugar': 0.55} 
def dCHF(d):
    for key,values in d.items():
        d[key]=d[key]*1.18
    return d


# In[20]:


result=dCHF(d)
print(result)


# In[ ]:



    


# In[ ]:





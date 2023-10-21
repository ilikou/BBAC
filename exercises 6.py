#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Use zip to iterate to all three lists and in a for loop and print each time the first name, 
#last name and age.
first_names = ['Jane', 'John', 'Jennifer']
last_names = ['Doe', 'Williams', 'Smith']
ages = [20, 40, 30]
zipped_list=list(zip(first_names,last_names,ages))
zipped_list
for first_names,last_names,ages in zipped_list  :
    print(f"The first name is: {first_names} , the Last name is {last_names}, age is {ages}" )
    


# In[2]:


#Calculate from the following lists the profit for each month. 
#Identify the month with the highest profits (use zip).
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

total_sales = [52000.00, 51000.00, 48000.00, 62000.0, 42000.0, 46000.0, 39000.0, 59000.0, 64000.0, 54000.0, 44000.0, 71000.0]

prod_cost = [46800.00, 45900.00, 43200.00, 45600.00, 37200.00, 42200.00, 48900.00, 33600.00, 54200.00, 33200.00, 42100.00]
profit=[x-y for x,y in zip(total_sales,prod_cost)]
month_profit=dict(zip(months,profit))
max_month=max(month_profit,key=lambda x:month_profit[x])
max_month
max_profit=max(profit)
max_profit    
print(f"The month with the highest profits is {max_month} and profit is {max_profit}" )


# In[3]:


#Use map function and lambda to make the email from the following list lowercase:
lst = ["Mary@GMAIL.com", "hari@YaHoo.com", "SopHIA@qg.com", "EVan@YahoO.COM"]
lowcase=list(map(lambda x:x.lower(),lst))
lowcase


# In[4]:


#Find the movie with the highest duration, use lambda function.
movies = {'pulp fiction': 154, 'terminator': 107, 'aliens': 137, 'the lion king': 98, 'pink panther': 115}
high_duration=max(movies,key=lambda x:movies[x])
high_duration


# In[5]:


#Write a program to filter out the even numbers from a list of integers using Lambda.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
neven_numbers=list(filter(lambda x : x%2!=0,lst))
neven_numbers


# In[6]:


#Filter out the even numbers from the following list and sort them using Lambda.
lst = [-4, 2, -3, 6, 3, 8, 11, -10]
neven_numbers=list(filter(lambda x : x%2!=0,lst))
neven_numbers.sort()
neven_numbers


# In[7]:


#Write a function to remove all elements from a given list present in another list using lambda 
#(and filter?).

def remove_elem(lst3,lst4):
    final=list(filter(lambda x:x not in lst4,lst3))
    return final
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [2, 4, 6, 8, 9]
final=remove_elem (lst1,lst2)
print(final)


# In[8]:


#Using the filter function and lambda, find the values that are common to the two lists below.

def comm_val(lst3,lst4):
    final=list(filter(lambda x: x in lst4,lst3))
    return final
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
final=comm_val(a,b)
print(final)


# In[9]:


#Use filter and lambda to return only negative numbers from a list.
lst = [2, -2, -3, 4, -5, 6, 7, -8, 9, -10]

negative_numbers=list(filter(lambda x:  x<0,lst))
print(negative_numbers)


# In[10]:


#Double the number of each element from the following list (use lambda)
lst = [6, 7, 23, 27, 24, 62, 87, 28, 23, 91]
double_number=list(map(lambda x: x*2,lst))
print(double_number)


# In[11]:


#Using sorted() function 
#and lambda sort the tuples in the list based on the last character of the second item.
# Cities population
lst = [(3090508, "Athens"), (9002488, "London"), (402762, "Zurich"), (198979, "Geneva"), (3769495, "Berlin"), (2165423, "Paris")]
lst=sorted(lst,key=lambda x: x[1][-1] )
lst


# In[12]:


#Write a Python program to find the maximum 
#and minimum values in the previous list of tuples using lambda function.
def minmax(lst):
    minimum=min(lst,key=lambda x : x[0])
    maximum=max(lst,key=lambda x : x[0])
    return minimum,maximum
lst = [(3090508, "Athens"), (9002488, "London"), (402762, "Zurich"), (198979, "Geneva"), (3769495, "Berlin"), (2165423, "Paris")]
minmax(lst)


# In[13]:


#Remove values that are not integer from a given list using lambda function
lst =  [4,67,8, None, 32, 'Missing', 21, 23.3]
interlist=list(filter(lambda x:isinstance(x,int),lst))
interlist


# In[14]:


#Write a Python program to sort a mixed list of integers and strings using lambda.
lst =  [4,67,8, 'not found', 32, 'missing', 21, 23, 'warning', 'alert']
interlist=list(filter(lambda x:isinstance(x,int),lst))
interlist.sort()
stringlist=list(filter(lambda x:isinstance(x,str),lst))
stringlist.sort()
print(f"The string list is {stringlist} and the inter list is {interlist}. " )


# In[15]:


#Write a Python program to calculate the average value of numbers in a list of lists using lambda.
#lst = [[33,4,33,22], [4,23,11,3], [1,22,75,11], [32,14,65,73], [3,2,6,8], [353,234,566,234,653]]
def average_list(lst):
    result=list(map(lambda x: sum(x)/len(x),lst))
    return result
lst = [[33,4,33,22], [4,23,11,3], [1,22,75,11], [32,14,65,73], [3,2,6,8], [353,234,566,234,653]]
average_list(lst)


# In[ ]:





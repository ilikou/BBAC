#!/usr/bin/env python
# coding: utf-8

# In[1]:


summ=5+225
summ


# In[2]:


inter=7//3
inter


# In[3]:


divid=7%3
divid


# In[4]:


print('-'*40)


# In[5]:


str1="John=is-a-great web developer\t    " 
str2=str1.replace('=',' ')
str3=str2.replace('-',' ')
str4=str3.replace('\t    ',' ')
str4


# In[6]:


first_name= input('Enter first name:')
last_name=input('Enter last name:')
age=input('Enter age:')
occupation=input('Enter occupation:')
print('New user '+first_name+last_name,' ,', age +' years old',',',occupation,',',' has been registered in the system')


# In[7]:


for i in range(1,101): 
    if i % 10 == 0: 
        print(i)    


# In[8]:


x = [3,5,23,6,7]
count=1
for i in x:
    count*=i
print(count)


# In[9]:


n = int(input('Enter integer:'))
summ = 0
for i in range(1, n + 1, 1):
    summ = summ + i
print(summ)


# In[10]:


x = [44,32,65,77,12,86]
x.sort()
x
print('the second largest number in the list is: ',x[-2])


# In[11]:


fruits = ['Apple', 'Grapes', 'Berry', 'Orange']
s='-'
s.join(fruits)


# In[12]:


x = [32,3,5,4,4,3,2,6,4,5,6,7,8]
x=list(dict.fromkeys(x))
print(x)


# In[13]:


lst = [1,2,[3,4],[5,[100,200,['Data Science']],23,11],1,7]
lst[3][1][2][0]


# In[14]:


x = [32,3,5,4,4,3,2,6,4,5,6,7,8]
newlist=list(set(x))
newlist


# In[15]:


x = [2,4,5,6,7,1,6,8]
y = [3,4,5,6,0,3,9]
set(x) ^ set(y)


# In[16]:


d = {'section':{'production':['wheel','tyre',{'engine':['pistons','valves','cylinder']}, 'door']}, 'development':'gearbox'}
print(d['section']['production'][2]['engine'][2])


# In[17]:


data = {'part 1':['a','b'], 'part 2':['c','d']}
import itertools      
for combo in itertools.product(*[data[k] for k in sorted(data.keys())]):
    print(''.join(combo))


# In[18]:


if 'holiday' in 'St. Moritz is a nice location to visit over Christmas holidays!':
    print('holiday in string')
else:
    print('holiday not in string')


# In[19]:


def string(paramm):
    return isinstance(paramm, str)
print(string("Hello, World!"))


# In[35]:


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print("First three letters of the alphabet:", alphabet[:3])
print("Three letters from the middle of the alphabet:", alphabet[4:7])
print("Letters from the middle to the end of the alphabet:", alphabet[5:])


# In[31]:


def replace_strings_with_zero(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], str):
            lst[i] = 0
x = [4, 67, 8, 'None', 32, 'Missing', 21]
replace_strings_with_zero(x)
print(x)


# In[34]:


electricitybill = {
    'January': 232,
    'February': 245,
    'March': 267,
    'April': 223,
    'May': 257,
    'June': 284,
    'July': 243,
    'August': 120,
    'September': 245,
    'October': 278,
    'November': 345,
    'December': 326,
}


totalcost = sum(electricitybill.values())
print(f"{totalcost}")

averagebill = totalcost / len(electricitybill)
print(f"{averagebill}")








# In[23]:


def convertnumbers(grades):
    lettergrades = []

    for i in grades:
        if i >= 90:
            lettergrades.append('A')
        elif i >= 80:
            lettergrades.append('B')
        elif i >= 70:
            lettergrades.append('C')
        elif i >= 60:
            lettergrades.append('D')
        else:
            lettergrades.append('F')

    return lettergrades
grades = [91, 64, 47, 82, 67, 96]
lettergrades = convertnumbers(grades)

print(lettergrades)
    


# In[24]:


temperature = {
        'June': [25,25,26,27,25,25,24,27,28,28,31,32,33],
        'July': [34,34,36,39,39,38,39,37,39,41,41,39,37],
        'August': [37,37,36,37,35,35,34,37,38,34,32,33,31],
}
hottestmonth = None
coldestmonth = None
maxtemperature = float('-inf')
mintemperature = float('inf')

for month, temperatures in temperature.items():
    maxtemp= max(temperatures)
    mintemp= min(temperatures)

    if maxtemp > maxtemperature:
        maxtemperature = maxtemp
        hottestmonth = month

    if mintemp < mintemperature:
        mintemperature = mintemp
        coldestmonth = month

print(f"{hottestmonth} {maxtemperature}")
print(f"{coldestmonth} {mintemperature}")


# In[25]:


evensquares = [x**2 for x in range(2, 11, 2)]

print(evensquares)


# In[26]:


def evennumbers(inputlist):
    even_numbers = [x for x in inputlist if x % 2 == 0]
    return evennumbers


# In[27]:


def elements(list):
    if not list:
        return None
    product=1
    for number in input_list:
        product *=number
    return product


# In[28]:


def uniqueelements(list):
    uniquelist = list(set(list))
    return uniquelist


# In[29]:


def average(numbers):
    if len(numbers) == 0:
        return None  
    total = sum(numbers)
    average = total / len(numbers)
    return average


# In[30]:


order_list = [
    'fries', 'burger', 'eggs', 'pasta', 'pizza', 'schnitzel', 'salad', 'water',
    'soda', 'wine', 'eggs', 'pasta', 'pizza', 'schnitzel', 'salad', 'water',
    'soda', 'wine', 'pizza', 'schnitzel', 'soda', 'wine', 'lemonade', 'steak',
    'pasta', 'salad', 'fries', 'burger', 'water', 'burger'
]


order_counts = {}
for i in order_list:
    if i in order_counts:
        order_counts[i] += 1
    else:
        order_counts[i] = 1
for order, count in order_counts.items():
    print(f"{order}: {count} times")


# In[ ]:





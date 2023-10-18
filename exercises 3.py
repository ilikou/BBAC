#!/usr/bin/env python
# coding: utf-8

# In[1]:


#askhsh 1 
x = ['the island', 'pie', 'alien', 'superman', 'once upon a time in America', 'the godfather']
sorted(x,key=len)
final=sorted(x,key=len)
print(final)


# In[2]:


#askhsh 2
inventory = {

    'gold' : 500,

    'pouch' : ['flint', 'twine', 'gemstone'],

    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']

}


inventory ['pocket']=['seashell', 'strange berry', 'lint']


# In[3]:


inventory ['backpack'].sort()
inventory


# In[4]:


inventory['backpack'].remove('dagger')
inventory


# In[5]:


inventory['gold'] = inventory['gold'] +50


# In[6]:


inventory


# In[7]:


#askhsh 3 
d = {'k1':[1,2,3,{'tricky':['life','man','machine',{'target':[1,2,3,'Artificial Intelligence']}]}]}
d['k1'][3]['tricky'][3]['target'][3]


# In[8]:


#askhsh 4 (a)
price={
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear':3,
    
    
    }

price2={'grapes':2.5,
        'mellons':3,
    
    
    
}


price.update(price2)
total_price=sum(price.values())
total_price


# In[9]:


#askhsh 4 (b)
stock = {

    "banana": 6,

    "apple": 0,

    "orange": 32,

    "pear": 15

}


prices = {

    "banana": 4,

    "apple": 2,

    "orange": 1.5,

    "pear": 3

}

total = 0
for key in stock:
    total += stock[key]*prices[key]
total
        


# In[10]:


#askhsh 5 (a)
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students= [lloyd,alice,tyler]
for student in students:
    print(student['name'])
    for key,value in student.items():
        if key!='name':
            avg=sum(value)/len(value)
            print (f'{key} average:{avg}' )
    print (40*'-')


# In[11]:


#askhsh 5 (b)
for student in students:
    print(student['name'])
    for key, value in student.items():
        if key != 'name':
            average = sum(value) / len(value)

            if average >= 90:
                grade = "A"
            elif 80 <= average < 90:
                grade = "B"
            elif 70 <= average < 80:
                grade = "C"
            elif 60 <= average < 70:
                grade = "D"
            else:
                grade = "F"

            print(key, grade)
    print (40*'-')


# In[ ]:





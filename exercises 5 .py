#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Change Alice’s grades to A,B,C,D,F for each grade in the list (hint: use enumerate!)
#A above 90 ,B between 80 and 90,C between 70 and 80,D between 60 and 70,Else is F
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
x = alice['homework']
x
[100.0, 92.0, 98.0, 100.0]
for i, element in enumerate(x):
    print(i, element)
def convert_grades(x):
    if x >= 90:
        grade = 'A'
    elif 80 <= x < 90:
        grade = 'B'
    elif 70 <= x < 80:
        grade = 'C'
    elif 60 <= x < 70:
        grade = 'D'
    else:
        grade = 'F'
    return grade
for index, element in enumerate(x):
    print(index, element, convert_grades(element))

# for i, element in enumerate(x):
#     x[i] = convert_grades(element)
# x
# now let's wrap this for the whole dictionary
for key in alice.keys():
    if key != 'name':
        for i, element in enumerate(alice[key]):
            alice[key][i] = convert_grades(element)

alice
{'name': 'Alice',
 'homework': ['A', 'A', 'A', 'A'],
 'quizzes': ['B', 'B', 'A'],
 'tests': ['B', 'A']}


# In[3]:


#Use map function to make the email from the following list lowercase:
#lst = ["Mary@GMAIL.com", "hari@YaHoo.com", "SopHIA@qg.com", "EVan@YahoO.COM"]

def lower_case(lst1):
    return lst1.lower()
lst = ["Mary@GMAIL.com", "hari@YaHoo.com", "SopHIA@qg.com", "EVan@YahoO.COM"]
lowlist=map(lower_case,lst)
list(lowlist)


# In[4]:


#Use map() to create a function which finds the length of each word in the phrase and 
#returns the values (len of each word) in a list. 
#(example sentence: Quantum computing will revolutionize the way we work.)

def lenth(x):
    lst=x.split()
    final_lenth=list(map(len,lst))
    return final_lenth
string='Quantum computing will revolutionize the way we work.'
lenth(string)


# In[5]:


#Use filter function to pass every student scored above 60 from the following list:
#scores = [['john', 45],['alice',67],['tyler',56],['nick',86]]
scores = [['john', 45],['alice',67],['tyler',56],['nick',86]]
def passes(x):
    return x[1]>60
final=list(filter(passes,scores))
print(final)


# In[6]:


#Use filter function to the following dictionary to filter out all users with lower times than 100:
#user_time = {'john':410, 'nadia': 700, 'tonny': 34, 'sylvia': 56, 'anna': 116}
user_time = {'john':410, 'nadia': 700, 'tonny': 34, 'sylvia': 56, 'anna': 116}
def lower(d):
    return d[1]>=100
finald=dict(filter(lower,user_time.items()))
print(finald)


# In[7]:


#Filter out the patients with not measured height:
#patient_height = {'john': 167, 'lizea': None, 'bob': 174, 'greg': None, 'hans': 193}
patient_height = {'john': 167, 'lizea': None, 'bob': 174, 'greg': None, 'hans': 193}
def patients(x):
    return x[1]!=None
finalpat=dict(filter(patients,patient_height.items()))
print(finalpat)


# In[8]:


#Filter out the keys containing the word error and 
#write the rest to a new dictionary using dictionary comprehension.
d = {'signal_x': 474, 
     'signal_x_error': 0.44,
     'signal_y': 321, 
     'signal_y_error' : 0.12, 
     'signal_z': 0.985,
     'signal_z_error': 0.032}
def flkey(x):
    return 'error' not in x[0]
final=dict(filter(flkey,d.items()))
print(final)


# In[ ]:





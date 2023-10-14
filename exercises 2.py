#!/usr/bin/env python
# coding: utf-8

# In[1]:


#askhsh 1
x=['Python', 'R', 'C', 'java']
for i in range(len(x)):
    print('A nice programming language is {}'.format(x[i]))


# In[2]:


#askhsh 2
multiple=[]
for i in range(1,11): 
    multiple.append(i*10)
print(multiple)
        


# In[3]:


#askhsh 3 (a)
score =list(range(1, 11))
print(score)
score[0],score[-1]
#askhsh 3 (b)
for score in range (1,11):
    if score is 1:
        print ('The judge gave the gymnast {} points'.format(score))
    else:
        print ('The judge gave the gymnast {} points'.format(score))


# In[4]:


#askhsh 4(a)
DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
x=DNA.count('A')
y=DNA.count('C')
z=DNA.count('G')
t=DNA.count('T')
print(' ',x,y,z,t)
#askhsh 4 (b)
RNA = DNA.replace('T', 'U')
print (RNA)


# In[5]:


#askhsh 5
x = [3,5,23,6,7]
count=1
for i in x:
    count*=i
print (count)


# In[6]:


#askhsh 6
n = int(input('Enter an integer n: '))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)


# In[7]:


#askhsh 7
x = [44,32,65,77,12,86]
x.sort()
second_largest=x[-2]
print(second_largest)


# In[8]:


#askhsh 8
x='koutrouilias@gmail.com'
username,domain=x.split('@')
print(domain)


# In[9]:


#askhsh 9
lst = [1,2,[3,4],[5,[100,200,['Data Science']],23,11],1,7]
word=lst[3][1][2][0]
print(word)


# In[10]:


#askhsh 10
x = [32,3,5,4,4,3,2,6,4,5,6,7,8]
unique=[]
for i in x:
    if i not in unique:
        unique.append(i)
print(unique)


# In[11]:


#askhsh 11
x = [2,4,5,6,7,1,6,8]
y = [3,4,5,6,0,3,9]
result=[]
for i in x:
    if i not in y:
        result.append(i)
for k in y:
    if k not in x:
        result.append(k)
            
print(result)


# In[12]:


#askhsh 12
list=[4,67,8, 'None', 32, 'Missing', 21]
for i in list:
    if isinstance(i,str):
        list.remove(i)
print (list)        


# In[ ]:





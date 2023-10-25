#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to check that a string contains only lowercase and uppercase characters.
import re
def only_letters(string):    
    patern=r'^[a-zA-Z]+$' 
    if re.match(patern,string):
        return True
    else:
        return False
string=input('Enter string :')
only_letters(string)


# In[2]:


#Write a Python program that matches a word at the beginning of a string.
import re
def match_word(string,word):
    patern=r'[a-zA-Z]' + word
    match=re.search(patern,string)
    return match is not None
string=input('Enter string:')
word=input('Enter word:')
match_word=(string,word)


# In[3]:


#Write a Python program that matches a word at the end of string
import re
def match_word(string,word):
    patern=word+r'[a-zA-Z]'
    match=re.search(patern,string)
    return match is not None
string=input('Enter string:')
word=input('Enter word:')
match_word=(string,word)


# In[8]:


#Write a Python program that matches a word containing 'z', 
#not at the start or end of the word. (Matches Brazil but not Zelda)
import re
string='Matches Brazil but not Zelda'
patern=re.compile(r'\w*z\w*')
result=patern.findall(string)
for i in result:
    print(i)


# In[9]:


#Write a Python program to match digits of length between 10 and 13
import re
def digit_numbers(string):
    patern=re.compile(r'\d{10,13}')
    return patern.findall(string)
string = "1234567890 12345678901 123456789012 1234567890123 123 1234 12345"    
result=digit_numbers(string)
result


# In[10]:


#Write a Python program so that the full email addresses are extracted. 
#(example: “For more information please write to the following 
#email address: admissions@footballclub.com, Mrs Stepanie Smith will be delighted to assist you.”)
import re
input_string='For more information please write to the following email address: admissions@footballclub.com, Mrs Stepanie Smith will be delighted to assist you.'
patern=re.compile(r'\w{2,}@\w{2,}.\w{2,}')
result=patern.findall(input_string)
result


# In[11]:


#E-mail Validation
#Write an email validating function, 
#returning True or False depending on whether an email address is correctly formatted 
#(e.g. john.smith@yahoo.com works, not  john.smith@yahoο, or  johnsmith@yahoo.com). 
#No input should lead to an exception.
#Extend your email validation in the first part to:  ". - _"  
#and at least four characters and in the second part: extensions with minimum two characters and maximum 4 characters
import re
def valid_email(email):
    patern=r'[a-zA-Z0-9_.-~+]{4,}@\w{2,}\.\w{2,4}' 
    if re.search(patern,email):
        return True
    else:
        return False

emails=['john.smith@yahoo.com','john.smith@yahoο','johnsmith@yahoo.com']
for email in emails:
    print(f"{email}: {valid_email(email)}")
        


# In[12]:


#Password Validation
#- Write a password validation function: the input should contain at least one lowercase letter, 
#at least one uppercase letter, at least one digit, and at least one symbol  from ``[$#/\@*]``. 
#Unmet criteria or any other character should lead to an exception.
def valid_password(password):
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[0-9]',password):
        return False
    if not re.search(r'[$#/\@*]',password):
        return False
    if re.search(r'[^a-zA-Z0-9$#/@*]', password):
        return False
    return True
        
test_list=['Aa2$','a2$','Aa','aA3#']
for password in test_list:
    print(f"{password}:{valid_password(password)}")        
        
        


# In[ ]:


#Unix Timestamps
#Print the difference between a given UNIX Timestamp and the current UNIX Timestamp as human-readable time.
#(Given timestamp: 1493560132)
timestamp=1493560132


# In[ ]:





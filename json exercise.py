#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Convert the following dictionary into JSON format:
#dic = {"meal" : "pizza", "drink" : "soda"}
import json

dic = {"meal" : "pizza", "drink" : "soda"}
json_data = json.dumps(dic)
print(json_data)


# In[ ]:


#Download the Beatles file.
#(a)Import it to your notebook and convert it to a Dictionary.
#(b)Create a function to print the names that have the role “singer”.
#(c)Add in each member the following key: {"years active": "1960–1970"}
#(d)Convert to JSON and save it

#(a)
import json
with open('beatles.json') as file:
    data = json.load(file)
print(data)



# In[ ]:


(b)
def get_names(dictionary):
    return [key for key in dictionary.keys() if "Singer" in dictionary[key]["role"]]
get_names(data)


# In[ ]:


#(c)
activity = {"years active": "1960–1970"}

for person in data.values():
    person.update(activity)
data


# In[ ]:


#(d)
#v2
#indent: tabs
data2 = json.dumps(data, indent = 3)
OUTPUT_FILE = "json_beatles_data.json"
with open(OUTPUT_FILE, "w") as output:
    output.write(data2)
    print(f"Success in creating/updating the file {OUTPUT_FILE}")


# In[ ]:





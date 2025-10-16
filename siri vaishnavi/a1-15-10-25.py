#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = 2  
with open("lab3.txt", "r") as file:
    lines = file.readlines()
    last = lines[-n:]  

for line in last:
    print(line, end="")


# In[3]:


lines_list = [] 

with open("lab3.txt", "r") as file:
    for line in file:
        lines_list.append(line.strip())  

print(lines_list)


# In[4]:


count = 0
with open("lab3.txt", "r") as file:
    for line in file:
        count = count+ 1

print("Number of lines:", count)


# In[6]:


min_length=10
with open("lab3.txt", 'r') as file:
    text = file.read()
    words = text.split()
    lengthy_words = []
    for word in words:
        if len(word)>=min_length:
             lengthy_words.append(word) 
print(lengthy_words)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


def read(filename, n):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            lastlines = lines[-n:]
            for line in lastlines:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "C:\college docs\cisco\ques.txt"
n = 5
read(filename,n)


# In[2]:


with open("C:\college docs\cisco\ques.txt","r") as file:
    list = [line.strip() for line in file]
print(list)


# In[3]:


filename = "C:\college docs\cisco\ques.txt"
try:
    with open(filename, "r") as file:
        line_count = sum(1 for line in file) # Read all lines and count them
    print(f"The file '{filename}' has {line_count} lines.")

except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
    


# In[4]:


filename = "C:\college docs\cisco\ques.txt"

try:
    with open(filename, "r") as file:
        words = []
        for line in file:
            words.extend(line.split())  # split by whitespace

    if words:
        # Find the 
        lengthy = max(words, key=len)
        print(f"The lengthy word in the file is: '{lengthy}'")
    else:
        print("The file is empty.")

except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
    


# In[ ]:





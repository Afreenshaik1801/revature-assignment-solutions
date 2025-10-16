#!/usr/bin/env python
# coding: utf-8

# In[10]:


def read_last_n_lines(filename="Documents/assignment.txt", n=2):
    with open(filename, "r") as file:
        lines = file.readlines()
        last_lines = lines[-n:]
        print(f"=== Last {n} Lines ===")
        for line in last_lines:
            print(line, end="")
        print()
read_last_n_lines()


# In[11]:


def create_list_from_file(filename="Documents/assignment.txt"):
    lines_list = []
    with open(filename, "r") as file:
        for line in file:
            lines_list.append(line.strip())
    print("\n=== Lines as List ===")
    print(lines_list)

create_list_from_file() 


# In[12]:


def count_lines_in_file(filename="Documents/assignment.txt"):
    count = 0
    with open(filename, "r") as file:
        for _ in file:
            count += 1
    print("\n=== Line Count ===")
    print("Number of lines:", count)

count_lines_in_file()


# In[17]:


def find_lengthy_words(filename="Documents/assignment.txt", min_length=10):
    lengthy_words = []
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        for word in words:
            if len(word) >= min_length:
                lengthy_words.append(word)
    print(f"\n=== Lengthy Words ({min_length}+ characters) ===")
    print(lengthy_words)

find_lengthy_words()


# In[ ]:





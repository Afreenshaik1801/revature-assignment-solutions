#!/usr/bin/env python
# coding: utf-8

# In[1]:


nums = [1,2,3,4]
prod = 1
for num in nums:
    prod *= num
print("Product of the ele",prod)


# In[2]:


for num in range(10,0,-1):
    print(num)


# In[3]:


nums = [3,9,1,6,2,8]
largest = nums[0] #assuming first to be the largest
for num in nums:
    if num>largest:
        largest = num
print("Largest number",largest)


# In[4]:


str = "Hello World"
for char in str:
    if char.isupper():
        print(char)


# In[9]:


num = [1,2,3,2]
occ = 2
index = 0
found = False

while index<len(num):
    if num[index] == occ:
        print(f"occ of {occ} is at {index}")
        found = True
        break
    index +=1
if not found:
    print(f"{occ} not found")


# In[11]:


num = [1,4,6,8,10,-3,5,7]
index = 0
while index<len(num) and num[index]>=0:
    print(num[index])
    index += 1


# In[16]:


for num in range(1,11):
    if num % 2 == 0:
        print(f"break loop, even number {num} found")
        break
    print(num)
else:
    print("no even number found")


# In[17]:


rows = 5
for i in range(rows, 0, -1):
    print("*" * i)


# In[28]:


# Base Class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}")

    def calculate_bonus(self):
        return 0.05 * self.salary  # Default 5% bonus


# Derived Class 1 → Developer
class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def calculate_bonus(self):
        return 0.10 * self.salary  # 10% bonus for Developer

    def show_projects(self):
        print(f"{self.name} is working on {self.programming_language}-based backend projects.")


# Derived Class 2 → Manager
class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size, department):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size
        self.department = department

    def calculate_bonus(self):
        return 0.15 * self.salary  # 15% bonus for Manager

    def assign_task(self):
        print(f"Manager {self.name} assigned tasks to {self.team_size} team members in {self.department}.")


# Derived Class 3 → Intern
class Intern(Employee):
    def __init__(self, emp_id, name, salary, duration):
        super().__init__(emp_id, name, salary)
        self.duration = duration

    def calculate_bonus(self):
        return 1000  # Fixed ₹1000 bonus

    def extend_internship(self, extra_months):
        self.duration += extra_months
        print(f"Internship extended. New duration: {self.duration} months.")


# Creating Objects and results

# Developer
dev = Developer(emp_id=101, name="Neha", salary=80000, programming_language="Python")
dev.display_info()
print(f"Bonus: ₹{dev.calculate_bonus()}")
print("-" * 40)

# Manager
mgr = Manager(emp_id=102, name="Raj", salary=120000, team_size=10, department="IT")
mgr.display_info()
print(f"Bonus: ₹{mgr.calculate_bonus()}")
print("-" * 40)

# Intern
intern = Intern(emp_id=103, name="Amit", salary=15000, duration=6)
intern.display_info()
print(f"Bonus: ₹{intern.calculate_bonus()}")
print("-" * 40)

dev.show_projects()
mgr.assign_task()
intern.extend_internship(2)


# In[31]:


rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*",end= " ")
        else:
            print(" ",end=" ")
    print()


# In[47]:


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


# In[46]:


with open("C:\college docs\cisco\ques.txt","r") as file:
    list = [line.strip() for line in file]
print(list)


# In[45]:


filename = "C:\college docs\cisco\ques.txt"
try:
    with open(filename, "r") as file:
        line_count = sum(1 for line in file) # Read all lines and count them
    print(f"The file '{filename}' has {line_count} lines.")

except FileNotFoundError:
    print(f"The file '{filename}' was not found.")


# In[52]:


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





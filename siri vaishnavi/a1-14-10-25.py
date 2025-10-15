#!/usr/bin/env python
# coding: utf-8

# In[7]:


s=[1,2,3,4,5]
p=1
for i in s:
    p=p*i
print(p)


# In[9]:


for i in range(10,0,-1):
    print(i)


# In[10]:


s=[3, 9, 1, 6, 2, 8]
Large=s[0]
for i in s:
    if i>Large:
        Large=i
print(Large)


# In[11]:


s="Hello World"
for s1 in s:
    if s1.isupper():
        print(s1)


# In[ ]:





# In[1]:


s=[1, 4, 6, 8, 10, -3, 5, 7]
i=0
while i<len(s) and s[i]>=0:
    print(s[i])
    i=i+1


# In[5]:


for num in range(1,7):
    if num%2==0:
        print("breaking")
        break
    print(num)
else:
    print("no even number found")


# In[8]:


for i in range(6,0,-1):
    print('*'*i)


# In[11]:


for i in range(5):
    for j in range(5):
      if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1:
        print("* ", end="")
      else:
        print("  ", end="")
    print()


# In[9]:


s = [2, 7, 3, 7, 9, 7]
s1 = 7
i = 0  

while i < len(s):
    if s[i] == s1:
        print("First occurrence", s1, "is at index", i)
        break
    i += 1


# In[18]:


class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.05
    
class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language
        

    def calculate_bonus(self):
        return self.salary * 0.10  

    def show_projects(self,project):
        self.project = project 
        print(f"{self.name} is working on {self.programming_language} based {self.project} projects")
        
class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size, department):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size
        self.department = department

    def calculate_bonus(self):
        return self.salary * 0.15  

    def assign_task(self):
        print(f"Manager {self.name} assigned tasks to {self.team_size} team members in {self.department}.")

class Intern(Employee):
    def __init__(self, emp_id, name, salary, duration):
        super().__init__(emp_id, name, salary)
        self.duration = duration  

    def calculate_bonus(self):
        return 1000  

    def extend_internship(self, extra_months):
        self.extra_months=extra_months
        self.duration = self.duration+extra_months
        print(f"Internship extended. New duration: {self.duration} months.")

dev = Developer(101, "Neha", 80000, "Python ")
mgr = Manager(102, "Raj", 120000, 10, "IT")
intern = Intern(103, "Amit", 15000, 6)

for emp in [dev, mgr, intern]:
    emp.display_info()
    print(f"Bonus: {emp.calculate_bonus()}")
    print("----------------------------------------")


dev.show_projects("backend")
mgr.assign_task()
intern.extend_internship(2)



    


# In[ ]:





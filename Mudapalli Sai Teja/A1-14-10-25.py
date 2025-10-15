#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Calculate the product of elements in a list using a for loop:
list=[1,2,3,4]
x=1
for i in list:
    x=x*i
print(x)
    


# In[5]:


#Print numbers in reverse from 10 to 1 using a for loop:
for i in range(10,0,-1):
    print(i)
    


# In[3]:


#3.Find the largest number in a list using a for looP [3, 9, 1, 6, 2, 8]
list=[3, 9, 1, 6, 2, 8]
num=list[0]
for i in list:
    if i>num:
        num=i
print(num)
        
    


# In[4]:


#4.Print all uppercase letters in a string using a for loop: "Hello World"
string="Hello World"
for i in string:
    if i.isupper():
        print(i)


# In[ ]:


#5.Find the first occurrence of a number in a list using a while loop:


# In[3]:


#6.Print numbers in a list until a negative number is encountered using a while loop: [1, 4, 6, 8, 10, -3, 5, 7]
list=[1, 4, 6, 8, 10, -3, 5, 7]
num=0
while list[num]>=0:
    print(list[num])
    num+=1
    


# In[35]:


#7.Print numbers from 1 to 10. If a number is even, break the loop using a for loop and else clause:
for i in range(1,11):
    if i%2==0:
        print("even num",i)
        break
    print(i)
else:
        print("loop finished")


# In[54]:


#8.Draw below patternEnter the row size for the pattern: 5
'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''
for i in range(5,0,-1):
    x="* " * i
    print(x)


# In[59]:


#9.draw below pattern
'''
Enter the row size for the pattern: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''
size=5
x="* "*size
y="* "+" "*(size)+" *"   
for i in range(size):
    if i == 0 or i == size - 1:
        print(x)
    else:
        print(y)


# In[1]:


# Base Class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}")
    def calculate_bonus(self):
        return self.salary * 0.05
# Derived Class 1
class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language
        self.projects = ["Python-based backend projects", "Database optimization"]
    def calculate_bonus(self):
        return self.salary * 0.10
    def show_projects(self):
        print(f"{self.name} is working on {self.programming_language}-based backend projects.")
# Derived Class 2
class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size, department):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size
        self.department = department
    def calculate_bonus(self):
        return self.salary * 0.15
    def assign_task(self):
        print(f"Manager {self.name} assigned tasks to {self.team_size} team members in {self.department}.")
# Derived Class 3
class Intern(Employee):
    def __init__(self, emp_id, name, salary, duration):
        super().__init__(emp_id, name, salary)
        self.duration = duration
    def calculate_bonus(self):
        return 1000
    def extend_internship(self, months_to_add=3):
        self.duration += months_to_add
        print(f"Internship extended. New duration: {self.duration} months.")
# 1. Create instances of the derived classes
dev1 = Developer(101, "Neha", 80000, "Python")
mgr1 = Manager(102, "Raj", 120000, 10, "IT")
int1 = Intern(103, "Amit", 15000, 5)
# 2. Demonstrate Polymorphism 
# Neha (Developer)
dev1.display_info()
print(f"Bonus: ₹{dev1.calculate_bonus():.1f}")
print("----------------------------------------")
# Raj (Manager)
mgr1.display_info()
print(f"Bonus: ₹{mgr1.calculate_bonus():.1f}")
print("----------------------------------------")
# Amit (Intern)
int1.display_info()
print(f"Bonus: ₹{int1.calculate_bonus():.1f}")
print("----------------------------------------")
# 3. Demonstrate unique methods 
dev1.show_projects()
mgr1.assign_task()
int1.extend_internship(3)


# In[ ]:





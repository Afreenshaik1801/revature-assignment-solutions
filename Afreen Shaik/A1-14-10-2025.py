#Product of elements
list=[1,2,3,4,5]
product=1
for i in list:
    product*=i
print(product)


#Reverse Order
for i in range(10,0,-1):
    print(i)



#largest number in a list
nums=[3,9,1,6,2,8]
largest=0
for num in nums:
    if num>largest:
        largest=num
print(largest)




#printing uppercase letters
n="Hello World"
for i in n:
    if i.isupper():
        print(i)




#first Occurance
n=[3,9,1,6,2,8,10]
i=0
while i<len(n):
    if n[i]>5:
        print(n[i])
        break
    i+=1



#Print until -ve Num
n=[1, 4, 6, 8, 10, -3, 5, 7]
index=0
while index<len(n) and n[index]>=0:
    print(n[index])
    index+=1


#if even then break
for i in range(1,11):
    if i%2==0:
        print(f"EVen num {i} found")
        break
else:
    print("No even num found")


#pattern (inverted Right angle triangle)
n=5
for i in range(n,0,-1):
    for j in range(i):
        print(f"*",end=" ")
    print()



#Hallow Pattern
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(f"*",end=" ")
        else:
            print(f" ",end=" ")
    print()



#Employee Management using Inheritence 
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def display_info(self):
        print(f"Employee ID: {self.emp_id},Name: {self.name},salary: ₹{self.salary}")
    def calculate_bonus(self):
        return self.salary * 0.05
        
class Developer(Employee):
    def __init__(self,emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language=programming_language
    def calculate_bonus(self):
        return self.salary * 0.10
    def show_projects(self):
        print(f"{self.name} is working on {self.programming_language}-based backend projects.")
        
class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size, department):
        super().__init__(emp_id, name, salary)
        self.team_size=team_size
        self.department=department
    def calculate_bonus(self):
        return self.salary * 0.15
    def assign_task(self):
        print(f"Manager {self.name} assigned tasks to {self.team_size} team members in {self.department}.")
        
class Intern(Employee):
    def __init__(self, emp_id, name, salary, duration):
        super().__init__(emp_id, name, salary)
        self.duration=duration
    def calculate_bonus(self):
        return 1000
    def extend_internship(self,months=1):
        self.duration+=months
        print(f"Internship Extended. New duartion: {self.duration} months.")


d=Developer(101,"Neha",80000,"Python")
d.display_info()
print(f"Bonus: ₹{d.calculate_bonus()}")
print("-"*53)
    
m=Manager(102,"Raj",120000,10,"IT")
m.display_info()
print(f"Bonus: ₹{m.calculate_bonus()}")
print("-"*53)

i=Intern(103,"Amit",15000,7)
i.display_info()
print(f"Bonus: ₹{i.calculate_bonus()}")
print("-"*53)

d.show_projects()
m.assign_task()
i.extend_internship()
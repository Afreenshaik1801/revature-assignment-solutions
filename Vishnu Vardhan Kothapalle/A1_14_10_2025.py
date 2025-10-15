

#Products of elements
ls = [1,2,3,4,5,6]
prod = 1
for i in ls:
    prod = prod*i
print(f"The product of all number in the list is {prod}")

# reverse from 10 to 1
for i in range(10,0,-1):
    print(i,end=" ")

#largest in list using for loop
ls=[3,9,1,6,2,8]
large = 0
for i in ls:
    if i > large:
        large = i
print(f"The largest number in the array is {large}")

#uppercase
word = "Hello World"

for i in word:
    if i.isupper():
        print(i, end=" ")

#first Occurance
numbers = [10, 25, 30, 25, 40, 25]
target = 25
i = 0
found = False
while i < len(numbers):
    if numbers[i] == target:
        print(f"First occurrence of {target} is at index {i}")
        found = True
        break
    i += 1
if not found:
    print(f"{target} not found in the list")

#negative number occurance
ls = [1,4,6,8,10,-3,5,7]
i = 0
while ls[i] > 0:
    print(ls[i],end = " ")
    i +=1


#break for even number
for num in range(1,10):
    print(num)
    if num % 2 == 0:
        print("Even Number found Breaking the Loop")
        break
else :
    print("No Even numbers Found")


#pattern 1
for i in range(5,0,-1):
    print("* "*i)


#pattern 2
for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



#oops concept
class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")

    def calculate_bonus(self):
        print(f"Bonus: {self.salary * 0.05}")

class Developer(Employee):
    def __init__(self, emp_id, name, salary,programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def calculate_bonus(self):
        print(f"Bonus: {self.salary * 0.10}")

    def show_projects(self):
        print(f"{self.name} is working on the {self.programming_language}")

class Manager(Employee):
    def __init__(self, emp_id, name, salary,team_size,department):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size
        self.department = department

    def calculate_bonus(self):
       print(f"Bonus: {self.salary * 0.15}")

    def assign_tast(self):
        print(f"Manager {self.name} assigned task to {self.team_size} team members in {self.department}")

class Intern(Employee):
    def __init__(self, emp_id, name, salary,duration):
        super().__init__(emp_id, name, salary)
        self.duration = duration

    def calculate_bonus(self):
        print("Bonus: 1000")

    def extend_internship(self):
        print(f"Internship Extended. Now duration: {self.duration}")


emp1 = Developer("101","Neha",80000,"python")
emp1.display_info()
emp1.calculate_bonus()

print("---------------------------------")

emp2 = Manager(102,"Raj",120000,10,"IT")
emp2.display_info()
emp2.calculate_bonus()

print("---------------------------------")

emp3 = Intern(103,"Amit",15000,8)
emp3.display_info()
emp3.calculate_bonus()

print("---------------------------------")

emp1.show_projects()
emp2.assign_tast()
emp3.extend_internship()
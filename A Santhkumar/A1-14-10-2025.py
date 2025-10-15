# Base Class a Employee
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: â‚¹{self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.05  # Default 5% bonus


# Derived Class Developer
class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def calculate_bonus(self):
        return self.salary * 0.10  # 10% bonus

    def show_projects(self):
        print(f"{self.name} is working on {self.programming_language}-based backend projects.")


# Derived Class 2 Manager
class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size, department):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size
        self.department = department

    def calculate_bonus(self):
        return self.salary * 0.15  # 15% bonus

    def assign_task(self):
        print(f"Manager {self.name} assigned tasks to {self.team_size} team members in {self.department}.")


# Derived Class 3 Intern
class Intern(Employee):
    def __init__(self, emp_id, name, salary, duration):
        super().__init__(emp_id, name, salary)
        self.duration = duration

    def calculate_bonus(self):
        return 1000  

    def extend_internship(self, months):
        self.duration += months
        print(f"Internship extended. New duration: {self.duration} months.")


# Creating objects for each type of employee
dev = Developer(101, "Neha", 80000, "Python")
mgr = Manager(102, "Raj", 120000, 10, "IT")
intern = Intern(103, "Amit", 15000, 6)

# Polymorphism: same method behaves differently for each class
employees = [dev, mgr, intern]

for emp in employees:
    emp.display_info()
    print("Bonus: " + str(emp.calculate_bonus()))
    print("----------------------------------------")

# Additional method calls
dev.show_projects()
mgr.assign_task()
intern.extend_internship(2)
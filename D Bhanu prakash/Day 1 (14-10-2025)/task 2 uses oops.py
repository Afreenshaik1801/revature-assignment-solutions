class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}")

    def calculate_bonus(self):
        return 0.05 * self.salary

class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def calculate_bonus(self):
        return 0.10 * self.salary  

    def show_projects(self):
        print(f"{self.name} is working on {self.programming_language}-based backend projects.")

class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size, department):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size
        self.department = department

    def calculate_bonus(self):
        return 0.15 * self.salary  

    def assign_task(self):
        print(f"Manager {self.name} assigned tasks to {self.team_size} team members in {self.department}.")

class Intern(Employee):
    def __init__(self, emp_id, name, salary, duration):
        super().__init__(emp_id, name, salary)
        self.duration = duration

    def calculate_bonus(self):
        return 1000 

    def extend_internship(self, extra_months):
        self.duration += extra_months
        print(f"Internship extended. New duration: {self.duration} months.")

dev = Developer(101, "Bhanu", 80000, "Python")
mgr = Manager(102, "prakash", 120000, 10, "IT")
intern = Intern(103, "bosi", 15000, 6)

employees = [dev, mgr, intern]

for emp in employees:
    emp.display_info()
    print(f"Bonus: ₹{emp.calculate_bonus()}")
    print("----------------------------------------")

dev.show_projects()
mgr.assign_task()
intern.extend_internship(2)
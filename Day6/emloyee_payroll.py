class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus

class Developer(Employee):
    def __init__(self, name, salary, project_bonus):
        super().__init__(name, salary)
        self.project_bonus = project_bonus

    def calculate_salary(self):
        return self.salary + self.project_bonus

# Example
m = Manager("Rajesh", 50000, 8000)
d = Developer("Deva", 40000, 6000)

for emp in (m, d):
    print(f"{emp.name}'s total salary: ₹{emp.calculate_salary()}")

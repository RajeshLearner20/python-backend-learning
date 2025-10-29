class Employee():

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name:{self.name} , Salary:{self.salary}")


class Developer(Employee):

    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language = programming_language

    def display(self):
        print(f"Name:{self.name}, Salary:{self.salary} , Programming_language:{self.programming_language}")


class manager(Developer):
    def __init__(self,name,salary,programming_language,team_size):
        super().__init__(name,salary,programming_language)
        self.team_size = team_size

    def details(self):
        print(f"Name:{self.name} , salary:{self.salary} ,programming_language:{self.programming_language}, team_size:{self.team_size}")


emp = manager("Rajesh",40000,"Python",7)
emp.details()
        
        

        
        
        
        

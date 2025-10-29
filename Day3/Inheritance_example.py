class person():

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name} , Age: {self.age}")


class Student(person):

    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade

    def display(self):
        print(f"Name: {self.name} , Age: {self.age} , Grade: {self.grade}")


student1 = Student("Rajesh",21,"A")

student1.display()




        

    

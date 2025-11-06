class student():

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() /len(self.marks)



s1 = student("Rajesh",[88,77,95,51,68])

print(f"Student Name:{s1.name} Total Marks:{s1.total()} Average:{s1.average():.2f}")          

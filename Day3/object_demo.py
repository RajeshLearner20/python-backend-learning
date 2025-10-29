class car():

    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"The {self.brand} {self.model} {self.year}")


car1 = car("Mahindra","Mahindra Thar",2010)
car2 = car("Tata" , "Tata Indica" ,1998)
car1.display()
car2.display()

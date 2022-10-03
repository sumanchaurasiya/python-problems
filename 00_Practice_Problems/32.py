# create a student database

class Student:
    type = "Student Database"
    def data(self):
        print(f"Name is {self.name}")
        print(f"Branch is {self.branch}")
        print(f"Year is {self.year}")

obj1 = Student()
print(obj1.type)
obj1.name = "Sia"
obj1.branch = "CSE"
obj1.year = "2045"    
obj1.data()
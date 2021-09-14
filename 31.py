# python program to craete an instance of a student havig id name and class and display it as dictionary

class Student:
    def __init__(self, s_id, s_name, s_class):
        self.s_id = s_id
        self.s_name = s_name
        self.s_class = s_class

suman = Student('S1','Suman','10')
print(suman.__dict__)

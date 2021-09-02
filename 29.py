# a class for storing the information of workers for a company 

class Programmer:
    company:"Microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product
   
    def getInfo(self):
        print(f"The name of the programmer is {self.name}, the product of the programmer is {self.product} ")

ram = Programmer("Ram", "skype")
sia = Programmer("Sia", "canva")
ram.getInfo()
sia.getInfo()

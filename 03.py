#swapping two number using third variable

a = int(input("Enter number to be swapped :"))
b = int(input("Enter another no to be swapped :"))

'''temp = a
a = b
b = temp'''
a,b = b,a    

print(f"Swapped number is : {a}" )
print(f"Swapped second no is :{b}")



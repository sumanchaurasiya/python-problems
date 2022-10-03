# python function to print even no in a list

list = [1, 3, 2, 7, 4, 8, 9, 0]

def evenNum(list):
    for i in list:
        if i%2==0:
            print(i, end =" ")
    
print(evenNum(list))
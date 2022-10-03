# max of three no

def max_No(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3
m=max_No(4,6,2)
print(m)
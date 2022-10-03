# write a function to reverse any string
def rev(s):
    str = " "
    for i in s:
        str = i+str
    return str

s = "sumanchaurasiya"
print("the original string is :" ,end = " ")
print(s)
print("the reversed string is : " , end =" ")
print(rev(s))


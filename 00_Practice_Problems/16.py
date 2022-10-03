# determine the type of triangle by taking sides as input
# if 3 sides ka different then scalene triangle
# if 2 sides are equal then isosceles triangle
# if all sides are equal then equilateral triangle

'''s1 = int(input("Enter first side :"))
s2 = int(input("Enter second side :"))
s3 = int(input("Enter third side: :"))

if(s1>=s2+s3 or s2>=s1+s3 or s3>=s1+s2):
    print("The triangle does not exist")
elif(s1==s2 and s1==s3 and s2==s3):
    print("Equilateral triangle")
elif(s1==s2 or s1==s3 or s2==s3):
    print("Isoscales triangle")
else:
    print("scalene triangle")'''

#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
'''Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.'''

heldc = int(input("Enter no of classes held :"))
atten = int(input("Enter attended classes : "))

per = (atten/heldc)*100
print("percentage of attendence : " + str(per))
if(per>=75):
    print("you are allowed to sit in the exam :" +str(per))
else:
    print("not allowed in exam")
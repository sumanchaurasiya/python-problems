# python prog to calcuate sum and average of n int numbers from the user.Input 0 to exit

sum = 0.0
count = 0
num = 1

while(num !=0):
    num = int(input("Enter some numbers : "))
    sum = sum+num
    count = count+1

if count == 0:
    print("Input some numbers:")
else:
    print("sum is : " +str(sum))
    print("average is : " + str(sum/(count-1)))



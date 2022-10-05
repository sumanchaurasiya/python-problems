print("Enter the Number:")
num = int(input())
sum = 0
for i in range(1, num):
  if num%i==0:
    sum = sum+i
if num==sum:
  print("It is a Perfect Number")
else:
  print("It is not a Perfect Number")
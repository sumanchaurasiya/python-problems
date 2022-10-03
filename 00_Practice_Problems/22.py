# python function to multiply all numbers in a list

list = [4, 5, 3, 6, 2, 1]
def multiplyList(list):
    result = 1
    for i in list:
        result = result * i
    return result

print(multiplyList(list))    
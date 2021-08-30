# write a python function that excepts a string input and calculate the no of lower case ad upper case letters

# def calc_Name(name):
#     myDict = {
#         "uppercase":0,
#         "lowercase":0
#     }
#     for i in name:
#         if i.isupper():
#             myDict["uppercase"]+=1
#         elif i.islower():
#             myDict["lowercase"]+=1
#         else:
#             pass

#     print("original string is :" , name)
#     print("no of uppercase letter :" , myDict["uppercase"])
#     print("no of lowercase letter : " , myDict["lowercase"])

# calc_Name("suman")

def calc_Name(name):
    uppercase = 0
    lowercase = 0
    for i in name:
        if i.isupper():
            uppercase+=1
        elif i.islower():
            lowercase+=1
        else:
            pass

    print("original string is :" , name)
    print("no of uppercase letter :" , uppercase)
    print("no of lowercase letter : " ,lowercase)

calc_Name("suman")
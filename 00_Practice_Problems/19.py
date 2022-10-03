# python prog to check validity of ka passwordValidation :

'''At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.'''

import re
pw = input("Enter your password : ")
x = True
while x:
    if(len(pw)<6 or len(pw)>16):
        break
    elif not re.search("[a-z]",pw):
        break
    elif not re.search("[A-Z]",pw):
        break
    elif not re.search("[0-9]",pw):
        break
    elif not re.search("[$#@]",pw):
        break
    elif re.search("\s",pw):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Not a Valid Password")


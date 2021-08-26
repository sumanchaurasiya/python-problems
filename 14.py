# create a student dictionary storing marks of 3 subjects also print the sum of all marks

'''marksDict = {
    "maths":65,
    "biology":80,
    "physics":75
}
print(sum(marksDict.values()))'''

# merge two dictionaries

myDict1 = {
    "a":60,
    "b":50
}
myDict2 = {
    "c":90,
    "d":30
}
myDict=myDict1.copy()
myDict.update(myDict2)
print(myDict)
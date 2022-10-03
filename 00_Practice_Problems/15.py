# print highest three values of corresponding keys in the dict
from heapq import nlargest
myDict = {
    "a":40,
    "b":55,
    "c":20,
    "d":90,
    "e":80
}

largest = nlargest(3,myDict, key=myDict.get)
print(largest)
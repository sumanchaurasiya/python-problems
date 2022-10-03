name = input("Enter your name: ")

# print(name.upper())
# print(name.lower())

# print(name[-1])

print(name[0].upper() + name[1:-1] + name[-1].upper())
a = round(len(name)/2)
print(name[a])
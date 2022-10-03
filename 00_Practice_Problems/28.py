# replace all the donkey word with ****

with open('sample.txt', 'r') as f:
    data = f.read()

data = data.replace("donkey", "****")

with open('sample.txt', 'w') as f:
    f.write(data)

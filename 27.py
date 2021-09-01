#multiplication table

for i in range(2, 25):
    with open(f'table.txt{i}', 'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j} \n")

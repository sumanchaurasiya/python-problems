import cmath
num = 6+4j

root = cmath.sqrt(num)
print('root of {0} is {1:0.3f}+{2:0.3f}j'.format(num,root.real,root.imag))
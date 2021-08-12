# Area of triangle using herons formula.
# formula = √s(s-a)(s-b)(s-c)
# s = (a+b+c)/2

side_a = float(input("Enter value of side a : "))
side_b = float(input("Enter value of side b : "))
side_c = float(input("Enter value of side c : "))

print("Perimeter is : " + str((side_a+ side_b+ side_c)/2))
s = (side_a+ side_b+ side_c)/2

print("Area of triangle is : " + str((s*(s-side_a)*(s-side_b)*(s-side_c))**0.5) )

def sphere(r) :
    v=4/3*3.14*r**3
    return v
def cone(r,h) :
    v=1/3*3.14*r**2*h
    return v
def cylinder(r,h) :
    v=3.14*r**2*h
    return v
x=int(input("Enter the radius : "))
y=int(input("Enter the height : "))
print("Volume of sphere is : ",sphere(x))
print("Volume of cone is : ",cone(x,y))
print("Volume of cylinder is : ",cylinder(x,y))
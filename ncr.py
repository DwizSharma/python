n=int(input("Enter the valve of n : "))
r=int(input("Enter the valve of r : "))
s=1
v=1
l=n-r
for n in range (n,0,-1):
    s=s*n
for r in range (r,0,-1):
    v=v*r
for l in range ((n-r),0,-1):
    l=l*(n-r)    
h=s/(v*l)
print(h)
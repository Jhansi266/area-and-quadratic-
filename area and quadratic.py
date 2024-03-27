#area of triangle
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area if triangle is:",area)






#quadratic equation
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
d=b**2-4*a*c
res1=(-b+d**0.5)/2*a
res2=(-b-d**0.5)/2*a
print(res1)
print(res2)

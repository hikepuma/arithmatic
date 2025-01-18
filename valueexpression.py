#program for calculating for value expression
#valueexpresiion
import math
a=float(input("Enter a value of A:"))
b=float(input("Enter a value of B:"))
res=(a+b)**2
res1=(a+b)*(a+b)
res2=a*a+2*a*b+b*b
res3=a**2+2**2*b+b**2
print("*"*50)
print("\t\tAll logic expression given below:")
print("*"*50)
print(f"\t\t1) (a+b)**2={res}")
print(f"\t\t2) (a+b)*(a+b)={res1}")
print(f"\t\t3) a*a+2*a*b+b*b={res2}")
print(f"\t\t3) a**2+2**2*b+b**2={res3}")
print("*"*50)



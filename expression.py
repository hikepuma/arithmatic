#program calculating of expression
#expression2
a=float(input("Enter value of A:"))
m=float(input("Enter value of m:"))
n=float(input("Enter value of n:"))
res=(a**m)/(a**n)
res1=a**(m-n)
print("*"*50)
print("\t\tFirst logic of value ({}**{})/({}**{})={}".format(a,m,a,n,res))
print("\t\tSecond logic of value {}**({}-{})={}".format(a,m,n,res))
print("*"*50)

#Program for Calculating simpleint and total amount o pay
#ArithmeticOpEx2.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#cal simple interest
si=(p*t*r)/100
totamt=p+si
#display the total result
print("-"*50)
print("\t\tSimple Interest Results")
print("-"*50)
print("\t\tPrinciple Amount:{}".format(p))
print("\t\tTime:{}".format(t))
print("\t\tRate of Interest:{}".format(r))
print("\t\tSimple Interest:{}".format(si))
print("\t\tTOTAL AMOUNT TO PAY:{}".format(totamt))
print("-"*50)
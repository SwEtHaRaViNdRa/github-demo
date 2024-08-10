import math
n=float(input("Enter a number for finding square root:"))
sqrtval=math.sqrt(n)
print("sqrt({})={}".format(n,sqrtval))
print("------or-------")
print("sqrt({})={}".format(n,round(sqrtval,2)))
print("------or------")
print("sqrt(%0.2f)=%0.2f"%(n,sqrtval))

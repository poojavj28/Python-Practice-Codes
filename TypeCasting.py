#If string holding integer then it can be converted into int
a='30'
print(a,type(a))
b=int(a)
print(b,type(b))

#str ti integer conversion is not allowed
x='XYZ'
print(x,type(x))
#y=int(x)
#print(y,type(y))

p = float(input('Enter Float type data ')) #12.22
print(p, type(p))

#bool()
#1. While converting int to bool for all non zero values we will get True.
#2. While onverting int bool for 0 and empty strings we will get False.
q = 12
print(q, type(q))
q = bool(q)
print(q, type(q))

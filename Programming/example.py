li = list(map(int,input().split(","))) #10,20,30,40,40
li = list(set(li))
li.sort()   #sort() won't  return anything (None) #li = li.sort() will hold null value so don't do this
print("Largest Element",li[-1]) # 40
print("Second Largest Element",li[-2]) # 30
print("Smallest Element",li[0]) # 10
print("Second Smallest Element",li[1]) # 20


s1 = {1,2,3}
s2 = {1,2,3,4,5}
print(s1.issubset(s2)) #All ele of s1 are present in s2?True
print(s2.issubset(s1)) #All ele of s2 are present in s1?False


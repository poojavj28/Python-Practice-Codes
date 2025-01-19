li = list(map(int,input().split())) # [10,20,20,30]
d = {}
for i in li:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
for num,count in d.items():
    print(f"{num} occures {count} times(s)")

'''
10 20 20 30
10 occures 1 times(s)
20 occures 2 times(s)
30 occures 1 times(s)
'''
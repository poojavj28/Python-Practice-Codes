#Find Ruuner-up score
n = int(input())
li =list(map(int,input().split()))
li = list(set(li))
li.sort(reverse='True')
print(li[1])

'''
Output:
5   
2 3 6 6 5
5
'''
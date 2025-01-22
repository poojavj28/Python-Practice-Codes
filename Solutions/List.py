li = []
n =int(input())
for i in range(n):
    command, *values = input().split()
    values = list(map(int,values))
    if command == 'insert':
        li.insert(values[0],values[1])
    elif command == 'print':
        print(li)
    elif command == 'remove':
        li.remove(values[0])
    elif command == 'append':
        li.append(values[0])
    elif command == 'sort':
        li.sort()
    elif command == 'pop':
        li.pop()
    elif command == 'reverse':
        li.reverse()
        
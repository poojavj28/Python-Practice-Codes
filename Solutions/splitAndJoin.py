def split_and_join(line):
    line = line.split()
    return '-'.join(line)

res = split_and_join(input())
print(res)
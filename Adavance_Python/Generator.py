def disp():
    return 10
    return 20
    return 30

print(disp()) # 10
print(disp()) # 10
print(disp()) # 10

#Generator Concept:

def generator_function():
    print("one") # one
    yield 10 
    print("two") # two
    yield 20
    print("three") # three
    yield 30
print(generator_function()) # <generator object generator_function at 0x00000250FABE5F00>
ref = generator_function()
print(next(ref)) # 10
print(next(ref)) # 20
print(next(ref)) # 30
#print(next(ref)) # StopIteration

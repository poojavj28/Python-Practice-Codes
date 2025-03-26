'''
Strings are Immutable:
1. Once we declare the string we cannot modify it, 
if we try to modify the string it will create new string.

2. If new string does not have any reference variable then it will be removed.

3. Python Internally uses String Interning.

4. String Interning is the Process of Checking string Intern Pool before creating any new object.

Whenever we want to create new object, python first check string
intern pool, weather that object already exits or not.

when Object already exist in the string intern records then address of existing object will be reused.
'''
s1 = 'Kodnest'
s1 = s1.upper()
print(s1) # KODNEST

s2 = 'K'
print(s2,id(s2)) # K 140731212954560

s3 = 'Hello'
s4 = 'World'
print(s3,id(s3)) # Hello 2878409256144
print(s4,id(s4)) # World 2878409256336

print('s3 ID of H:',id(s3[0])) # s3 ID of H: 140731400190768
print('s4 ID of W:',id(s4[0])) # s4 ID of W: 140731400191488

print('s4 ID of o:',id(s4[1])) # s4 ID of o: 140731400192640
print('s3 ID of o:',id(s3[-1])) # s3 ID of o: 140731400192640

print('s3 ID of l:',id(s3[2])) # s3 ID of l: 140731400192496
print('s3 ID of l:',id(s3[3])) # s3 ID of l: 140731400192496
print('s4 ID of l:',id(s4[3])) # s4 ID of l: 140731400192496
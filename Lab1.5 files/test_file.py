f = open('hello.py','r')
print(type(f))

s = f.readline()
print(s)

f.seek(0)
for s in f:
    print(s)

f.seek(0)
L = f.readlines()
print(L)

f.seek(0)
L = list(f)  #быстрее чем readlines, но больше памяти
print(L)

f.close()
f = open('hello.py','a')
f.write('\n# Test string')

f.close()
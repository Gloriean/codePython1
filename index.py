#Array module
import array

obj = array.array('d', [1.2, 2.9, 3.7])
print(obj)
print(type(obj), obj)
print(obj.buffer_info())

var = array.array('d', [2.2, 4.5, 6.77])
print(var)
print(type(var), var)

num = array.array('I', [4, 5, 6])
print(num)
print(type(num), num)

add = array.array('d')
add = obj + var
print("Array add = " , add)

str = 'gfyyryrur'
array.array('u')
print(str)

import array
ver = array.array('i', [4, 5, 6, 9])
print(ver)

for i in ver:
    print(i)

for i in range(4):
    print(i)
#Classes and Objects


nM = array.array('i', [6, 67, 7, -9, -2, -12, 5])
for i in nM:
    print(i)

for pnt in range(5):
    print(pnt, nM[pnt])

nM.reverse()
print(nM)
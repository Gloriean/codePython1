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


nM = array.array('i', [6, 67, 7, -9, -2, -12, 5])
for i in nM:
    print(i)

for pnt in range(5):
    print(nM[pnt])
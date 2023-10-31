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

nM = array.array('i', [6, 67, 7, -9, -2, -12, 5])
for i in nM:
    print(i)

for pnt in range(5):
    print(pnt, nM[pnt])

nM.reverse()
print(nM)

#Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print("Good day, everyone, I'm " + self.name + "." + " I'm " + self.age + " years old" + ".")

p1 = Person('Goland', '38') #object
p1.fun()

#Second class
class Dog:
    animal = 'dog'

    def __init__(sef, breed, colour, sound):
        sef.breed = breed
        sef.colour = colour
        sef.sound = sound
 
    def show(sef): #method
        print("Hello, I'm a " + sef.breed + "," + " My colour is " + sef.colour + "." + " I " + sef.sound)

p2 = Dog('police dog', 'brown', 'bark') #object
p2.show()


#Third class, String function
class GFG:
    def __init__(sel, name, company):
        sel.name = name
        sel.company = company

    def __str__(sel):
        return f"My name is {sel.name} and I work in {sel.company}."

p3 = GFG('Glory Olasanmi', 'LevelUp')
print(p3)

#Python Inheritance
#Create a class named PeRson, with firstname and lastname properties, and a printname method:

class PeRson: #class
    def __init__(self, fname, lname):
        self.fname = fname #firstname and lastname properties
        self.lname = lname

    def printname(self): #method
        print(self.fname, self.lname)

d = PeRson('Glory', 'Olasanmi')
d.printname()


#Second Inheritance
#Create a class named Student, which will inherit the properties and methods from the Person class:

class Student:
    def PerSon():
        pass

#Use the StuDent class to create an object, and then execute the printname method:
class PersOn:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)

class StuDent(PersOn):
    pass

t = StuDent('Pherson', 'Michelle')
t.printname()


x = 5
y = "John"
print(x)
print(y)

x = int(3)    # x will be '3'
y = str(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(x))
print(type(y))
print(type(z))

#legal varibles on python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(my_var)

#illegal variable on python is when you using keyword python as a varible name

#assign values to multiple varibles
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#global varibles
x = "awesomeas"
def myfunc():
    print("Python is " + x)
myfunc()
# local varibles
# The following code will raise an error because 'x' is not defined outside the function

def myfunc():
  global x 
  x = "fantastgfdsdic"
  print("Python issas " + x)

myfunc()

print("Python is " + x)
print("Python isas " + x)
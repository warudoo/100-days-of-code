# Contoh Type data number dalam python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(y)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random Number
import random
print(random.randint(1, 1000))  # Menghasilkan bilangan bulat acak antara 1 dan 10
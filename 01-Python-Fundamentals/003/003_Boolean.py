a = 30
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
    
# Example of using f-string with boolean values
is_greater = a > b
print(f"Is a greater than b? {is_greater}")
# Example of using f-string with boolean expressions 
is_equal = a == b
print(f"Is a equal to b? {is_equal}")
# Example of using boolean in a conditional statement
if is_greater:
    print("Yes, a is greater than b")
else:
    print("No, a is not greater than b")
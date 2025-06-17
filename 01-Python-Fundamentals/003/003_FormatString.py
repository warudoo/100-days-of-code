age = 36
txt = f"My name is John, I am {age}"
print(txt)

# The f-string allows you to embed expressions inside string literals, using curly braces `{}`.
# This is a more readable and concise way to format strings compared to the older methods like `str.format()` or `%` formatting.

# Example of using f-string with a variable
name = "Alice"
greetings = f"Hai my name is {name} and i am {age} years old"
print(greetings)
# Example of using f-string with an expression
result = f"The sum of 5 and 10 is {5 + 10}"
print(result)
hasila = f"Hasil 5 x 10 = {5 * 10} dan 5 dibagi 10 = {5 / 10}"
print(hasila)
# Example of using f-string with a function call
def greet(name):
    return f"Hello, {name}!"
print(greet("SALWARUD"))
# Example of using f-string with a dictionary
person = {"name": "Bob", "age": 30}
info = f"Name: {person['name']}, Age: {person['age']}"
print(info)
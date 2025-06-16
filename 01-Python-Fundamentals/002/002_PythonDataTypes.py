x = 5
print(type(x))

# Contoh List
fruits_list = ["apple", "banana", "cherry"]
fruits_list.append("orange")  # Menambah item baru
fruits_list[0] = "mango"      # Mengubah item pertama
print(fruits_list)            # Output: ['mango', 'banana', 'cherry', 'orange']

# Contoh List
fruits_list = ["apple", "banana", "cherry"]
fruits_list.append("orange")  # Menambah item baru
fruits_list[0] = "mango"      # Mengubah item pertama
print(fruits_list)            # Output: ['mango', 'banana', 'cherry', 'orange']

# Contoh Dictionary
profile = {"name": "John", "age": 36}
print(profile["name"])  # Mengakses nilai dengan kuncinya
profile["age"] = 37     # Mengubah nilai
print(profile)          # Output: {'name': 'John', 'age': 37}

# Contoh Set
unique_fruits = {"apple", "banana", "cherry", "apple"} # "apple" kedua akan diabaikan
print(unique_fruits)      # Output: {'banana', 'cherry', 'apple'} (urutan bisa berbeda)
print("banana" in unique_fruits) # Sangat cepat. Output: True

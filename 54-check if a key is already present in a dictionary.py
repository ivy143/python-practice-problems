#check if a key is already present in a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
key_to_check = "age"

if key_to_check in my_dict:
    print(f"The key '{key_to_check}' is present in the dictionary.")
else:
    print(f"The key '{key_to_check}' is not present in the dictionary.")
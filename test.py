
arr = ["1 3", "456", " 89"]

string_item = "123 456 789"

new_arr = ["".join(chars).replace(" ", "") for chars in zip(*arr)]

print(new_arr)
    
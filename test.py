def rem_leading_and_trailing_duplicates(string):
    item_log = {}
    new_str = ""
    for char in string:
        item_log[str(char)] = "GUH"
    for key, value in item_log.items():
        new_str += key
    print(new_str)

rem_leading_and_trailing_duplicates("hhhhhellooooo")
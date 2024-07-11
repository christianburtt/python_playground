

input_string = input("Enter a variable name in camelCase: ")

snake_case = ""
for character in input_string:
    if (character.isupper()):
        snake_case = snake_case + "_" + character.lower()
    else:
        snake_case = snake_case + character

print(snake_case)

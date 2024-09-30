# Task 1: Custom Module with Aliases 

import text_utils as tu

text = input("Enter some text: ")

reversed_text = tu.reverse_string(text)
capitalized_text = tu.capitalize_string(text)

print(f"Reversed: {reversed_text}")
print(f"Capitalized: {capitalized_text}")



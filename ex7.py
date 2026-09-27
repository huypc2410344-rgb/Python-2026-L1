def remove_dollar_sign(s):
    return s.replace("$", "")

text_input = input("Enter a string with dollar signs: ")
result = remove_dollar_sign(text_input)
print(f"Result: {result}")
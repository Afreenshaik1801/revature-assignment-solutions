# 4. To Print all uppercase letters in a string using a for loop
text = "BHanu"
print("Uppercase letters in string:")
for char in text:
    if char.isupper():
        print(char, end=" ")
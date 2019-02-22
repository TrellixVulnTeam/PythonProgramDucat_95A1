# Python Program - Convert Uppercase to Lowercase

print("Enter 'x' for exit.")
string = input("Enter any string in uppercase to convert in lowercase: ")
if string == 'x':
    exit()
else:
    string_in_lowercase = string.lower()
    print("\nSame String in Lowercase =",string_in_lowercase)
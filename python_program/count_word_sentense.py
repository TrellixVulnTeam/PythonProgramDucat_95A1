# Python Program - Count Word in Sentence

print("Enter 'x' for exit.")
string = input("Enter any string to count word: ")
if string == 'x':
    exit()
else:
    word_length = len(string.split());
    print("\nNumber of words =",word_length)
# Python Program - Count Number of Each Vowels

print("Enter 'x' for exit.")
string = input("Enter any string to count number of each vowel: ")
if string == 'x':
    exit()
else:
    vowels = 'aeiou'
    string = string.casefold()
    count = {}.fromkeys(vowels,0)
    print();
    for char in string:
        if char in count:
            count[char] += 1
    print(count)
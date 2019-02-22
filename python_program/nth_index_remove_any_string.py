#120.   nth index remove the string charter value form.>>>

def remove(string, n):
    first = string[:n]
    last = string[n+1:]
    return first + last                       # remove last charter in string values.
string = input("Enter the sring:")
n = int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n+1))
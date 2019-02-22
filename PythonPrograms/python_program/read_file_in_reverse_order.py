#132.  # Read the Contents of a File in Reverse Order .??

filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())
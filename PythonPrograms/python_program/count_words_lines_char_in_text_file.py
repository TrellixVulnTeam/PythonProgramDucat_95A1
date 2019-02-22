#73.  Count the Number of Words,lines,char in a Text File. ??


file=open("word.txt","w")
txt="ram gher jata hai \nshyam ram ko marta hai \nshamu ramu ka bhai hai"
file.write(txt)
file.close()

numline=0
numword=0
numchar=0

with open("word.txt","r") as file:
   for line in file:
       wordlist=line.split(" ")
       numline= numline+1
       numword= numword + len(wordlist)
       numchar= numchar+ len(line)
print(numline)
print(numword)
print(numchar)
file.close()
# string the mathod used to applied any process mathod ...????
# got the output in any string value to boolean value true/false ....????


a= "Hello Python World"
b= "hello python world"
c= "hello \t python \t world"
d= "こんにちは"
e= "def"
f= '56'

print(a.capitalize())     # any string value find in first cpiltize number  ...  (small char)
print(a.isupper())        # any string value find in uppercase ...  (captilize char)
print(a.islower())        # any string value find in lowercase ...  (small char)
print(a.split())          # any string value (break any string to all word in other line to line)
print(a.isalnum())        # any string is  in string num value or char vlaue but not read any special char  like that  ...  @ # $ % ^  (not used in any string)
print(a.isalpha())        # any string is not used special char in string like that  ...  @ # $ % ^  (not used in any string)
print(len(a))             # find the string length ..
print(a.find("l"))        # find the any char in string word (pass any char in parasentenses ("chr",start value,stop value ))
# find used any char given output always (-1). but not char in given string   .
print(a.index("l"))       # index of any char input string.
print(a.index("l",0,5))       # index of any char input string.
print(a[0:12])            # find the any value of 0to12 between all value find out all value char.
print(a.count("l"))       # any string find and count any char in count number.
print(a.find("left"))     # find the any world but not include string so got (-1).    always
print(a.casefold())       # any string use this mathod so output came always caseless.
if (a==b):                # both are compare to caseless value of string. 
	a.casefold(b)
print(a.center(30,"*"))   # string built in centre and after and before getting fillchar.(*)   o/t-->>    *****hello python world*****
print(a.encode(encoding="utf16"))     # string built in fuction to machenary coding like that ..  ("utf8","utf16"...)  
print(a.encode(encoding="utf8"))
print(a.count("l"))               # string find the char in string how many times in this strings.
print(a.endswith("world"))     	  # its return value in true/false the world in string or not.
print(c.expandtabs(tabsize=8))    # tab size increse '\t' string get tab space then print size of space.

'''
format(....)                    ------------>>>>>>>>>         forget next 
format_map(....)                ------------>>>>>>>>>         using in class insilized to slice to again ...???
'''

print(a.index('l',0,18) )         # index is used the char position in list form just like .. got left to right first index so print them (o/t --- 2) but not print (3, and 14)
print(a.isascii())                # any string all charcter in the ascii value or not (given ans in True / False)   ------>>>  boolean ans in result.
print(d.isascii())                 # not read japnese char in ascii not given ..  (o/t ---  Flase.)
print(f.isdecimal())              # read only decimal value in string .
print(f.isdigit())                # read only the digit value in any given string.
print(a.isidentifier())           # python def any fuction otherwise print the python class o/t always True , otherwise False...??  (any string but not use python def and class type..)
print(b.isprintable())            # any string we can print the any string then output given True and false..          
print(f.isnumeric()               # any string value this mathod onlu find the numeric value given result in true or false..?? 
print(b.isspace())                #not worked any one.../   # any string value used in whitespace (' ','\t','\n' ....  all used whitespaces ).   
print(c.istitle())                # not worked in file .../   # (title used based in used for any one ...)
p = ','.join(['qu','gd','pr'])
print(p)                          # not work in join of list all char.
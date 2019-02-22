#133.    Remove the Characters of Odd Index Values in a String .??

def remove(string):      # define the string key.
  final = ""               # final= space
  for i in range(len(string)):    # in range i for len of string.
    if i % 2 == 0:                 # condition final print:
      final = final + string[i]
  return final                      # call final value.
string = input("Enter string:")
print("Modified string is:",remove(string))            # print string which remove odd charters parts.
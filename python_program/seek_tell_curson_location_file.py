# seek and tell telling the cursor leaving any postion tell on the function and the seek carry on the cursor is 0th position...??

f = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\railway.txt","r+")
f.seek(0)                                 # carry to movoes last postion to 0th position.
print(f.tell())
print(f.readline()) 
print(f.tell())                           # search what postion of the cursor location position.
print(f.readlines())
print(f.tell())
f.close()



'''
output ===

0

Streamline the booking experience  20 feb to 31 dec 2018-19.

63

['Make booking rail more cost efficient, \n', 'removing complexity from the rail booking process. \n', 'Rail providers across the globe\n',
 'Amadeus Rail Display is a dedicated rail booking tool\n', ' with one of the most comprehensive sources of rail content \n', 
 'in the world, including full content from local rail providers\n', ' in all key European rail markets.\n', 
 'Simple Yet Smart Technology\n', 'The Amadeus Rail application features a user-friendly graphical\n', 
 ' interface and offers fast and intuitive end-to-end booking flows.\n', ' Fully integrated into the Amadeus Selling Platform, the rail API enables\n',
 ' you to build your own booking engine, too.\n', 'Upsell ancillary services \n', 'Give your customers a relaxed experience in all things travel,\n', 
 ' relieving their stress by offering smoothly connecting transport to and from the airport, \n', 'city center or venue 2018-19. ']

 904

'''
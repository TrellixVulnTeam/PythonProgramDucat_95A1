# any word search in given file output is given that in his searching the word how much time in file..??

f = open("C:/Users/Saurabh/Desktop/file_handle/mahabharat.cpp","r",encoding="utf-8")
a=f.read()
e=a.split()
c=0
for x in e:
	if x =="of":
		c = c+1
print("searching word how many time : " , c)
f.close()


'''
output ====
searching word how many time :  19

'''



f = open("C:/Users/Saurabh/Desktop/file_handle/mahabharat.cpp","r",encoding="utf-8")
a=f.read()
print(a)
e=a.split()
c=0
n = input("searching any word in this file : ")
for x in e:
	if x == n:
		c = c+1
print("searching word how many time : " , c)
f.close()



'''
output ===


The Mahābhārata is an epic legendary narrative of the Kurukṣetra War and the fates of the
 Kaurava and the Pāṇḍava princes. It also contains philosophical and devotional material,
 such as a discussion of the four "goals of life" or puruṣārtha (12.161). Among the principal
 works and stories in the Mahābhārata are the Bhagavad Gita, the story of Damayanti, an abbreviated
 version of the Rāmāyaṇa, and the story of Ṛṣyasringa, often considered as works in their own right.
Traditionally, the authorship of the Mahābhārata is attributed to Vyāsa. There have been many attempts to
 unravel its historical growth and compositional layers. The oldest preserved parts of the text are thought
 to be not much older than around 400 BCE, though the origins of the epic probably fall between the 8th and 9th centuries BCE.
 [4] The text probably reached its final form by the early Gupta period (c. 4th century CE).[5][6] According to the Mahābhārata
 itself, the tale is extended from a shorter version of 24,000 verses called simply Bhārata.[7]
The Mahābhārata is the longest epic poem known and has been described as "the longest poem ever written".
[8][9] Its longest version consists of over 100,000 śloka or over 200,000 individual verse lines (each shloka is a couplet),
 and long prose passages. At about 1.8 million words in total, the Mahābhārata is roughly ten times the length of the Iliad and the
 Odyssey combined, or about four times the length of the Rāmāyaṇa.[10][11] W. J. Johnson has compared the importance of the Mahābhārata
 in the context of world civilization to that of the Bible, the works of William Shakespeare, the works of Homer, Greek drama,
 or the Quran.[12] Within the Indian tradition it is sometimes called the Fifth Veda.
 
 
 
searching any word in this file : an
searching word how many time :  2


'''
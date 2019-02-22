# Python Calculate Grade of Student  ???

# student result in inter with grade ..???

sum = 0
for i in range(5):
	n = int(input("enter the no of subject : "))
	sum = sum + n
print("total sum of all subject: ",sum)
result = sum
pecentange = (result * 100) / 500
print("total marks of subject in inter out of : 500 ")
print()

print(" ###############  '\n'   pecentange below 33% '\n' then fail and F Grade. '\n' ")
print(" pecentange  33% to 45% '\n' then pass and D Grade. '\n' ")
print(" pecentange  45% to 60% '\n' then pass and B Grade. '\n' ")
print(" pecentange  60% to 80% '\n' then passed good and A Grade. '\n' ")
print(" pecentange  80% to 90%  '\n' then passed honner and H Grade. '\n' ")
print(" pecentange  90% to 100% '\n' then passed super grade with excellent performance and S Grade. '\n'  ################ ")

print()

if pecentange < 33:
	print(" ************   pecentange below 33% '\n' then fail and F Grade. *********** '\n' ")
elif pecentange >=33 and pecentange < 45:
	print(" ***********    pecentange  33% to 45% '\n' then pass and D Grade.  *********** '\n' ")
elif pecentange >=45 and pecentange < 60:
	print(" *********** pecentange  45% to 60% '\n' then pass and B Grade. *********** '\n' ")
elif pecentange >=60 and pecentange < 80:
	print(" *********** pecentange  60% to 80% '\n' then passed good and A Grade. *********** '\n' ")
elif pecentange >=80 and pecentange < 90:
	print(" *********** pecentange  80% to 90%  '\n' then passed honner and H Grade. *********** '\n' ")
elif pecentange >=90 and pecentange < 100:
	print(" ***********  pecentange  90% to 100% '\n' then passed super grade with excellent performance and S Grade. *********** '\n' ")
elif pecentange == 100:
	print(" *********** pecentange 100% '\n' then passed super grade with excellent performance mind belowing and S++  Grade. *********** '\n' ")
else:
	print("***********  result invalid.")
	print("try again no response your result.  '\n' ***********  ")
	
	
"""
output == 
enter the no of subject : 100
enter the no of subject : 100
enter the no of subject : 100
enter the no of subject : 100
enter the no of subject : 100
total sum of all subject:  500
total marks of subject in inter out of : 500

 ###############  '
'   pecentange below 33% '
' then fail and F Grade. '
'
 pecentange  33% to 45% '
' then pass and D Grade. '
'
 pecentange  45% to 60% '
' then pass and B Grade. '
'
 pecentange  60% to 80% '
' then passed good and A Grade. '
'
 pecentange  80% to 90%  '
' then passed honner and H Grade. '
'
 pecentange  90% to 100% '
' then passed super grade with excellent performance and S Grade. '
'  ################

 *********** pecentange 100% '
' then passed super grade with excellent performance mind belowing and S++  Grade. 
*********** '
'
"""
#24.  Read Height in Centimeters and then Convert the Height to Feet and Inches ...??



height= float(input("enter the height of the men/women: "))
feet2=height/(30.5)
print("feet2",feet2)
feet=int(feet2)
feet1=feet2-feet
# print(feet)
inch=(feet1)*12
inch=(round(inch,2))
# print(inch)
print(feet,"feet",inch,"inches")
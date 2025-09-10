score=int(input("Enter Score:"))
if score<=100 and score>=90:
	print("Grade A+")
elif score<=89 and score>=80:
	print("Grade A")
elif score<=79 and score>=70:
	print("Grade B+")
elif score<=69 and score>=60:
	print("Grade B")
elif score<=59 and score>=50:
	print("Grade C")
else:
	print("Fail")


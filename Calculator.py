def calculator():
	choice=int(input("Press 1 for Addition \nPress 2 for Substraction \nPress 3 for multiplication \nPress 4 for division \nEnter a valid choice:"))
	if choice==1:
		x=int(input("Enter x:"))
		y=int(input("Enter y:"))
		result=x+y
		print(result)
	elif choice==2:
		x=int(input("Enter x:"))
		y=int(input("Enter y:"))
		result=x-y
		print(result)
	elif choice==3:
		x=int(input("Enter x:"))
		y=int(input("Enter y:"))
		result=x*y
		print(result)
	elif choice==4:
		x=int(input("Enter x:"))
		y=int(input("Enter y:"))
		result=x/y
		print(result)
	else:
		print("Invalid choice")
		calculator()

calculator()

print("Welcome to formula program")
print("Folling formula are available")
choice=int(input("Press 1 for (a+b)^2=(a*a)+(b*b)+(2*a*b) \nPress 2 for (a-b)^2=(a*a)+(b*b)-(2*a*b) \nPress 3 for a^2-b^2=(a+b)*(a-b) \nPress 4 for (x+b)*(x+b)=(x*x)+(a*x)+(b*x)+(a*b) \nEnter your's choice:"))

if choice==1:
	print("You have selected formula")
	a=int(input("Enter a:"))
	b=int(input("Enter b:"))
	result=(a*a)+(b*b)+(2*a*b)
	print(result)

elif choice==2:
	print("You have selected formula")
	a=int(input("Enter a:"))
	b=int(input("Enter b:"))
	result=(a*a)+(b*b)-(2*a*b)
	print(result)

elif choice==3:
	print("You have selected formula")
	a=int(input("Enter a:"))
	b=int(input("Enter b:"))
	result=(a+b)*(a-b)
	print(result)

elif choice==4:
	print("You have selected formula")
	x=int(input("Enter x:"))
	a=int(input("Enter a:"))
	b=int(input("Enter b:"))
	result=(x*x)+(a*x)+(b*x)+(a*b)
	print(result)

else:
	print("invalid choice")
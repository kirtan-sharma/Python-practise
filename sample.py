billing_amout = 0
next_choice = True
while next_choice :
	choice = int(input("press 1 for samosa\nPress 2 for tea\nPress 3 for cold drink\nPress a valid choice:"))
	if choice == 1 :
		quantity = int(input("Enter No. of samosa : "))
		price = 10
		amount = quantity * price
	elif choice == 2 :
		quantity = int(input("Enter No. tea : "))
		price = 5
		amount = quantity * price
	elif choice == 3 :
		quantity = int(input("Enter No. cold drink : "))
		price = 20
		amount = quantity * price
	else :
		print("invalid item")
	billing_amout = billing_amout + amount
	next_item = input ("Enter y to add other item or any other key to stop")
	if next_item == "y" or next_item == "Y" :
		next_choice = True
	else :
		next_choice = False

print("Bill Details")
print("Your Bill is {} inr" .format(billing_amout))

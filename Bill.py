Price=float(input("Enter Price:"))
Quantity=float(input("Enter Quantity:"))
AWT=Price*Quantity
tax=(AWT*10)/100
BA=AWT+tax
print("Billing amount=",BA)
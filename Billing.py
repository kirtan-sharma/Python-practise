menu_item = ["Chips","chocolate","coke"]
bill = []

for i in menu_item:
	print(i)
	quantity = int(input("Enter no. of item:"))
	rate = 10
	amount = quantity * rate
	item = [i,quantity,rate,amount]
	bill.append(item)
	print(bill)

total_amount = 0

for k in bill :
	total_amount = total_amount = k[3]

cgst = (total_amount * (5/100))
sgst = (total_amount * (5/100))

payable_amount=total_amount+cgst+sgst

for j in bill:
	print(j)

print("Amount:",total_amount)
print("CGST:",cgst)
print("SGST:",sgst)
print("Total:",payable_amount)
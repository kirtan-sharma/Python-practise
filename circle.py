def circle():
	r=int(input("Enter radius:"))
	a=r*r*(22/7)
	c=r*2*(22/7)
	print("Area for {};{}".format(r,a))
	print("Circumference for {};{}".format(r,c))
for i in range(10):
	circle()
	

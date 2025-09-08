def facts():
	val = int(input("Enter Value : "))
	fact = 1 
	for i in range(1,val+1):
		fact = fact	* i 
	print("Factorial of {} is {}".format(i,fact))

def facts(var1):
	fact = 1 
	for i in range(1,var1+1):
		fact = fact	* i 
	#print("Factorial of {} is {}".format(i,fact))
	return 	fact

#calculate permutation of n = 5 on r = 3 (nPr = n!/(n-r)!)
#calculate combination of n = 5 on r = 3 (nCr = n!/(r! * (n-r)!))
n = 5
r = 3 
permutation	 = facts(n)/facts(n-r)
combination = facts(n)/facts(r)*facts(n-r)
print("Permutation = ",permutation)
print("Combination = ", combination)
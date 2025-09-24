#Factorial For loop

n=int(input("Enter value:"))
fact_n=1
for i in range(1,n+1):
	fact_n=fact_n*i
print("Factorial=",fact_n)
print("This is by For loop")

#Factorial While loop

n=int(input("Enter value:"))
fact_n=1
s=1
while(s<=n):
	fact_n=fact_n*s
	s=s+1
print("Factorial=",fact_n)
print("This is by while loop")

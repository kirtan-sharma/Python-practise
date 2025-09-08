N=int(input("Enter value of N:"))
R=int(input("Enter value of R:"))
fact_N=1
for i in range(1,n+1):
	fact_N=fact_N*i
fact_NR=1
for j in range (1,(N-R)+1):
	fact_NR=fact_NR*j
NPR=fact_N/fact_NR
print("{}P{}={}".format(N,R,NPR))
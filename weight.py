student = []
n = int(input("Enter the No. of Students in the class : "))
sum = 0
for i in range(n):
	x = float(input("Enter the weight of the student : "))
	sum = sum + x
	student.append(x)
	print(student)
average = sum/n
print("Average of Student weight in a class where weight are {} is {}".format(student,average))
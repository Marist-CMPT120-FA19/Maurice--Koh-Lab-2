#HW Building a tree

def main():
	n = int(input("Please enter the number of branches:"))
	for x in range(n):
		print((" " * (n - x)),('#' * (2*x+1)))
	print(n*" ", "#")

main()








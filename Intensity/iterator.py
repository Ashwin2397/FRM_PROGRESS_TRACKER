import os 

def main():

	n_books=input("Enter number of books: ")
	
	
	for i in range(0,int(n_books)):

		start=input("Enter start reading: \n")
		end=input("Enter end reading: \n")

		file= "book"+str(i+1)+".txt"

		with open(file,"w") as op:

			for x in range(int(start),int(end)+1):
				op.write("R"+" "+str(x)+"\n")

if __name__ == '__main__':
	main()
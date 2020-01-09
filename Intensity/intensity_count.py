import os 
import sys 

def main():

	for i in range(1,5):

		file="book"+str(i)+"_intensity.txt"

		with open(file,"r") as ip:

			lines=ip.readlines()

			easy_count=len([item for item in lines if("Easy" in item)])
			med_count=len([item for item in lines if("Medium" in item)])
			hard_count=len([item for item in lines if("Hard" in item)])

		with open(file,"a") as op:

			op.write("\n\n")
			op.write("=====================================STATISTICS====================================\n\n")
			op.write("EASY COUNT: "+str(easy_count)+"\n")
			op.write("MED COUNT: "+str(med_count)+"\n")
			op.write("HARD COUNT: "+str(hard_count)+"\n")






if __name__ == '__main__':
	main()
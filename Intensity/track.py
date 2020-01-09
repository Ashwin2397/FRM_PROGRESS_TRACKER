
#MIght be garbage but i saved it anyways 


import os 
import datetime 
import csv 


def main():

	# print(datetime.date(2020))
	print(str(datetime.datetime.now()).split(" ")[0])
	exit()

	prompt=input("Enter start or end and Reading_Number: \n")

	fieldnames=["Date","Reading_Number","Start_Time","End_Time"]


	if("track.csv" in os.listdir()):

		with open("track.csv","w") as op:

			if prompt.split(" ")[0]=="start":

				reader=csv
				writer=csv.Dictwriter(op,fieldnames=fieldnames)





	else:

		with open("track.csv","w") as op:

			writer=csv.Dictwriter(op,fieldnames=fieldnames)

			writer.writeheader()
			datetime_list=str(datetime.datetime.now()).split(" ")
			writer.writerow({"Date":datetime_list[0],"Reading_Number":prompt.split(" ")[1],"Start_Time":datetime_list[1],"End_Time":"-"})





if __name__ == '__main__':
	main()
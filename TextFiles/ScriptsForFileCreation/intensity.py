import os 
import sys 

constants=((1,15),(16,36),(37,63),(64,81))

def main():

	for i in range(1,5):

		ip_file="book"+str(i)+".txt"
		op_file="book"+str(i)+"_intensity"+".txt"

		with open(ip_file,"r") as ip:

			lines=ip.readlines()
			keys=[int(item.strip("\n").split(" ")[1]) for item in lines]
			n_pages=[int(item.strip("\n").split(" ")[2]) for item in lines]

			rnum_pagenum=create_dict(keys,n_pages)
			

		r_left=getList() #List must be integers

		with open(op_file,"w") as op:

			for key in rnum_pagenum:

				if(key in r_left):
					op.write("R "+str(key)+" "+intensity_value(rnum_pagenum[key])+"_REDUNDANT?"+"\n\n")

				else:
					op.write("R "+str(key)+" "+intensity_value(rnum_pagenum[key])+"\n\n")

		
def getList():
		
	with open("readings_left.txt","r") as ip:

		r_list=[int(item.strip("\n")) for item in ip]

	return r_list


def intensity_value(n_pages):

		"""
		- 7 and below is easy?
		- 8-11 is medium
		- 12 and above is hard
		*N.B* SUBJECT TO CHANGES

		RETURNS:
			String with intensity value followed by number of pages
		"""
		intensity=""
		if(n_pages<=7):
			#Easy
			intensity="Easy"
		elif(n_pages>=8 and n_pages<=11):
			#Medium
			intensity="Medium"
		elif(n_pages>=12):
			#Hard
			intensity="Hard"

		return f"{intensity}_n_Pages:{n_pages}"	

def create_dict(keys,n_pages):

	n_dict={}

	for i in range(len(keys)):
		n_dict[keys[i]]=n_pages[i]

	return n_dict


if __name__ == '__main__':
	main()
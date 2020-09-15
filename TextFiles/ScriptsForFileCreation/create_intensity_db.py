import os 
import sys
import sqlite3
import intensity
import sql_util 

constants=((1,15),(16,36),(37,63),(64,81))

def main():

	cursor,con=sql_util.create_cursor_con("randz.db")

	sql_util.create_table(cursor,"intensity",["reading text", "n_pages text", "intensity text"])

	for i in range(1,5):

		ip_file="book"+str(i)+".txt"

		with open(ip_file,"r") as ip:

			lines=ip.readlines()
			keys=[int(item.strip("\n").split(" ")[1]) for item in lines]
			n_pages=[int(item.strip("\n").split(" ")[2]) for item in lines]

			rnum_pagenum=intensity.create_dict(keys,n_pages)
			



		for key in rnum_pagenum:

			cursor.execute(r"INSERT INTO"+" intensity "+"VALUES(?,?,?);",(str(key),str(rnum_pagenum[key]),intensity_value(rnum_pagenum[key])))
			# Reading #, number of pages, intensity

	sql_util.print_table(cursor,"intensity","81")
	sql_util.close(con)


def print_table(cursor):

	print("\n\nINTENSITY TABLE: \n")
	print("Reading Number, Number of pages, Intensity,\n")

	i=1
	# cursor.execute(r'SELECT * FROM intensity WHERE reading=?',(str(i),))
	cursor.execute(r'SELECT * FROM intensity LIMIT 0,81')
	row=cursor.fetchone()

	while row!=None:
		print(row)
		row=cursor.fetchone()
	# while(row!=None):

	# 	print(row)
	# 	i+=1
	# 	cursor.execute(r'SELECT * FROM intensity WHERE reading=?',(str(i),))
	# 	# cursor.execute(r'SELECT * FROM intensity')

	# 	row=cursor.fetchone()



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

		return intensity	


if __name__ == '__main__':
	main()
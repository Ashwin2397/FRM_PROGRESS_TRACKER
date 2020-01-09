import sqlite3
import datetime
import os 

"""
SQL_TIPS:
	
	- Exectute Args:
		1.Pass in execute statement as a raw string with "?" in its placeholder
		2.Pass in arguments as a tuple

	- End statements with semi-colon ";" 

	- cursor.fetchone() returns a tuple

	SQL KEYWORDS:

		*N.B* 
		use UPPERCASE for keywords(to diffrentiate keywords),
        SQL stms are case sensitive 
		*N.B*
		
		List of keywords:
			SELECT
			INSERT
			VALUES
			WHERE 


"""

def main():


	cursor,con=create_cursor()

	initial_prompt(cursor)

	prompt=input("Enter in format: [read/study] [start/end] [reading number]: \n")
	prompt_list=prompt.split(" ")

	pass_flow(prompt_list,cursor)

	con.commit()
	con.close()

def initial_prompt(cursor):

	print("*****************************************************************\n\n")
	print("q - Quit")
	print("s - Store information")
	print("g - Get all tables")
	print("*****************************************************************\n\n")

	prompt=input("Enter appropriate command: \n")

	if prompt=="q":
		exit()
	elif prompt=="s":
		return
	else:
		printRow(cursor)
		exit()

def create_cursor():

	if not "tracker.db" in os.listdir():

		con=sqlite3.connect("tracker.db")
		curser=con.cursor()
		curser.execute('''CREATE TABLE start_end (date text, reading text, start text, end text )''')
		curser.execute('''CREATE TABLE read_time (date text, reading text, start text, end text )''')
		
	else:
		con=sqlite3.connect("tracker.db")
		curser=con.cursor()

	return curser,con

def pass_flow(prompt_list,cursor):

	datetime_list=getDateTime()

	if(prompt_list[1]=="start"):
		write_row(cursor,prompt_list,datetime_list)
	else:
		update_row(cursor,prompt_list,datetime_list)


def write_row(cursor,prompt_list,datetime_list):

	end='-'
	if prompt_list[0]=="study":
		execute_stm=r'''INSERT INTO start_end VALUES(?,?,?,?);'''
	else:
		execute_stm=r'''INSERT INTO read_time VALUES(?,?,?,?);'''

	cursor.execute(execute_stm,(datetime_list[0],prompt_list[2],datetime_list[1],end))



def update_row(cursor,prompt_list,datetime_list):

	if prompt_list[0]=="study":
		execute_stm=r'''UPDATE start_end SET end=? WHERE reading=?;'''
	else:
		execute_stm=r'''UPDATE read_time SET end=? WHERE reading=?;'''

	cursor.execute(execute_stm,(datetime_list[1],prompt_list[2]))
	
def printRow(cursor):

	print("\n\nStudy Timings Table: \n")
	print("Date,Reading Number, Start Time, End Time\n")

	i=1
	cursor.execute('SELECT * FROM start_end WHERE reading=?',str(i))
	row=cursor.fetchone()

	while(row!=None):

		print(row)
		i+=1
		cursor.execute('SELECT * FROM start_end WHERE reading=?',str(i))
		row=cursor.fetchone()
	print("\n\n")
	print("Reading Timings Table: \n")
	print("Date,Reading Number, Start Time, End Time")

	i=1
	cursor.execute('SELECT * FROM read_time WHERE reading=?',str(i))
	row=cursor.fetchone()

	while(row!=None):

		print(row)
		i+=1
		cursor.execute('SELECT * FROM read_time WHERE reading=?',str(i))
		row=cursor.fetchone()

def getDateTime():

	return str(datetime.datetime.now()).split(" ")








if __name__ == '__main__':
	main()
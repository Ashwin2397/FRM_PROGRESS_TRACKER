import sqlite3
import datetime
import os
import sql_util

"""

GOAL: 

	- Clock 5 hours of revision in a week
		- Have a feature to clock revision times and add them together to review weekly sessions to see if goal has been met
		  If goal is not met, decrease/increase goal where appropriate
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
			FROM
			LIMIT
			UPDATE
			SELECT

"""


def main():


	cursor,con=sql_util.create_cursor_con("tracker.db")

	initial_prompt(cursor,con)

	con.commit()
	con.close()

def updateTable(cursor,start,end,readingNumber,table):
	
	
	cursor.execute(f"UPDATE {table} SET start=?,end=?,time=? WHERE reading=?;",(start,end,timeTaken(start,end),readingNumber,))
	
def store_prompt():

	prompt=input("Enter in format: [read/study] [start/end] [reading number]: \n")

	if prompt=="e":
		exit()

	cfm=input("Would you like to confirm this command: "+prompt+" ?\nEnter y or n: ")

	if cfm=="y":
		return prompt.split(" ")
	elif cfm=="e":
		exit()
	else:
		return store_prompt()





def initial_prompt(cursor,con):

	print("*****************************************************************\n\n")
	print("e - Exit")
	print("s - Store Information")
	print("g - Get Information")
	print("d - Delete Information")
	print("p - Pause")
	print("u - Update Information")
	print("*****************************************************************\n\n")

	prompt=input("Enter appropriate command: \n")

	if prompt=="e":
		exit()
	elif prompt=="s":
		pass_flow(store_prompt(),cursor)
	elif prompt=="g":
		get(cursor,con)
	elif prompt=="d":
		delete(cursor)
	elif prompt=="p":
		pause(cursor)
	elif prompt=="u":
		update(cursor)


	con.commit()
	initial_prompt(cursor,con)

def update(cursor):

	print("*****************************************************************\n\n")
	prompt=input("\nEnter in Format: [read/study] [startTime: 10:41:50] [endTime: 10:42:50] [readingNumber]\n").strip().split(" ")

	if(prompt=="e"):
		exit()
	updateTable(cursor=cursor,table=table_name(prompt[0]),start=prompt[1],end=prompt[2],readingNumber=prompt[3],)


	


def prompt_map(prompt):


	"""Work in progress"""
	constants={"easy":"Easy","med":"Medium","hard":"Hard"}

	return 
def pause_end(cursor,prompt_list):

	"""
	PARAMETERS:
		-Prompt_list: [read/study] [reading number]
	OUTPUT:
		- Ends this reading 
	"""

	if prompt_list[0]=="read":
		#update reading from table, to end it, 
		cursor.execute("SELECT start FROM read_time WHERE reading=?",prompt_list[1])
		start=cursor.fetchone()[0]
		execute_stm=r'''UPDATE read_time SET start=?,end=?,time=? WHERE reading=?;'''

	elif prompt_list[0]=="study":
		#update reading from table, to end it, 
		cursor.execute("SELECT start FROM start_end WHERE reading=?",prompt_list[1])
		start=cursor.fetchone()[0]
		execute_stm=r'''UPDATE start_end SET start=?,end=?,time=? WHERE reading=?;'''

	cursor.execute(execute_stm,("PAUSE","PAUSE",timeTaken(start,getDateTime()[1]),prompt_list[1]))


def pause(cursor):

	"""
	OUTPUT:
		- Pauses reading that had been specified to pause 
	
	IMPLEMENTATION:
		- To aid "UI"
			- Issue Pause flag with R#
			- Pause flag simply ends Reading
			- Upon end of pause, User will simply Start reading again 
				- When reading is started, nothing will happen		
	"""
	print("\n*****************************************************************\n\n")
	prompt=input("Enter in format: [read/study] [reading number]\n")
	prompt_list=prompt.split(" ")

	pause_end(cursor,prompt_list)


def delete(cursor):

	print("\n*****************************************************************\n\n")
	prompt=input("Enter in format [read/study] [reading number]:\n")

	prompt_list=prompt.split(" ")

	sql_util.delete_row(cursor,table_name(prompt_list[0]),"reading",prompt_list[1])


def table_name(r_s):

	if r_s=="read":
		return "read_time"

	return "start_end"

def create_cursor(file_name):

	if not file_name in os.listdir():

		con=sqlite3.connect(file_name)
		curser=con.cursor()
		curser.execute('''CREATE TABLE start_end (date text, reading text, start text, end text, time text )''')
		curser.execute('''CREATE TABLE read_time (date text, reading text, start text, end text, time text )''')
		
	else:
		con=sqlite3.connect(file_name)
		curser=con.cursor()

	return curser,con

def pass_flow(prompt_list,cursor):

	datetime_list=getDateTime()

	if(prompt_list[1]=="start"):
		#Check for pause
		write_row(cursor,prompt_list,datetime_list)
	elif(prompt_list[1]=="end"):
		update_row(cursor,prompt_list,datetime_list)


def write_row(cursor,prompt_list,datetime_list):

	if(check_pause(cursor,prompt_list)):
		execute_stm="UPDATE "+map(prompt_list[0])+" SET start=? WHERE reading=?;"
		cursor.execute(execute_stm,(getTime(),prompt_list[2],))
	else:

		end='-'
		time="-"
		if prompt_list[0]=="study":
			execute_stm=r'''INSERT INTO start_end VALUES(?,?,?,?,?);'''
		else:
			execute_stm=r'''INSERT INTO read_time VALUES(?,?,?,?,?);'''

		cursor.execute(execute_stm,(datetime_list[0],prompt_list[2],datetime_list[1].split(".")[0],end,time))

def getTime():

	return getDateTime()[1].split(".")[0]

def getDate():

	return getDateTime()[0]

def map(table_name):

	constant={"read":"read_time","study":"start_end"}

	return constant[table_name]

def check_pause(cursor,prompt_list):

	time=sql_util.select_from_where(cursor,"time",map(prompt_list[0]),"reading",prompt_list[2])

	if time!=None and time[0]!="-":
		return True

	return False

def get(cursor,con):

	print("*****************************************************************\n\n")
	print("e - Exit")
	print("g - Get all tables")
	print("gr - Get reading tables")
	print("p - Get progress")
	print("gi - Get Intensity")
	print("*****************************************************************\n\n")

	prompt=input("Enter appropriate command: \n")

	if prompt=="e":
		exit()
	elif prompt=="g":
		printTables(cursor)
	elif prompt=="gr":
		reading_table(cursor)
	elif prompt=="gi":
		get_intensity(cursor)
	elif prompt=="p":
		prog_table(cursor)
	else:
		get(cursor)

	initial_prompt(cursor,con)


def prog_table(cursor):

	print("*****************************************************************\n\n")
	print("a - Average Times")
	print("ai - Average Intensity Times")
	print("p - Percent Accomplished of Book")
	print("n - Number of readings left")
	print("nw - Number of weeks left")
	print("s - Summary")
	print("*****************************************************************\n\n")

	prompt=input("Enter appropriate command: \n")

	if prompt=="a":
		ave_time(cursor)
	elif prompt=="ai":
		ave_intensity_time(cursor)
	elif prompt=="p":
		percent(cursor)
	elif prompt=="n":
		number(cursor)
	elif  prompt=="nw":
		n_weeks()
	elif  prompt=="s":
		summary(cursor)

def ave_intensity_time(cursor):

	prompt=input("Enter in Format: [easy/med/hard]: \n")

	intensity_ave(cursor,prompt_map(prompt))


def intensity_ave(cursor,prompt):
	

	tot_time,n_readings=tot_intensity(cursor,prompt,"start_end")
	ave_study_time=mean_time(tot_time, n_readings)
	print(f"\nAverage Study time for {prompt.upper()} intensity: {ave_study_time}")

	tot_time,n_readings=tot_intensity(cursor,prompt,"read_time")
	ave_read_time=mean_time(tot_time, n_readings)
	print(f"\nAverage Read time for {prompt.upper()} intensity: {ave_read_time}")

	print("Average Total Reading and Studying Time: "+addTime(ave_read_time,ave_study_time))


def tot_intensity(cursor,prompt,table_name):

	tot_time="0 hr 0 mins"
	cursor.execute("SELECT time FROM "+table_name+" WHERE intensity=?",(prompt,))
	row=cursor.fetchone()
	n_readings=0

	while row!=None:

		tot_time=addTime(row[0],tot_time) 
		n_readings+=1
		row=cursor.fetchone()


	return tot_time,n_readings

def summary(cursor):

	done,left_book,left_total=n_readings(cursor)
	n_weeks=get_n_weeks([2020,4,12])
	print("END DATE: 12 April 2020")
	print(f"Readings/Week to finish BOOKS: {left_book/n_weeks}")
	print(f"Readings/Week to 'finish syllabus': {left_total/n_weeks}")
	

def get_n_weeks(date):

	final_week=datetime.date(date[0],date[1],date[2]).isocalendar()[1]
	current_date=[int(item) for item in str(datetime.datetime.now()).split(" ")[0].split("-")]
	current_week=datetime.date(2020,current_date[1],current_date[2]).isocalendar()[1]

	return final_week-current_week+1

def n_weeks():
	
	
	print(f"\nNumber of weeks left till April 12th 2020: {get_n_weeks([2020,4,12])}")


def n_readings(cursor):
	total_readings=81-16

	readings_done=sql_util.number_of_rows(cursor,"start_end","100")
	
	return readings_done,total_readings-readings_done,total_readings-readings_done+31

def number(cursor):

	done,left_book,left_total=n_readings(cursor)
	print("\nNumber of Readings Done: "+str(done))
	print(f"Number of Readings left in Book: {left_book}")
	print(f"Number of Readings left TOTAL: {left_total}")




def percent(cursor):

	prompt=input("Enter in Format: [Book Number]\n")

	getPercent(cursor,prompt)

def getPercent(cursor,book_n):

	cursor.execute("SELECT reading FROM start_end LIMIT 0,100")
	reading_done=[]
	bounds=getBounds(book_n)

	row=cursor.fetchone()

	while row!=None:
		if int(row[0])>=bounds[0] or int(row[0])<=bounds[1]:
			reading_done.append(int(row[0]))

		row=cursor.fetchone()

	displayPercent(reading_done,book_n,bounds)

def displayPercent(reading_done,book_n,bounds):

	output=[item for item in range(bounds[0],bounds[1]+1) if not item in reading_done]
	
	print("\nReadings NOT done: ")
	print(output)
	print(f"Percentage Accomplished of Book {str(book_n)} {(len(reading_done)/(len(reading_done)+len(output)))*100}%")
	


def getBounds(book_n):

	bounds={"1":"1 15","2":"16 36","3":"37 63","4":"64 81"}

	return [int(item) for item in bounds[book_n].split(" ")]

def ave_time(cursor):

	
	tot_time,n_readings=ave_table("start_end",cursor)
	mean_study_time=mean_time(tot_time,n_readings)
	print("Average Study Time: "+mean_study_time)

	tot_time,n_readings=ave_table("read_time",cursor)
	mean_read_time=mean_time(tot_time,n_readings)
	print("Average Reading Time: "+mean_read_time)

	print("Average Total Reading and Studying Time: "+addTime(mean_read_time,mean_study_time))


def ave_table(table_name,cursor):

	tot_time="0 hr 0 mins"
	cursor.execute("SELECT time FROM "+table_name+" LIMIT 0,100")
	row=cursor.fetchone()
	n_readings=0

	while row!=None:

		tot_time=addTime(row[0],tot_time) 
		n_readings+=1
		row=cursor.fetchone()


	return tot_time,n_readings

def mean_time(tot_time,n_readings):

	tot_time_list=tot_time.split(" ")

	mins=int(tot_time_list[2])+int(tot_time_list[0])*60

	ave_time=mins/n_readings
	hours=0

	if ave_time>=60:
		hours+=1
		ave_time-=60

	return str(hours)+" hr "+str(int(ave_time))+" mins\n"



def get_intensity(cursor):


	print("*****************************************************************\n\n")
	prompt=input("Enter in Format: [Reading Number]\n")

	# cursor.execute("SELECT intensity FROM intensity WHERE reading=?",(str(prompt),))

	print("Intensity for Reading Number "+str(prompt)+": "+sql_util.select_from_where(cursor,"intensity","intensity","reading",str(prompt))[0].upper())
	print("Number of pages: "+sql_util.select_from_where(cursor,"n_pages","intensity","reading",str(prompt))[0]+"\n")



def reading_table(cursor):

	"""
	FORMAT(given):
		- Date, Reading Number, Start Time, End Time, Time Taken
		- Reading number, Number of pages, Intensity

	FORMAT(wanted):
		- Reading Number, Time Taken, Intensity

	"""
	#Study table first:

	cursor.execute("SELECT reading,time FROM start_end LIMIT 0,100;")
	row=cursor.fetchone()
	output=[]
	temp=[] 

	while row!=None:
		temp.append(row[0])
		temp.append(row[1])

		output.append(temp)

		row=cursor.fetchone()
		temp=[]

	for i in range(len(output)):

		row=sql_util.select_from_where(cursor,"intensity","intensity","reading",output[i][0])
		if row!=None:
			output[i].append(row[0])


	print("\n#################################################")
	print("\nSTUDY TABLE\n")
	print("\nReading Number, Time Taken, Intensity\n")

	print_Format(output)
	print("#################################################\n")

	cursor.execute("SELECT reading,time FROM read_time LIMIT 0,100;")
	row=cursor.fetchone()
	output=[]
	temp=[] 

	while row!=None:
		temp.append(row[0])
		temp.append(row[1])

		output.append(temp)
		row=cursor.fetchone()
		temp=[]

	for i in range(len(output)):

		row=sql_util.select_from_where(cursor,"intensity","intensity","reading",output[i][0])
		if row!=None:
			output[i].append(row[0])


	print("#################################################")
	print("\nREADING TABLE\n")
	print("\nReading Number, Time Taken, Intensity\n")

	print_Format(output)
	print("#################################################\n")


def print_Format(output):

	"""
	PARAMETER:
		- Take output list and print it 
		- Output list is a list of lists

	"""

	for row in output:
		res=""
		for item in row: 
			res+=item+", "

		print(res)
	print("")

def update_row(cursor,prompt_list,datetime_list):

	start=sql_util.select_from_where(cursor,"start",map(prompt_list[0]),"reading",prompt_list[2])[0]

	if(check_pause(cursor,prompt_list)):

		#if i had paused it before and now i am ending it again, i will use the start time to get the timetaken and add
		#it with the timetaken before, hence getting the total time taken

		time_taken=sql_util.select_from_where(cursor,"time",map(prompt_list[0]),"reading",prompt_list[2])[0]
		total_time=addTime(time_taken,timeTaken(start,getTime()))
		cursor.execute("UPDATE "+map(prompt_list[0])+" SET time=? WHERE reading=?;",(total_time,prompt_list[2],))

	else:
		cursor.execute("UPDATE "+map(prompt_list[0])+" SET end=?,time=? WHERE reading=?;",(getTime(),timeTaken(start,getTime()),prompt_list[2],))

def addTime(a,b):

	a_split=a.split(" ")
	b_split=b.split(" ")

	hours=int(a_split[0])+int(b_split[0])
	mins=int(a_split[2])+int(b_split[2])

	if mins>=60:
		hours+=1
		mins-=60

	return str(hours)+" hr "+str(mins)+" mins"

def printTables(cursor):

	print("\n\nSTUDY TIMINGS TABLE: \n")
	print("Date, Reading Number, Start Time, End Time, Time Taken\n")

	sql_util.print_table(cursor,"start_end","1000")
	print("\n\n")
	print("READING TIMINGS TABLE: \n")
	print("Date,Reading Number, Start Time, End Time, Time Taken\n")

	sql_util.print_table(cursor,"read_time","1000")

	print("\n\nINTENSITY TABLE: \n")
	print("Reading Number, Number of pages, Intensity,\n")

	sql_util.print_table(cursor,"intensity","1000")

	# cursor.execute(r"SELECT * FROM intensity WHERE reading=?",str(1))
	# row=cursor.fetchone()
	# print(row.keys)	

def getDateTime():

	return str(datetime.datetime.now()).split(" ")


def timeTaken(start,end):

	start_list=start.split(":")
	end_list=end.split(":")

	time_taken=(int(end_list[0])*60+int(end_list[1]))-(int(start_list[0])*60+int(start_list[1]))

	hours=0

	while time_taken>=60:
		hours+=1
		time_taken-=60


	return str(hours)+" hr "+str(time_taken)+" mins"





if __name__ == '__main__':
	main()

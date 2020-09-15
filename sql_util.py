import os 
import sqlite3
import datetime

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
			LIMIT
			ORDER BY
			AND



	Order:
		- "ORDER BY" [col name] 
			- Sorted in ascending by default
			- sort by descending instead by appending DESC:
				- ORDER BY [col-name] DESC


	Filter:
		- Use "WHERE" and logic impliers:
			- >;  - or; 
			- <;  - and;

	PRINT:

		- Use LIMIT to print rows, 
		- Upper bound must be the number of rows the table has, else the table will start printing
		  from the top again
		- cursor is now an iterable object,
		  do rows=cursor.fetchone() to get the next row

			EG: cursor.execute(r'SELECT * FROM [table_name] LIMIT 0,100')
				rows=cursor.fetchone()


	NATURAL JOIN:
		- To combine tables based on an implicitly realized relationship amongst colums of tables

		==> Selecting from multiple tables:
			- Example: 
				where, table names: products, order_contents, orders

				SELECT orderDate name, customerLastName, customerFirstName FROM products NATURAL JOIN order_contents NATURAL JOIN orders ORDER BY customerLastName;	 

	Classes<=>columns:

		- Use DOT notation to derefence colums of tables when dealing with mutiple tables
			- TO avoid confusion where columns may share similar names
			- Therefore [table name].[column name]


	IN:
		Use for filtering results, can use this keyword as such:
			- select .. from ... where ... in(....)

	DISTINCT: 
		- Used for filtering out DUPLICATES!!!

		SELECT DISTINCT firstName,lastName FROM students natural join grades where grades<=70;
		<=> SELECT firstName,lastName FROM students WHERE vnum IN(SELECT vnum FROM grades WHERE grade<70);
"""
def create_row(cursor,table_name,values):

	"""
	PARAMETERS:
		- cursor 
		- table_name:
			- Type: String
		-Values:
			- Type: TUPLE
			- Description: List contains all the values to add(where # of values match the number of cols)


	"""

	execute_stm="INSERT INTO "+table_name+" VALUES("

	for i in range(len(values)):

		if i==len(values)-1:
			execute_stm+="?);"
		else:
			execute_stm+="?,"


	cursor.execute(execute_stm,values)
	cursor.commit()


def delete_row(cursor,table_name,col_name,where_var):

	"""
	PARAMETERS:
		- table_name, type: String
		- where_var, type:String

	OUTPUT:
		- Executes delete row via sql

	"""	
	execute_stm="DELETE FROM "+table_name+" WHERE "+col_name+"='"+where_var+"';"
	cursor.execute(execute_stm)


def close(con):

	"""
	PARAMETERS:
		- Connection object

	RETURN:
		- Commits and closes connection
	"""
	con.commit()
	con.close()
def create_table(cursor,table_name,params):

	"""
	PARAMETERS:
		- Assumes item in params is as such '[header name] [type]...'
		- Assumes table_name is a string
	Takes a list of params(table headers),uses cursor to create table

	ASSUMPTIONS:
		Assumes that the exception to be thrown is 'TABLE EXISTS' by SQL"""

	execute_stm=r"CREATE TABLE "+table_name+" ("

	i=0
	for i in range(len(params)):

		if i==len(params)-1:
			execute_stm+=params[i]+" );"
		else:
			execute_stm+=params[i]+","


	try:
		cursor.execute(execute_stm)
	except:
		return


def create_cursor_con(file_name):

	"""connects to file(with file name) and creates cursor"""

	con=sqlite3.connect(file_name)
	return con.cursor(),con


def move_tables(ipdb,opdb,table_name):

	"""
	INCOMPLETE!!! 

	PARAMETERS:
		-ipdb, type: input db file, String
		-opdb, type: output db file, String
		-table_name, type: String

	RETURN:
		-Transfers table(table_name) from ipdb to opdb"""

	ip_cursor=create_cursor(ipdb)
	op_cursor=create_cursor(opdb)

	ip_cursor.execute("SELECT * FROM ")

def number_of_rows(cursor,table_name,n_rows):

	execute_stm=r"SELECT * FROM "+table_name+" LIMIT 0,"+n_rows

	cursor.execute(execute_stm)
	row=cursor.fetchone()
	number_rows=0
	while(row!=None):

		number_rows+=1
		row=cursor.fetchone()

	return number_rows

def print_table(cursor,table_name,n_rows):
	"""
	PARAMETERS:
		cursor, type: cursor object
		table_name, type: string
		n_rows, type: string

	"""

	execute_stm=r"SELECT * FROM "+table_name+" LIMIT 0,"+n_rows

	cursor.execute(execute_stm)
	row=cursor.fetchone()

	while(row!=None):

		print(row)
		row=cursor.fetchone()


def select_from_where(cursor,col,table_name,where_var,where_args):

	"""
	PARAMETERS:
		- All are strings

	RETURNS:
		cursor.fetchone() {a tuple}
	"""

	cursor.execute("SELECT "+col+" FROM "+table_name+" WHERE "+where_var+"=?",(where_args,))
	return cursor.fetchone()

def getDateTime():

	"""
	PARAMETERS: NONE

	OUTPUT: Used by getDate and getTime
	"""

	return str(datetime.datetime.now()).split(" ")

def getTime():

	return getDateTime()[1].split(".")[0]

def getDate():

	return getDateTime()[0]

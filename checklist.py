import os 
import sys 


def main():

	r_list=[]
	create_reading_list(r_list)
	action_menu()

	process_input(r_list)


def process_input(r_list):

	prompt=input("\nEnter Appropriate action: \n")

	if prompt=="q":
		exit()

	elif(prompt=="r"):
		remove_reading(r_list)

	elif(prompt=="g"):
		print_list(r_list)

	process_input(r_list)




def create_reading_list(list_of_readings):


	if("readings_left.txt" in os.listdir()):

		with open("readings_left.txt","r") as op:
			get_list(list_of_readings,op)

	else:
		#First run
		with open("readings_left.txt","w") as op:
			write_and_append(list_of_readings,op)
			


def get_list(r_list,op):

	for line in op:
		line_split=line.split("\n")
		r_list.append(line_split[0])

def write_and_append(list_of_readings,op):

	for i in range(1,82):
		op.write(str(i)+"\n")
		list_of_readings.append(i)

def action_menu():

	print("**********************************************************\n")
	print("q - Quit")
	print("r- remove_reading")
	print("g - Get readings left")
	print("**********************************************************\n")

def remove_reading(r_list):

	prompt=input("Reading to remove or anomaly to add/remove: \n")
	if prompt=="q":
		exit()
	elif prompt=="g":
		print_list(r_list)
	elif prompt=="ga":
		get_anomalies()
	elif prompt.split(" ")[0]=="r":
		rm_anomaly(prompt)
	elif prompt.split(" ")[0]=="a":
		add_anomaly(prompt)
	elif prompt=="diff":
		get_diff_count(r_list)
	elif prompt=="menu":
		print_rm_menu()
	else:
		r_list.remove(prompt)
		remove_from_file(prompt,r_list)

	remove_reading(r_list)

def print_rm_menu():

	print("**********************************************************\n")
	print("q -Quit")
	print("g - Get readings left")
	print("ga - Get Anomalies list")
	print("r [s?r?] - remove Anomaly [s?r?]")
	print("a [s?r?] - add Anomaly [s?r?]")
	print("diff - Get length differences")
	print("menu - get THIS menu")
	print("**********************************************************\n")

def get_anomalies():

	with open("anomaly.txt","r") as ip:

		for line in ip:
			print(line.split("\n")[0])
def get_diff_count(r_list):

	r_count=len(r_list)
	anomaly_count=0

	with open("anomaly.txt","r") as ip:
		anomaly_count=len(ip.readlines())

	print(f"Anomaly Count: {anomaly_count}")
	print(f"R Count: {r_count}")
	print(f"Difference is {anomaly_count-r_count}\n")


def add_anomaly(prompt):

	with open("anomaly.txt","a") as op:
		op.write(prompt.split(" ")[1]+"\n")

def rm_anomaly(prompt):

	with open("anomaly.txt","r") as ip:
		anomaly_lines=ip.readlines()

	os.remove("anomaly.txt")

	with open("anomaly.txt","w") as op:

		for line in anomaly_lines:
			if(line.split("\n")[0]!=prompt.split(" ")[1]):
				op.write(line)

		 
def remove_from_file(prompt,r_list):

	os.remove("readings_left.txt")

	with open("readings_left.txt","w") as op:
		
		for item in r_list:
			op.write(str(item)+"\n")


def print_list(r_list):
	print(r_list)


if __name__ == '__main__':
	main()
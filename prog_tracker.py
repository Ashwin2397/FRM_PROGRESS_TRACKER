import os 
import sys 
import datetime


constants={"aim date ideal":"2nd April 2020","aim date technical":"30th March 2020","latest date":"16th April 2020","FRM exam date":"16th May 2020"}


def main():

	print("\nWelcome to FRM Progress Tracker!\n")

	print("**********************************************************\n")
	print("q - Quit")
	print("s - Store Readings")
	print("g - Get")
	print("**********************************************************\n")

	prompt=input("Please key in appropriate action:\n")


	

	action_required(prompt)


def initial_action(prompt):

	"""Takes in prompt(a string) and pass control to the appropriate function"""

def get_action(prompt):

	"""Takes in get prompt(a string) and passes control to the appropriate function"""

def get_action(prompt):

	"""Takes in store prompt(a string) and passes control to the appropriate function"""

def get_menu():
	"""Prints get menu"""
	print("**********************************************************\n")
	print("  q - Quit")
	print("  p - Percentage accomplished")
	print("  pr - Projected Date")
	print("  rl - Readings left")
	print("  a - Aim Date")
	print("  pr - Proportion of book accomplished")
	print("  n -Number of readings to do per day to get back on track\n")
	print("**********************************************************\n")

	prompt=input("Please key in appropriate action:\n")

def store_menu():
		
	"""Prints store action menu"""

	print("**********************************************************\n")
	print("q - Quit")
	print("")
	print("")
	print("")

	print("**********************************************************\n")


def getTime():
	
	return str(datetime.now()).split(" ")[1]


def getDate():

	return str(datetime.now()).split(" ")[0]

def percent(file):
	"""Returns percentage accomplished"""

def projected_date(file):
	"""Returns the projected completed date"""

def readings_left(file):
	"""Returns the number of readings left"""

def aim_date(file):
	"""Returns the aim date(technical,ideal and latest)"""

def prop_book(file):
	"""Returns the proportion of all books completed"""

def get_back_on_track(file):
	"""Returns number of readings per day to get back on track"""	






if __name__ == '__main__':
	main()
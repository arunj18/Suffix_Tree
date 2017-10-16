##########################################################################################
# Author: Arun John 16-Nov-2017                                                          #
##########################################################################################
#											 #
##########################################################################################
# Notes: 										 #
#	1. The search() method and first_occur() methods do not support more than one 	 #
#          word and only accepts lower case input without any punctuations. No error     #
#	   handling has been done right now but will be implemented in the future for    #
#	   both these methods. In the future, these methods may also support searching   #
#	   for a string instead of only a word. 					 #
#											 #
#	2. The rel() method also takes inputs only in lower case and without any 	 #
#	   punctuation. Error handling for this method is also not implemented yet and   #
#	   may be done in the future.							 #
#											 #
#	3. Comments will also be added in methods in the future to better explain what   #
#	   is happening in each of the methods and suggestions for better performance.	 #
#											 #
##########################################################################################
import sys
if(sys.version_info[0] < 3):
	raise "Python 3 required"
del sys
import data_clean as dc
import classes as cl
import copy
import os
clean_data,results_data=dc.get_data()
print(dc.verify_data(clean_data))
working_data=copy.deepcopy(clean_data)
del copy
del dc
Tree=cl.GStree(working_data)
while(True):
	print("----Suffix Tree----".center(os.get_terminal_size().columns))
	print("1. Single Word Search")
	print("2. First Occurence Single Word")
	print("3. Relevant Search")
	print("4. Exit")
	print("Choose an option: ",end = ' ')
	option=input()
	try:
		option=int(option)
		if(option==1):
			print("Enter a word to search: ")
			query=input()
			Tree.search(query)
		elif(option==2):
			print("Enter a word to search: ")
			query=input()
			Tree.first_occur(query)
		elif(option==3):
			print("Enter a string to search: ")
			query=input()
			Tree.search(query)
		elif(option==4):
			raise SystemExit
		else:
			print("Invalid option")
	except ValueError:
		option=option.lower()
		if("search" in option):
			if("relevant" in option):
				print("Enter a string to search: ")
				query=input()
				Tree.rel(query)
			elif("single" in option or "word" in option):
				print("Enter a word to search: ")
				query=input()
				Tree.search(query)
			else:
				print("Invalid option")
		elif("relevant" in option):
			print("Enter a string to search")
			query=input()
			Tree.rel(query)
		elif("first" in option or "occurence" in option):
			print("Enter a word to search: ")
			query=input()
			Tree.first_occur(query)
		elif("quit" in option or "exit" in option):
			raise SystemExit
		else:
			print("Invalid option")

##########################################################################################
	

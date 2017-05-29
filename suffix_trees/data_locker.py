#!/usr/bin/python3.5

"""	
	Proper Syntax:
	--------------
	Usage 1		:	./deduplicator [store|get|delete] -file [file1 file2 ...] -locker [locker]
	Usage 2		: 	./deduplicator [list] -locker [locker]

	Return Codes for the CLI:
	-------------------------

	0	:	Program ran successfully
	1	:	Syntax error for running deduplicator
	2	:	Locker not found in this directory
	3	:	File NOT found 
"""

from suffix_tree import SuffixTree 	# Main data structure
import glob 						# Used to find all files in a directory
import sys 							# used for getting command line args
import os							# used to look for files in a directory
import pickle 						# can be used to save a data struct to a file


#=====================================================================
#							  Functions
#=====================================================================
def parse_cmd_line(argv):
	# Vars
	inputSize = len(argv)
	files = []
	locker = ''

	# User command
	command = ''
	allowed_commands = ['store','get','delete','list']
	
	# Input asrguments
	min_num_args = 6
	flags = {'first':'-file',
		 	'second':'-locker'}

	#------------------------------------Basics--------------------------------------
	
	# The first argument should always be the program command
	if (inputSize >= 2):
		command = argv[1]
	else:
		raise ValueError

	# If the command is invalid, then return 
	if command not in allowed_commands:
		raise SyntaxError

	#-------------------------------------List---------------------------------------
	
	if (command.__eq__('list')):
		# should only have 4 inputs
		if (inputSize is 4 and argv[2].__eq__(flags['second'])):
			
			# remove any path so locker must be placed in current directory
			locker = argv[3].split('/')
			
			# Locker name is last in the split list
			if (locker[-1].__eq__('')):
				# User eneded locker name with /
				locker = locker[-2]
			else:
				# User did not end locker name with /
				locker = locker[-1]

			return (command, None, locker)
		else:
			raise SyntaxError

	#--------------------------------store|get|delete---------------------------------

	# Error check for the wrong number of inputs when not listing files in locker
	if (inputSize < min_num_args):
		raise ValueError

	# Determine how many files were passed 
	for i in range(2,inputSize):
		if (argv[i].__eq__(flags['first'])):
			i += 1

			# Add files to the list while we havent arrived to the next flag
			while (not argv[i].__eq__(flags['second'])):
				files.append(argv[i])
				i += 1

				# if we are stuck in this loop then raise a flag
				if (i > inputSize-1):

					# None of the flags were found 
					raise SyntaxError

			# If everything was correct, then take the last input as the locker name and path
			if (i+1 <= inputSize-1):
				locker = argv[i+1].split('/')
			else:	
				raise SyntaxError

			# Locker name is last in the split list
			if (locker[-1].__eq__('')):
				# User eneded locker name with /
				locker = locker[-2]
			else:
				# User did not end locker name with /
				locker = locker[-1]

			break

	#------------------------------------Return--------------------------------------

	# If any of the three components are NULL then raise an ERROR
	if (not locker or not command or not files):
		raise SyntaxError

	else:	
		# Return the extracted information to the main loop
		return (command,files,locker)


def move_files_to_locker(fileList, locker):
	# We need to place the files into the locker
	destination = './'+locker+'/'

	# List of files currently within /deduplicator
	files = os.listdir('./')
	
	# Test that each file is within deduplicator
	for file in fileList:
		if file not in files:
			raise ValueError(3, "Error: File not found in current directory.")
		else:
			# Create the directory if it does not exist
			if (not os.path.exists(destination)):
				os.mkdir(destination)

			# The file is in the deduplicator and we need to move it into ./locker
			os.rename(file, destination+file)

	return 

def delete_locker_files(fileList, locker):
	# Search within the locker
	path = './'+locker+'/'

	# Check to see if the locker exists
	if (not os.path.exists(path)):
		raise ValueError(2, "Error: Locker not found in this directory.")

	# Files to be deleted
	files = os.listdir(path)

	# Make sure the file exists
	for file in fileList:
		if file not in files:
			raise ValueError(3, "Error: File not found in locker.")
		else:
			# Delete the file from the locker
			os.remove(path+file)

	return


def get_locker_contents(fileList,locker):
	# We need to place the file into deduplicator
	destination = './'

	# Path to the files in the locker
	path = './'+locker+'/'

	# Check to see if the locker exists
	if (not os.path.exists(path)):
		raise ValueError(2, "Error: Locker not found in this directory.")
	
	# List of files currently in the locker
	files = os.listdir(path)
	
	# Test that each file is within the locker
	for file in fileList:
		if file not in files:
			raise ValueError(3, "Error: File not found in locker.")
		else:
			# The file is in the locker and we need to move it back into ../deduplicator
			os.rename(path+file, destination+file)
	
	return


def list_locker_contents(locker):
	# We need to search within the locker
	path = './'+locker

	# Check to see if the locker exists
	if (not os.path.exists(path)):
		raise ValueError(2, "Error: Locker not found in this directory.")

	# Current files held in the locker
	files = os.listdir(path)

	# Sort by name
	files = sorted(files)

	# display
	for file in files:
		print(file)

	return


def main():
	try:
		# Get the command line data from the user
		(command,fileList,locker) = parse_cmd_line(sys.argv) 

	except(ValueError, SyntaxError) as e:

		# Most likely a syntax error 
		print("Usage 1: ./deduplicator [store|get|delete] -file [file1 file2 ...] -locker [locker]")
		print("Usage 2: ./deduplicator [list] -locker [locker]")

		# Error value
		return 1

	else:

		try:
			if (command.__eq__('store')):

				# Place the new files into the locker
				move_files_to_locker(fileList, locker)

			elif (command.__eq__('delete')):

				# Remove the files from the locker 
				delete_locker_files(fileList, locker)

			elif (command.__eq__('get')):

				# Extract files from the locker back into deduplicator
				get_locker_contents(fileList,locker)

			elif (command.__eq__('list')):

				# List all of the files currently in the locker
				list_locker_contents(locker)

		except Exception as e:

			# handle any errors which may have occured above
			print(e.args[1])
			
			# Error value
			return e.args[0]


#=====================================================================
#								Main
#=====================================================================
if __name__ == '__main__':
	sys.exit(main())



"""
	Suffix Tree Material:
	---------------------

	def build_tree(locker):
		fileTrees = {} # dictionary <file-name> : <tree>
		lockerFiles = glob.glob('./'+locker+'/f*'); # contained within the locker?
		for file in lockerFiles:
			with open(file) as F:
				for line in F:
					fileTrees[file] = SuffixTree(line) # build the tree for each file
		return fileTrees


	def save_data_Structure(fileTrees,locker):
		path  = './'+locker+'/saved_trees.txt'
		storage_file = open(path,'wb')
		pickle.dump(fileTrees, storage_file) # save the data structure to a file
		storage_file.close() 
		fileTrees = build_tree(locker)
		
	# implementation 
	for tree in fileTrees:
		print(fileTrees[tree].find_substring('ban')) # print the index of the substring in each of the files
	
	save_data_Structure(fileTrees,locker)
"""

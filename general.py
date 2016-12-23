#!/usr/bin/python3.5

import os

def create_folder(directory):
	if not os.path.exists(directory):
		print("Creating Folder " + directory)
		os.makedirs(directory)


#create list of files which are crawled and which are not

def create_list(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'

	if not os.path.isfile(queue):
		write_file(queue,base_url)
	if not os.path.isfile(crawled):
		write_file(crawled,'')


#create new file
def write_file(path, data):
	with open(path, 'w') as f:
		f.write(data)

#Append data to the file
def append_to_file(path, data):
	with open(path,'a') as file:
		file.write(data + '\n')

#delete the contents of the file
def delet_file_contents(path):
	with open(path,'w') as file:
		pass


#copy the contents from file to set
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as file:
		for line in file:
			results.add(line.rstrip())
	return results


#copy from set to file
def set_to_file(links, file):
	with open(file,"w") as f:
		for l in sorted(links):
			f.write(l+"\n")




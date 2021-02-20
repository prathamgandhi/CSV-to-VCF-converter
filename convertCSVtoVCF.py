#This code has been licensed under GNU GPLv3 License Agreement.

import csv	#Imports a csv library that makes it easier to parse CSV files.

with open('ContactList.csv') as read_file:	#Opens a file named "ContactList.csv" assumed to be present within the same folder.
	csv_reader = csv.reader(read_file, delimiter=',')	#Parsed the csv file
	with open('ContactList.vcf', 'w') as write_file:	#Opens a file named "ContactList.vcf" for write purposes, creates a file if not already present in the same folder.
		for row in csv_reader:
			write_file.write('BEGIN:VCARD\n')
			write_file.write('VERSION:2.1\n')
			write_file.write(f'N:{row[1]};{row[0]}\n')
			write_file.write(f'FN:{row[0]} {row[1]}\n')
			write_file.write(f'TEL;CELL:{row[2]}\n')
			write_file.write('END:VCARD\n')
			
			
'''
The CSV file is assumed to have the following structure:
First Name, Last Name, Telephone Number (Cell)
Pratham, Gandhi, ##########
John, Snow, ##########
......


If you wish to include more data in the vcf file like email-id, designation, etc, make a csv file containing that information in a particular order.
For the format of the vcf file follow : https://en.wikipedia.org/wiki/VCard#Example_of_vCard_files
Written by Pratham Gandhi.
'''





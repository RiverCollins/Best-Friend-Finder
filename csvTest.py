import csv



def write_to_file():

	f = open('chaz.csv' , 'wt')
	try:
		writer = csv.writer(f)
		writer.writerow(('Title 1' ,  'Title 2', 'Title 3'))
		i = 2
		for i in range(10):
			writer.writerow(('River', 'Collins', i))
	finally:
		f.close()

	#print (open('test.csv', 'rt').read())



def read_in_file():
	f = open('chaz.csv', 'rt')
	try:
		reader = csv.reader(f)
		for row in reader:
			print(row)
	finally:
		f.close()



write_to_file()
read_in_file()
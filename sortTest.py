import csv

with open("fanchazstic.csv","r") as fh:
  reader = csv.reader(fh, delimiter = ',')
  sort = sorted(reader, key=lambda x: int(x[1]), reverse=True)
  print(sort)
  

with open("fanchazstic.csv","r") as fh:
	reader = csv.reader(fh, delimiter = ',')
	row_count = sum(1 for row in reader)
	print(row_count)

'''
f = open('fanchazstic.csv', 'r')
reader = csv.reader(f, delimiter = ',')
row_count = sum(1 for row in reader)
print(row_count)
sort = sorted(reader, key=lambda x: int(x[1]), reverse=True)
print(sort)
f.close()
'''
f = open('fanchazsticSorted.csv' , 'w', newline = '')
print('yes')
try:
	print('yess')
	writer = csv.writer(f)
	i = 0
	for i in range(row_count):
		writer.writerow(sort[i])
finally:
	f.close()

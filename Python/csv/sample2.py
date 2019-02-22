import csv

with open('employee_file2.csv', mode='w') as csv_file:
	names = ['emp_name', 'dept', 'birth_month']
	writer = csv.DictWriter(csv_file, fieldnames=names)
	writer.writeheader()
	writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
	writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
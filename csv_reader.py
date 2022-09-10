import csv
person_file = open('person.csv','r')

csvFile = csv.reader(person_file)


csvFile = csv.DictReader(person_file)

line = 0

for lines in csvFile:
     line = line + 1
     print("line: {}".format(line))
     print(lines)
     print(type(lines))

    # if lines['Age'] == '15':
        #print('Name:', lines['Name'])

     print('Profession:', lines['Profession'])
     print('Age:', lines['Age'])

    # print('Profession:', lines[2])
     #print('Profession:', lines[])




# # importing the csv module

import csv
from datetime import datetime

# # field names
# columns = ['roll', 'name', 'class','date']
# #
# # # name of csv file
# filename = "student.csv"
# #
# students = [
#     {'roll': 5, 'name': 'Alif', 'class': 9, 'date': datetime.now()},
#     {'roll': 10, 'name': 'Lima', 'class': 10, 'date': datetime.now()},
#     {'roll': 2, 'name': 'Ripa', 'class': 5, 'date': datetime.now()}
#]
#
# writing to csv file
# with open(filename, 'w') as csvfile:
#     # creating a csv dict writer object
#     writer = csv.DictWriter(csvfile,  columns)
#
#     # writing headers (field names)
#     writer.writeheader()
#
#     # writing data rows
#      writer.writerow()
#     # writer.writerows(students)
#     for s in students:
#        writer.writerow({s})
#       # writer.writerow({'roll': 2, 'name': 'Ripa', 'class': 5, 'date': datetime.now()})
#
#

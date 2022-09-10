import csv
from os.path import exists

class Student:
    def __init__(self):
        self.filename = "student_db.csv"

    def insert_student(self):

        name = input('enter name : ')
        roll = input('enter roll : ')
        age = input('enter age : ')

        columns = ['name', 'roll', 'age']

        is_file_exist = exists(self.filename)
        # writing to csv file
        with open(self.filename, 'a') as file:

            csv_writer = csv.DictWriter(file, columns)

            if not is_file_exist:
                csv_writer.writeheader()

            csv_writer.writerow({'roll': roll, 'name': name, 'age': age})

    def find_student(self, name):

        with open(self.filename, 'r') as file:
            csv_reader = csv.DictReader(file)

            student=None
            for lines in csv_reader:
                if lines['name'] == name:
                    student = lines

            if student:
                print('found student :', student)
            else:
                print("Student {} not found!".format(name))


    def print_students(self):

        with open(self.filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for lines in csv_reader:
                #print all student here from csv
                print('students :', lines)



while True:
    command = input("Please enter command, \nPress 1 for insert \n2 for find \n3 for list of students \n4 to exit \n>>")
    obj_student = Student()
    if command == '1':
        obj_student.insert_student()
    elif command == '2':
        name  = input("Enter student name: \n>")
        obj_student.find_student(name)
    elif command == '3':
     obj_student.print_students()
    elif command == '4':
     break




#To make executable file run bellow command
#pyinstaller --onefile student_db.py
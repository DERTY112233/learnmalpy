#!/bin/python3

class students:
    numofstudents = 0
    def __init__(self,  fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

        students.numofstudents += 1

    def fullname(self):
        print(self.fname + ' ' + self.lname)




stu1 = students('joyien', 'noscope', "jojonoscope22@gmail.com")
stu2 = students('DERTY', 'boi', "dertiboi8080@gmail.com")

print(students.numofstudents)

students.fullname(stu1)


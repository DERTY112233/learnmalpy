#!/bin/python3

class students:
    def __init__(self,  fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email
    def fullname(self):
        print(self.fname + ' ' + self.lname)




stu1 = students('Joel', 'Paiva', "joelpaiva112233@gmail.com")
stu2 = students('Storm', 'Paiva', "stormiboi8080@gmail.com")

stu1.fullname()


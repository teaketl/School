"""
File name: adminClass.py
Purpose: Child of User Class
Author: Teagan Holmes
Create date: 11/8/2023
Last update date:11/8/2023
version: 1.1
"""
from userClass import User;


class Admin(User):
    department = "";
    studentList = [];
    def __init__(self, fn="", ln="", us="", p="", bd="", pm="", d="",sl=None): #teacher fn/ln
        super().__init__(fn, ln, us, p, bd, pm); #teacher fn/ln
        self.department = d
        self.studentList = sl
        if sl is None:
            self.studentList = []
        else:
            self.studentList = sl

    #str method
    def __str__(self):
        return "Admin - Name: " + self.firstName + " " + self.lastName  + " " + "Username: " + self.username + " " + "Birthday: " + self.birthday + " " + "Permission: " + self.permission + " " + "Department: " + self.department + " " + "Student List: " + str(self.studentList);

    #setters
    def setDepartment(s, d):
        s.department = d
    def setStudentList(s, sl):
        s.studentList = sl;

    #getters
    def getDepartment(s):
        return s.department
    def getStudentList(s):
        for sl in s.studentList:
            print(sl.firstName + " " + sl.lastName);
#extra methods
    def addStudent(s, sl):
        if sl not in s.studentList:
            s.studentList.append(sl);
    def removeStudent(s, sl):
        if sl in s.studentList:
            s.studentList.remove(sl);

"""
File name: canvas.py
Purpose: login screen for canvas project
Author: Teagan Holmes
Create date: 11/8/2023
Last update date:11/28/2023
version: 1.1
"""
import utility;
import adminUtility;
import studentUtility;
from studentClass import Student;


loginScreen = input("Enter 1 to enter Admin login or 2 to enter Student login:\n");


if loginScreen == '1':
    try:
        admin = open('adminLogin.csv','r');
        readAdmin = utility.readCSV(admin)
        adminSignIn = adminUtility.login(readAdmin);
        if adminSignIn == True:
            adminUtility.adminOptions();
        else:
            print("Invalid signin")
    except:
        FileNotFoundError

if loginScreen == '2':
    try:
        student = open('studentInfo.csv','r')
        readStudent = utility.readCSV(student)
        studentSignIn = studentUtility.login(readStudent);
        if studentSignIn == True:
            Student.studentOptions('');
        else:
            print("Not a valid option!")
    except:
        FileNotFoundError;
        print("No students added.")



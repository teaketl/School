"""
File name: adminUtility.py
Purpose: Child of User Class
Author: Teagan Holmes
Create date: 11/8/2023
Last update date:11/28/2023
version: 1.1
"""
import utility;
from adminClass import Admin;
from studentClass import Student;
import os.path;

def login(signInCSV):
    for tries in range(6):
        username = input("Enter a username:\n");
        password = input("Enter a password:\n");
        if tries == 5:
            print("too many tries!");
            exit();
        else:
            for person in signInCSV:
                if person[0] == username and person[1] == password:
                    return True;

def adminOptions():
    for tries in range(5): # keep asking
        options = input("Choose one of the following:\n1. Add Student 2. Add Course 3. Add Course Enrollment\n 4. See All Student Info 5. See All Course Information 6. See all Enrollment Info 7. Logout\n")
        if options == '1':
            addStudentID = input("Enter Student ID Number:\n");
            addStudentFN = input("Enter Student Info.\nEnter a First Name:");
            addStudentLN = input("Enter Last Name:\n");
            addStudentUsername = input("Enter a Username:\n");
            addStudentPassword = input("Enter a Password:\n");
            addPermission = input("Enter Permission (Student or Admin):\n");
            addBirthday = input("Enter a birthday:\n");
            addStudentMajor = input("Enter a Major:\n");
            addStudentGrade = input("Enter a Grade:\n");
            addStudentGPA = input("Enter a GPA:\n");
            studentInfoFile = 'studentInfo.csv';
            studentLoginFile = 'studentLogins.csv'; #add user and pass to logins
            userAndPass = [addStudentUsername,addStudentPassword];
            studentHeaders = ["Student ID","First Name","Last Name", "Username","Password","Permission","Birthday","Major","Grade","GPA","Courses"]
            if os.path.isfile(studentInfoFile) is True: #make sure file exists if so read
                openStudentInfo = open('studentInfo.csv','r');
                studentInfo = utility.readCSV(openStudentInfo);
                if addStudentID == studentInfo[0]: #must be unique id number
                    print("Enter a different ID number.");
                else:
                    newStudent = [addStudentID,addStudentFN,addStudentLN,addStudentUsername,addStudentPassword,addPermission,addBirthday,addStudentMajor,addStudentGrade,addStudentGPA]
                    print("Successfully added new student!");
                    utility.appendCSV(studentInfoFile, newStudent);
            else:
                print("Student successfully added!");
                utility.appendCSV(studentInfoFile, studentHeaders);
                utility.appendCSV(studentInfoFile, newStudent);
                utility.appendCSV(studentLoginFile, userAndPass);

        if options == '2': #ADD COURSE ENROLLMENT OPTION
            addCourseNumber = input("Add Course Enrollment.\nEnter a Course Number:");
            addCourseName = input("Add Course Name:\n");
            courseList = [addCourseNumber,addCourseName] #goes into appendCSV function
            courseFile = 'courses.csv';
            courseHeaders = ["Course Name","Course Number","Student List"];
            if os.path.isfile(courseFile) is True:
                readCourseInfo = open('courses.csv','r');
                courses = utility.readCSV(readCourseInfo);
                if courses[0] == addCourseNumber or courses[1] == addCourseName: #check against number (index 1) and name (index 2)
                    print("Conflicting course name or number.");
                else:
                    utility.appendCSV(courseFile, courseList) #if not wrong, append
            else:
                print("Created new file and added course name and number!"); #friendly user message
                utility.appendCSV(courseFile, courseHeaders); #add headers only if new file
                utility.appendCSV(courseFile, courseList); #append course name and #

        if options == '3': #ENROLL STUDENT
            enrollStudent = input("Enter a Student ID to enroll them in a course:\n");
            courseNumber = input("Enter a Course Number:\n");
            courseName = input("Enter a Course Name:\n");
            courseHeaders = ["Course Number","Course Name"]
            enrollment = [courseNumber,courseName];
            enrollFile = 'studentInfo.csv';
            if os.path.isfile(enrollFile) is True:
                if enrollStudent == studentInfo[0]:
                    if courseNumber == courses[0] and courseName == courses[1]:
                        utility.appendCSV(enrollFile, enrollment);
                    else:
                        print("Not a course.");
                else:
                    print("Not a Student");
            else:
                print("Added new enrollment");
                utility.appendCSV(enrollFile, courseHeaders);
                utility.appendCSV(enrollFile, enrollment);


        if options == '4': #SEE ALL STUDENTS
            try:
                openStudentInfo = open('studentInfo.csv', 'r');
                readStudentInfo = utility.readCSV(openStudentInfo);
                for row in readStudentInfo:
                    print(row);
            except:
                FileNotFoundError;
                print("You haven't added any students yet!"); #gotta add a first student dude


        if options == '5': #PRINT ALL COURSE ENROLLMENT
            try:
                openCourseCSV = open('courses.csv', 'r');
                courseInfo = utility.readCSV(openCourseCSV);
                for row in courseInfo:
                    print(row);
            except:
                FileNotFoundError;
                print("You haven't added any courses yet!");


        if options == '6': #PRINT ALL ENROLLMENT
            try:
                openStudentInfoAgain = open('studentInfo.csv','r');
                readStudentInfo = utility.readCSV(openStudentInfoAgain);
                for i in readStudentInfo:
                    firstRows = readStudentInfo[i][-1]
                    print(firstRows); #read and print enrollment
            except:
                FileNotFoundError;
                print("You haven't added any students!");

        if options == '7':
            return;
        else:
            print("Enter a menu option!");

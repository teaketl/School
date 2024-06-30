"""
File name: courseClass.py
Purpose: course class
Author: Teagan Holmes
Create date: 11/2/2023
Last update date:11/5/2023
version: 1.1
"""

class Course: #inhereites from student class
    courseName = "";
    courseNumber = "";
    studentList = []; #split by comma # student should be from student then can pull age, birthday etc

    def __init__(self, cnam="",cnum="",sl=None):
        self.courseName = cnam
        self.courseNumber = cnum
        self.studentList = sl
        if sl is None:
            self.studentList = []
        else:
            self.studentList = sl

    def __str__(self):
        return "Course - Course Name: " + self.courseName + " " + "Course Number: " + self.courseNumber + " " + "Student List: " + str(self.studentList);


    #setters for course class others inherited from Student Class
    def setCourseName(s, cnam):
        s.courseName = cnam;
    def setCourseNumber(s, cnum):
        s.courseNumber = cnum;
    def setStudentList(s, sl):
        s.studentList = sl;

    #getters for course class
    def getCourseName(s):
        return s.courseName;
    def getCourseNumber(s):
        return s.courseNumber;

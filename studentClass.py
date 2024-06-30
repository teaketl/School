import utility;
from userClass import User;

class Student(User):
    IDnumber = "";
    major = "";
    grade = "";
    GPA = 0.0;
    courses = []
    def __init__(self, fn="", ln="", us="", p="", bd="", pm="",ID="", m="", gr="", gpa="", c=None): #rearrange to us, p, ... #constructor
        super().__init__(fn, ln, us, p, bd, pm);
        self.IDnumber = ID;
        self.major = m;
        self.grade = gr;
        self.gpa = gpa;
        self.courses = c;
        if c is None:
            self.courses = [];
        else:
            self.courses = c;

    def __str__(self):
        return "Student Name : " + self.firstName + self.lastName + " " + "ID Number: " + self.IDnumber + "Username: " + self.username + " " + "Password: " + self.password + " " + "Major : " + self.major + " " + "Grade: " + self.grade + " " + "GPA: " + self.gpa + " " + "Birthday: " + self.birthday + " " + "Courses: " + str(self.courses) + "Permission: " + self.permission;

    def __repr__(self):
        return f"Student: {self.firstName} {self.lastName}";

    def setMajor(s, m):
        s.major = m;
    def setGrade(s, gr):
        s.grade = gr;
    def setGPA(s, gpa):
        s.gpa = gpa;
    def setCourses(s, c):
        s.courses = c;

    def getMajor(s):
        return s.major;
    def getGrade(s):
        return s.grade;
    def getGPA(s):
        return s.gpa;
    def getCourses(s):
        return s.courses;

#if i put pass will it just pass if correct and go to the next function
    def studentOptions(s):
        for tries in range(20): # keep asking
            options = input("Choose one of the following:\n1.Print Enrollment 2. Logout");
            if (options == '1'):
                try:
                    IDnumber = input("Enter your ID number to pull up your enrollment:\n")
                    openStudentInfo = open('studentInfo.csv', 'r');
                    readStudentInfo = utility.readCSV(openStudentInfo);
                    if (IDnumber == readStudentInfo[0]): #0 index for ID number
                        for IDnumber in range(len(readStudentInfo)):
                            for studentList in readStudentInfo:
                                print(studentList);
                    else:
                        print("Wrong ID!");
                except:
                    FileNotFoundError;
                    print("No students have been added yet. How did you even log in?"); #gotta add a first student dude
            elif (options != '1' or '2'):
                print("Not an option!");
            elif options == '2':
                return;

"""
File name: userClass.py
Purpose: For final project. blueprint for the admin and student class
Author: Teagan Holmes
Create date: 11/8/2023
Last update date:11/8/2023
version: 1.1
"""

import sys;
import csv;
from datetime import date; # for convertAge calculator

class User:
    firstName = "";
    lastName = "";
    username = ""; # should move these to top
    password = ""; # ^^^^
    birthday = 0; #use age calc later
    permission = "";
    def __init__(self, fn="", ln="", us="", p="", bd="", pm=""): #rearrange to us, p, ... #constructor
        self.firstName = fn;
        self.lastName = ln;
        self.username = us;
        self.password = p;
        self.birthday = bd;
        self.permission = pm;

    #str method
    def __str__(self):
        return "User - Name: " + self.firstName + " " + self.lastName  + " " + "Username: " + self.username + " " + "Password: " + self.password + " " + "Birthday: " + self.birthday + " " + "Permission: " + self.permission;

    #setters
    def setFirstName(s, fn):
        s.firstName = fn;
    def setLastName(s, ln):
        s.lastName = ln;
    def setUsername(s, us):
        s.username = us;
    def setPassword(s, p):
        s.password = p;
    def setBirthday(s, bd):
        s.birthday = bd;
    def setPerm(s, pm):
        s.permission = pm;

    #getters
    def getFirstName(s):
        return s.firstName;
    def getLastName(s):
        return s.lastName;
    def getUsername(s):
        return s.username;
    def getPassword(s):
        return s.password;
    def getBirthday(s):
        return s.birthday;
    def getPerm(s):
        return s.permission;

    def getAge(s, YYYY, MM, DD):
        birthday= date(YYYY, MM, DD);
        today= date.today();
        calc = ((today - birthday).days / 365);
        age= int(calc);
        return age;


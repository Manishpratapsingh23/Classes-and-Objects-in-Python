'''
You are given two classes, Person and Student,
 where Person is the base class and Student is the derived class. 
 Completed code for Person and a declaration for Student are provided for you in the editor. 
 Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, .
A string, .
An integer, .
An integer array (or vector) of test scores, .
A char calculate() method that calculates a Student object's average 
and returns the grade character representative of their calculated average:
'''




class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
   
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    def __init__(self,fname,lname,idnumber,score):
        super().__init__(fname,lname,idnumber)
        self.score = score

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    def calculate(self):
        a = sum(self.score)/len(self.score)
        if a>=90 and a<=100:
            ch = 'O'
        elif a>=80 and a<90:
            ch = 'E'
        elif a>=70 and a<80:
            ch = 'A'
        elif a>=55 and a<70:
            ch = 'P'
        elif a>=40 and a<55:
            ch = 'D'
        else:
            ch = 'T'
        return ch

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
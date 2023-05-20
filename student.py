from math import * # Import math

class Student:
    ''' A student class with name ,credit and quality within it .'''
    def __init__(self, name, credit, quality):
        self.name = name
        self.credit = credit
        self.quality = quality

    def getName(self):
        ''' Returns name of the student'''
        return self.name

    def getCredit(self):
        '''Returns the credits of the student'''
        return self.credit

    def getQuality(self):
        '''Returns the quality of the sudent'''
        return self.quality

    def gpa(self):
        '''Returns grade point average of a student'''
        return self.quality / self.credit


def makeStudent(infostr):
    '''Helper function to create a Student object'''
    name, credit, quality = infostr.split('\t')
    return Student(name, credit, quality)


def read_student(filename):
    '''Accepts filename and returns the students in that file'''
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students


def write_student(students, filename):
    '''Writes student into another file called outputfile'''
    outfile = open(filename, 'w')
    for s in students:
        print('{0}\t{1}\t{2}'.format(s.getName, s.getCredit, s.getQuality), file=outfile)
    outfile.close()


def sort(filename, by, order):
    '''Receives filename and sorts file either according to gpa,name or credit'''
    data = read_student(filename)
    if by == 'gpa':
        data.sort(key=Student.gpa)
        if order == 'd':
            data.reverse()
    if by == 'name':
        data.sort(key=Student.getName)
        if order == 'd':
            data.reverse()
    if by == 'credit':
        data.sort(key=Student.getCredit)
        if order == 'd':
            data.reverse()
    return data
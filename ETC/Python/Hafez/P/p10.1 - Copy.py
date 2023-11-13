class Person:
    def __init__(self):
        system("cls")
        self.name=input('{} section:\n\nEnter your first name: '.format(((str(type(self)).split('.'))[-1]).split("'")[0])).strip()
        self.last_name=input('Enter your last name: ').strip()
        self.age=int(input('Enter your age: '))
        n=1
        if type(self)==Student:
            n=18
        elif type(self)==Teacher:
            n=22
        while self.age<n:
            self.age=int(input('\7Age cannot be lower than {}!\nTry again: '.format(n)))
        self.gender=input('Enter your gender (Male/ Female/ Other): ')
        while self.gender!='Male' and self.gender!='Female' and self.gender!='Other':
            self.gender=input('\7Wrong input!\nEnter your gender from shown options (Male/ Female/ Other): ')
        if type(self)!=Person:
            self.uni=input("Enter your university's name: ")
        if type(self)==Student:
            self.term=int(input('Enter your semester: '))
            while self.term<=0 or self.term>10 or ((self.age+1)-18)*2<self.term:
                if self.term<=0 or self.term>10:
                    self.term=int(input('\7Your semester cannot be lower than 1 or higher than 10!\nTry again: '))
                    continue
                self.term=int(input('\7Your cannot be at semester {} in the age of {}!\nTry again: '.format(self.term,self.age)))
    def info(self):
        system("cls")
        print('You are a ',((str(type(self)).split('.'))[-1])[:-2],'\nName: ',self.name,'\nLast name: ',
              self.last_name,'\nAge: ',self.age,' years old\nGender: ',self.gender,sep='')
        if type(self)==Teacher:
            print('University of ',self.uni,'\n',self.exp,' years of experiance\nTeaching hours in a month: '
                  ,self.hour,'\nCost per hour: ',self.cst_hr,sep='',end='\n\n')
        elif type(self)==Student:
            print('University of ',self.uni,'\nSemester: ',self.term,sep='',end='\n\n')
class Student(Person):        #Student
    def __init__(self):
        super().__init__()
        self.grade=[]
    def get_grade(self):
        system("cls")
        i=0
        num=int(input('Enter number of grades for {} {}: '.format(st.name,st.last_name)))
        while num<=0:
            num=int(input('\7This number must be possetive!\nEnter number of grades for {} {} again: '.format(st.name,st.last_name)))
        while i<num:
            i+=1
            G=float(input('\nEnter grade number {}: '.format(i)))
            while not(0<=G<=20):
                G=float(input('\n\7Grade must be in range of 0 to 20!\nEnter grade number {} again: '.format(i)))
            U=float(input('Enter unit for grade number {}: '.format(i)))
            while U<=0:
                U=int(input('\n\7Unit must be possetive!\nEnter unit for grade number {} again: '.format(i)))
            self.grade+=[G,U]
    def mean(self):
        grd=unt=0
        for i in range(0,len(self.grade),2):
            grd+=self.grade[i]*self.grade[i+1]
            unt+=self.grade[i+1]
        self.average=grd/unt
        return self.average
    def evaluation(self):
        if self.mean()<10:
            self.evaluate='Failed'
        elif self.mean()<12:
            self.evaluate='Conditioneded'
        else:
            self.evaluate='Passed'
        return self.evaluate
class Teacher(Person):        #Teacher
    def __init__(self):
        system("cls")
        super().__init__()
        self.exp=int(input('Enter your experience: '))
        while self.age-self.exp<22 or self.exp<0:
            self.exp=int(input('\7You can make experience only after you are 22 years old!\nTry again: '))
        self.hour=int(input('Enter your overall teaching hours per month: '))
        while not(0<=self.hour<=400):
            self.hour=float(input('\7Your overall teaching hours per month must be in range of 0 to 400!\nTry again: '))
        self.cst_hr=float(input('Enter your teaching cost per hour: '))
        while self.cst_hr<0:
            self.cst_hr=float(input('\7Your teaching cost per hour cannot be negative!\nTry again: '))
    def salary(self):
        self.slry=self.cst_hr*self.hour
        return self.slry
#======================================================================================
from os import *
st=Student()
st.get_grade()
system("cls")
st.info()
system("pause")
system("cls")
print('GPA for',len(st.grade)//2,'grades of',st.name,st.last_name,'is',st.mean(),'\nYour GPA evaluation is:',st.evaluation(),end='\n\n')
system("pause")
system("cls")
tch=Teacher()
system("pause")
system("cls")
tch.info()
system("pause")
system("cls")
print(tch.name,' ',tch.last_name,"'s salary per month is ",tch.salary(),sep='',end='\n\n')
system("pause")

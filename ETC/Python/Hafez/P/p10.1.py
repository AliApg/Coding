class Person:
    def __init__(self):
        system("cls")
        self.name=input('{} section:\n\nEnter your first name: '.format(((str(type(self)).split('.'))[-1]).split("'")[0])).strip()
        while self.name=='' or self.name.isalpha()==False:
            self.name=input('\aName cannot be empty and it can only contain alphabet!\nTry again: ').strip()
        self.last_name=input('Enter your last name: ').strip()
        while self.last_name=='' or self.last_name.isalpha()==False:
            self.last_name=input('\aLast name cannot be empty and it can only contain alphabet!\nTry again: ').strip()
        n=1
        if type(self)==Student:
            n=18
        elif type(self)==Teacher:
            n=22
        while True:
            try:
                self.age=int(input('Enter your age: '))
                while self.age<n:
                    self.age=int(input('\7Age cannot be lower than {}!\nTry again: '.format(n)))
                break
            except:
                print('\7Age must be a integer number!')
        self.gender=input('Enter your gender (Male/ Female/ Other): ').strip()
        while (self.gender.lower() in ['male','female','other'])==False:
            self.gender=input('\7Wrong input!\nEnter your gender from shown options (Male/ Female/ Other): ').strip()
        if type(self)!=Person:
            self.uni=input("Enter your university's name: ").strip()
            while self.uni=='' or self.uni.isalpha()==False:
                self.uni=input("\aUniversity's name cannot be empty and it can only contain alphabet!\nTry again: ").strip()
    def info(self):
        system("cls")
        print('You are a ',((str(type(self)).split('.'))[-1])[:-2],'\nName: ',self.name,'\nLast name: ',
              self.last_name,'\nAge: ',self.age,' years old\nGender: ',self.gender,sep='')
        if type(self)==Teacher:
            print('University of ',self.uni,'\n',self.exp,' years of experiance\nTeaching hours in a month: '
                  ,self.hour,'\nCost per hour: ',self.cst_hr,sep='',end='\n\n')
        elif type(self)==Student:
            print('University of ',self.uni,'\nSemester: ',self.term,sep='',end='\n\n')
        system("pause")
        system("cls")
class Student(Person):        #Student
    def __init__(self):
        super().__init__()
        self.grade=[]
        self.term=input('Enter your semester: ')
        while  self.term.isdigit()==False or int(self.term)<=0 or int(self.term)>10 or ((self.age+1)-18)*2<int(self.term):
            if self.term.isdigit()==False:
                self.term=input('\7Your semester must be a number!\nTry again: ')
            elif int(self.term)<=0 or int(self.term)>10:
                self.term=input('\7Your semester cannot be lower than 1 or higher than 10!\nTry again: ')
            else:
                self.term=input('\7Your cannot be at semester {} in the age of {}!\nTry again: '.format(self.term,self.age))
        self.term=int(self.term)
    def get_grade(self):
        system("cls")
        i=0
        num=input('Enter number of grades for {} {}: '.format(st.name,st.last_name))
        while num.isdigit()==False or int(num)<=0:
            num=input('\7This input must be a possetive integer number!\nTry number of grades for {} {} again: '.format(st.name,st.last_name))
        num=int(num)
        while i<num:
            try:
                G=float(input('\nEnter grade number {}: '.format(i+1)))
                while not(0<=G<=20):
                    G=float(input('\n\7Grade must be in range of 0 to 20!\nEnter grade number {} again: '.format(i+1)))
                U=float(input('Enter unit for grade number {}: '.format(i+1)))
                while U<=0:
                    U=int(input('\n\7Unit must be possetive!\nEnter unit for grade number {} again: '.format(i+1)))
                self.grade+=[G,U]
                i+=1
            except:
                print('\n\7Input must be a number!')
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
        while True:
            try:
                self.exp=int(input('Enter your experience: '))
                while self.age-self.exp<22 or self.exp<0:
                    self.exp=int(input('\7You can make experience only after you are 22 years old!\nTry again: '))
                break
            except:
                print('\7This input must be an integer number!')
        while True:
            try:
                self.hour=float(input('Enter your overall teaching hours per month: '))
                while not(0<=self.hour<=400):
                    self.hour=float(input('\7Your overall teaching hours per month must be in range of 0 to 400!\nTry again: '))
                break
            except:
                print('\7This input must be a number!')
        while True:
            try:
                self.cst_hr=float(input('Enter your teaching cost per hour: '))
                while self.cst_hr<0:
                    self.cst_hr=float(input('\7Your teaching cost per hour cannot be negative!\nTry again: '))
                break
            except:
                print('\7This input must be a number!')
    def salary(self):
        self.slry=self.cst_hr*self.hour
        return self.slry
#======================================================================================
from os import *
st=Student()
st.get_grade()
st.info()
print('GPA for',len(st.grade)//2,'grades of',st.name,st.last_name,'is',st.mean(),'\nYour GPA evaluation is:',st.evaluation(),end='\n\n')
system("pause")
system("cls")
tch=Teacher()
tch.info()
print(tch.name,' ',tch.last_name,"'s salary per month is ",tch.salary(),sep='',end='\n\n')
system("pause")

from student_login import Login
from student_class2 import Student
from operator_class1 import Operator
import logging
import pandas as pd
import csv
import hashlib


"""def operator_log_foodlist(): operator will login and if his login was successfull he will make food list for one week
operator have three time chance to enter correct user and pass also"""


def Operator_log_foodlist():
    count = 0
    # return_count=100 #for returning of function
    while count < 3:
        obj2 = Operator('undertaking_user_pass.csv')
        obj_opera = obj2.Operator_Login(input("please enter opera username:"), input("please enter opera password:"))
        if str(obj_opera) == "operator login was succesful":
            count += 3
            print("login was succesful")
            obj2.Food_list()
        elif str(obj_opera) == "operator passeord is wrong":
            count += 1
            print("Access denied\n Wrong password")
        elif str(obj_opera) == "operator user_name is wrong":
            count += 1
            print("Access denied\n Wrong username")


# operator_run
obj3 = Operator_log_foodlist()
with open('food_list.csv', 'r') as foods:
    food_reader = pd.read_csv(foods)
    print(food_reader)



def Student_Log():
    """studen login method:studen have two time chance to enter wrong user or pass,
       else he or she couldnot login and if login was succesful this method return
       the row of person who entered for student class"""
    count = 0
    while count < 3:
        # create an object from student_login class
        obj_login = Login(input("please enter your user name:"), input("please enter your password:")).login()
        if str(obj_login) != 'Access denied\n Wrong password' and \
                str(obj_login) != 'Access denied\n No username found':
            print("login was succesful")
            count += 3
            return obj_login
        elif str(obj_login) == 'Access denied\n Wrong password':
            print("Access denied\n Wrong password")
            count += 1
        elif str(obj_login) == 'Access denied\n No username found':
            print('Access denied\n No username found')
            count += 1
    print("you have tried three times\nyour chance for login finished")


# student login
obj1 = Student_Log()
print(Student(obj1, 'studen_user_pass.csv', "food_list.csv").preview_food_list())
# print(Student(obj1, 'studen_user_pass.csv', 'food_list.csv').food_reservation())
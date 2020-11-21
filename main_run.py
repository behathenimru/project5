from student_login_n import Login
from student_class3 import Student
from operator_class_n import Operator
import pandas as pd
import logging

"""def operator_log_foodlist(): operator will login and if his login was successfull he will make food list for one week.
operator have three time chance to enter correct user and pass also"""


def Operator_log_foodlist():
    count = 0
    try:
        while count < 3:
            obj2 = Operator('undertaking_user_pass.csv')
            obj_opera = obj2.Operator_Login(input("please enter opera username:"),
                                            input("please enter opera password:"))
            if str(obj_opera) == "operator login was succesful":
                count += 3
                print("login was succesful")
                # obj2.Food_list()
                return True
            elif str(obj_opera) == "operator password is wrong":
                count += 1
                print("Access denied\n Wrong password")
            elif str(obj_opera) == "operator user_name is wrong":
                count += 1
                print("Access denied\n Wrong user_name")
            else:
                count += 1
                print("Access denied\n Wrong username and password")
    except:
        print("wrong value given")


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
            print('Access denied\n Wrong password')
            count += 1
        elif str(obj_login) == 'Access denied\n No username found':
            print('Access denied\n No username found')
            count += 1
    logging.info('This is an info message')

#main..................................................................
"""this part is the main of program:at first we have two choice,student or operator"""

"""if operator has been choosen we use Operator_log_foodlist method for loggin and if loggin was succesful
operator will make food list otherwise the program will end.
and if loggin was unsuccesfull we will back to choose student or operator loggin again"""

"""if student has been choosen we have some different choice to continue:
"Balance info
Charging balance
Weekly food menu
Food reservation
exit"""



status="True"
while status=="True":
    print("1-student\n2-operator\n")
    student_or_operator = input("plaese enter a number:")
    if student_or_operator == "2":
        obj3 = Operator_log_foodlist()
        if obj3 == True:
            operator_decition = input("do you want to make food list for student:\n1-yes\n2-no\n")
            if operator_decition == "1":
                obj_opera_food = Operator('undertaking_user_pass.csv')
                obj_opera_food.Food_list()
                print("you done")
            else:
                status="False"



    elif student_or_operator == "1":
        stu_row_num = Student_Log()
        stu_login = Student(student_row=stu_row_num, student_file="studen_user_pass.csv", food_file="food_list.csv")
        user_exit = "no"
        while user_exit == "no":
            with open("student_page.csv", 'r') as foods:
                food_reader = pd.read_csv(foods)
                print(food_reader)
            student_request = input("Please enter your request number:")
            if student_request == "0":
                stu_login = Student(student_row=stu_row_num, student_file="studen_user_pass.csv", food_file="food_list.csv")
                stu_init_credit = stu_login.student_Balance()
                print(stu_init_credit)
                user_exit = input("a) back to menu"
                                  "\n"
                                  "b) exit"
                                  "\n"
                                  "please enter a or b :")
                if user_exit == "b":
                    user_exit = "exit"
                else:
                    user_exit = "no"
            elif student_request == "1":
                charge_amount = int(input("please enter charging amount:"))
                stu_login = Student(student_row=stu_row_num, student_file="studen_user_pass.csv", food_file="food_list.csv")
                print(stu_login.credit_increment(charging=charge_amount))
                stu_new_credit = stu_login.student_Balance()
                print(stu_new_credit)
                user_exit = input("a) back to menu"
                                  "\n"
                                  "b) exit"
                                  "\n"
                                  "please enter a or b :")
                if user_exit == "b":
                    user_exit = "exit"
                else:
                    user_exit = "no"
            elif student_request == "2":
                stu_login = Student(student_row=stu_row_num, student_file="studen_user_pass.csv", food_file="food_list.csv")
                show_food_menu = stu_login.preview_food_list()
                print(show_food_menu)
            elif student_request == "3":
                stu_login = Student(student_row=stu_row_num, student_file="studen_user_pass.csv", food_file="food_list.csv")
                list_of_stu_food_orders = stu_login.food_reservation()
                if len(list_of_stu_food_orders) == 0:
                    pass
                else:
                    save_orders_for_main_file = stu_login.save_food_reservation(list_of_food_order=list_of_stu_food_orders)
                    save_orders_for_stu = stu_login.week_food_info_file()
                user_exit = input("a) back to menu"
                                  "\n"
                                  "b) exit"
                                  "\n"
                                  "please enter a or b :")
                if user_exit == "b":
                    user_exit = "exit"
                else:
                    user_exit = "no"
            elif student_request == "4":
                user_exit = "exit"
                status="False"
                print("user exit")

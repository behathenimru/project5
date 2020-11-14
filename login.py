from  student_list import list_students
from  operator_list import operator_info

class Login:

    choose_login = int(input("Please enter the number of the requested log in: \n 1.student \n 2.operator \n "))


    def __init__(self, username, password):
        self.username=username
        self.password=password

    def login(self):
        if choose_login == 1:
            if self.username == list_students["username"]:
                if self.password == list_students["password"]:
                    access = " successful "
                    return " Access successful "
            access = " denied "
            return " Access denied "

        if choose_login == 2:
            if self.username == operator_info["username"]:
                if self.password == operator_info["password"]:
                    access = " successful "
                    return " Access successful "
            access = " denied "
            return " Access denied "












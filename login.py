from  student_list import list_students
from  operator_list import operator_info

class Login:

    choose_login = int(input("Please enter the number of the requested log in: \n 1.student \n 2.operator \n "))


    def __init__(self, username , password):
        self.username=username
        self.password=password

    def login(self):
        if Login.choose_login == 1:
            for raw in list_students:
                if self.username == raw["username"]:
                    if self.password == raw["password"]:
                        access_student = " successful "
                        return " Access successful "

            access_student = " denied "
            return " Access denied "

        if Login.choose_login == 2:
            if self.username == operator_info[0]["username"]:
                if self.password == operator_info[0]["password"]:
                    access_operator = " successful "
                    return " Access successful "
            access_operator = " denied "
            return " Access denied "

        return " sth went wrong! "


print(Login("narges", "12345").login())









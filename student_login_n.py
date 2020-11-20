import csv
import pandas as pd
import hashlib


class Login:
    """This class is for student login"""

    def __init__(self, username , password) :
        self.username = username
        self.password = password


    def login(self) :

        row_count = 0
        with open('studen_user_pass.csv', 'r') as csv_file :
            reader = csv.reader(csv_file)
            names_list = next(reader)
            data = pd.read_csv('studen_user_pass.csv', names=names_list)
            username_list = data.user.tolist()#creating a list of colnames and getting usernames into a list

            if self.username in username_list:
                for row in reader:
                    if self.username != row[0]:
                        row_count += 1
                    elif self.username == row[0] :
                        str_hash_user = self.password
                        hash_object_user = hashlib.md5(str_hash_user.encode())
                        # print(2,"row[1]",row[1])
                        # print(2,"self.password",self.password)
                        #self.password=hash_object_user.hexdigest()
                        if self.password == row[1] :
                            return row_count+2  #it should add with 2(changed by maryam)

                            #return ' Access successful '
                        return 'Access denied\n Wrong password'

            return 'Access denied\n No username found'


# print(Login("9910012" , "o10012i").login())
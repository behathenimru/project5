import csv
import pandas as pd



class Login:

    def __init__(self, username , password) :
        self.username = username
        self.password = password


    def login(self) :
        row_count = 0

        with open('studen_user_pass.csv', 'r') as csv_file :
            reader = csv.reader(csv_file)
<<<<<<< HEAD
            names_list = reader.next ()
            #print(names_list)
=======
            names_list = next(reader)       #change reader.next() to next(reader) by narges
>>>>>>> 2275aa70a7129695759486b907e701b4608e5329
            data = pd.read_csv('studen_user_pass.csv', names=names_list)
            username_list = data.user.tolist()

            if self.username in username_list:

                for row in reader:

                    if self.username != row[0]:
                        row_count += 1

                    elif self.username == row[0] :
                        if self.password == row[1] :
<<<<<<< HEAD
                            return row_count
=======
                            return row_count+2  #add2 by narges
>>>>>>> 2275aa70a7129695759486b907e701b4608e5329
                            #return ' Access successful '
                        return ' Access denied '


            return ' Access denied! '
                    #sum(1 for rw in csv_file) + 1

<<<<<<< HEAD
print(Login("9910012" , "l10012h").login())
=======
print(Login("9910021" , "g10021r").login())
>>>>>>> 2275aa70a7129695759486b907e701b4608e5329

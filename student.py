import csv

#class Login:
    #def __init__(self, username , password):
        #self.username=username
        #self.password=password

#def login():
with open('studen_user_pass.csv', 'r') as csv_file:
    reader=csv.reader(csv_file)
    for row in reader:
        print(row)
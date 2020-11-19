import csv
import hashlib


class Operator:
    def __init__(self, operator_file):
        self.operator_file = operator_file
        # with open('undertaking_user_pass.csv', 'r') as csv_file :
        #     reader = csv.reader(csv_file)
        #     self.reader=reader

    def Operator_Login(self, name, password):
        str_hash_opera = password
        hash_object_opera = hashlib.md5(str_hash_opera.encode())
        self.password = hash_object_opera.hexdigest()
        self.name = name
        with open(self.operator_file, 'r') as stu_file:
            # open operator info file
            self.reading_operator = csv.reader(stu_file)
            #     self.operator_info = list(self.reading_operator)
            for row in self.reading_operator:
                if self.name == row[0] and self.password == row[2]:
                    print("operator login was succesful")
                elif self.name == row[0] and self.password != row[2]:
                    print("operator passeord is wrong")
                elif self.name != row[0] and self.password == row[2]:
                    print("operator user_name is wrong")

    def Food_list():
        with open('food_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["day", "food number1", "price", "food number2", "price"])
            writer.writerow(["saturday", input("enter a food nember one for saturday:"), input("enter a price:") \
                                , input("enter a food nember two for saturday:"), input("enter a price:")])
            writer.writerow(["sunday", input("enter a food nember one for sunday:"), input("enter a price:") \
                                , input("enter a food nember two for sunday:"), input("enter a price:")])
            writer.writerow(["monday", input("enter a food nember one for monday:"), input("enter a price:") \
                                , input("enter a food nember two for monday:"), input("enter a price:")])
            writer.writerow(["tuesday", input("enter a food nember one for tuesday:"), input("enter a price:") \
                                , input("enter a food nember two for tuesday:"), input("enter a price:")])
            writer.writerow(["wednsday", input("enter a food nember one for wednsday:"), input("enter a price:") \
                                , input("enter a food nember two for wednsday:"), input("enter a price:")])
            writer.writerow(["thirsday", input("enter a food nember one for thirsday:"), input("enter a price:") \
                                , input("enter a food nember two for thirsday:"), input("enter a price:")])
            writer.writerow(["friday", input("enter a food nember one for friday:"), input("enter a price:") \
                                , input("enter a food nember two for friday:"), input("enter a price:")])


# obj = Operator('undertaking_user_pass.csv')
# obj.Operator_Login(input("please enter operator name:\n"), input("please enter operator password:\n"))

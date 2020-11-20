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
                    return "operator login was succesful"
                elif self.name == row[0] and self.password != row[2]:
                    return "operator passeord is wrong"
                elif self.name != row[0] and self.password == row[2]:
                    return "operator user_name is wrong"

    def Food_list(self):
        with open('food_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["day", "food number1", "price", "food number2", "price"])
            writer.writerow(["Saturday", input("enter a food number one for Saturday:"), input("enter a price:") \
                                , input("enter a food number two for Saturday:"), input("enter a price:")])
            writer.writerow(["Sunday", input("enter a food number one for Sunday:"), input("enter a price:") \
                                , input("enter a food number two for Sunday:"), input("enter a price:")])
            writer.writerow(["Monday", input("enter a food number one for Monday:"), input("enter a price:") \
                                , input("enter a food number two for Monday:"), input("enter a price:")])
            writer.writerow(["Tuesday", input("enter a food number one for Tuesday:"), input("enter a price:") \
                                , input("enter a food number two for Tuesday:"), input("enter a price:")])
            writer.writerow(["Wendsday", input("enter a food number one for Wendsday:"), input("enter a price:") \
                                , input("enter a food number two for Wendsday:"), input("enter a price:")])
            writer.writerow(["Thursday", input("enter a food number one for Thursday:"), input("enter a price:") \
                                , input("enter a food number two for Thursday:"), input("enter a price:")])
            writer.writerow(["Friday", input("enter a food number one for Friday:"), input("enter a price:") \
                                , input("enter a food number two for Friday:"), input("enter a price:")])


# obj = Operator('undertaking_user_pass.csv')
# obj.Operator_Login(input("please enter operator name:\n"), input("please enter operator password:\n"))
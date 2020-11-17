import csv
import pandas as pd


class Student:
    """ It is Student class. It gets file of students info (file contents: user number, password, credit, weekly food reservation),
    login student row number from the "students" file, and food file(file contents: food menu for a week).
    by this class student(user) can charge his credit and reserves food for a week.
    It subtracts food cost from user credit and report the balance condition.
    This class updates students info file after weekly reservation.
    also makes a file for student to report list of food reservation and his credit"""
    """ This class contains """

    def __init__(self, student_row, student_file, food_file):
        """ student_row = login student row number from the students info file
        student_file = name of students info file
        food_file= name of food file"""
        self.student_row = student_row
        self.student_file = student_file
        self.food_file = food_file
        with open(self.student_file, 'r') as stu_file:
            # open students info file
            self.reading = csv.reader(stu_file)
            self.student_info = list(self.reading)  # make a list, contaning lists of each student info
            self.student_credit = int(
                self.student_info[self.student_row][2])  # get info of student credit form its cell

    def preview_food_list(self):
        """ this method shows the menu of food for a week and their costs"""
        with open(self.food_file, 'r') as foods:
            food_reader = pd.read_csv(foods)
            return food_reader

    def food_reservation(self):
        """ This method get student order.
        It make a list of dictionaries for student food reservation, each dict is contained ordered food and its cost.
        this method compars food cost with student credit. If user balance is sufficient, subtracting food cost from credit and save order.
        else, it reports insufficient balance and exit from method"""
        with open(self.food_file, 'r') as foods:
            # open food file as reader
            food_reader = csv.reader(foods)
            line_count = 0  # for control lines of food file for reading the file
            list_of_food_order = []  # the list that contains dicts of ordered food and its cost for a week
            for row_r in food_reader:
                """ it is a loop to read food file rows then reserves food"""
                food_order_dict = {}  # dict of each ordered food (dict key) and its cost(dict value)
                if line_count == 0:  # doesn't read the first line of the food file
                    line_count += 1
                    pass
                else:
                    food_check = 100  # make while condition
                    while food_check == 100:  # do this loop until student enters correct number which the method wants.
                        print(row_r[0], ":", "1-", row_r[1], "2-", row_r[3])  # show each day food suggestion
                        food_order = input("please enter food number, if you wont to order enter 0:")
                        # get food order from user by enter the related number of food suggestion
                        if food_order == "0" or food_order == "1" or food_order == "2":
                            # check to get a correct order(number)
                            if food_order == "0":  # user didn't order any food
                                food_check = 200
                                food_order_dict["-"] = None  # save nothing in dict
                                pass
                            elif food_order == "1":  # choose first suggestion
                                food_order = row_r[1]  # replace food number with food name as food order
                                if self.student_credit < int(row_r[2]):
                                    # compare user balance with food cost
                                    return """ your balance is insufficient.
                                your Balance:{}""".format(self.student_credit)
                                else:
                                    self.student_credit -= int(row_r[2])  # subtract food cost from balance
                                food_order_dict[food_order] = int(row_r[2])
                                # adjust key and value of "food_order_dict" dictionary with name of ordered food and its cost from their cells in food file
                                food_check = 200  # change while condition to exit from While loop

                            elif food_order == "2":  # choose second suggestion
                                food_order = row_r[3]  # replace food number with food name as food order
                                if self.student_credit < int(row_r[2]):
                                    # compare user balance with food cost
                                    return """ your balance is insufficient.
                                your Balance:{}""".format(self.student_credit)
                                else:
                                    self.student_credit -= int(row_r[2])  # subtract food cost from balance
                                food_order_dict[food_order] = int(row_r[4])
                                # adjust key and value of "food_order_dict" dictionary with name of ordered food and its cost from their cells in food file
                                food_check = 200  # change while condition to exit from While loop
                        else:
                            # report to student to choose correct order
                            print("please enter correct number")
                list_of_food_order.append(
                    food_order_dict)  # append dict of food and it cost to the list of "list_of_food_order"
                self.student_info[self.student_row][
                    2] = self.student_credit  # update student credit after each reservation
            return list_of_food_order  # use this list in "save_food_reservation" method to save ordered food in "students" file for operator
            # and for student to show his food reservation result

    def credit_increment(self, charging):
        """ this method charge user credit by get charge amount
        It also updates student related rows in "students" file after charging """
        init_credit = int(
            self.student_info[self.student_row][2])  # change initial credit amount from string to integer
        self.student_info[self.student_row][2] = init_credit + charging  # add charge amount to credit
        with open(self.student_file, 'w', newline='') as new_file:
            # update the student row in "students" file
            csv_writer = csv.writer(new_file)
            csv_writer.writerows(self.student_info)
        return self.student_info[self.student_row][2]  # updated student credit

    def save_food_reservation(self, list_of_food_order):
        """ this method save student food reservation in students file for operator
        it get "list_of_food_order" list that is made in "food_reservation" method
        then save food names in related cell of each day in the student row"""
        for i in range(len(list_of_food_order)):
            """ the loop for move in "list_of_food_order" list and set the food name it their cells"""
            if i == 0:
                pass
            else:
                for food_name in list_of_food_order[i].keys():
                    # set the food name from the key of "food_order_dict" in "list_of_food_order" list
                    self.student_info[self.student_row][i + 2] = food_name

        with open(self.student_file, 'w', newline='') as new_file:
            # update "students" file after student food reservation is finished for a week
            csv_writer = csv.writer(new_file)
            csv_writer.writerows(self.student_info)
        return self.student_file

    def week_food_info_file(self):
        """ In this method save a file for student to report his food reservation for a week"""
        with open("food_reservation_for_student.csv", 'w') as file_for_student:
            write_file = csv.writer(file_for_student)
            write_file.writerow(
                ["student number", "student password", "credit", "sat", "sun", "mon", "tue", "wen", "thu", "fri"])
            write_file.writerow(self.student_info[self.student_row])

    def student_credit(self):
        """ this method report student balance"""
        if self.student_info[self.student_row][2] == 0:
            print("please charge your account")
        else:
            return "your Balance:{}".format(self.student_info[self.student_row][2])

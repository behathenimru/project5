import csv
def Food_list():
    with open('food_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["day", "food number1", "price", "food number2", "price"])
<<<<<<< HEAD
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
=======
        writer.writerow(["Saturday", input("enter a food nember one for saturday:"), input("enter a price:") \
                            , input("enter a food nember two for saturday:"), input("enter a price:")])
        writer.writerow(["Sunday", input("enter a food nember one for sunday:"), input("enter a price:") \
                            , input("enter a food nember two for sunday:"), input("enter a price:")])
        writer.writerow(["Monday", input("enter a food nember one for monday:"), input("enter a price:") \
                            , input("enter a food nember two for monday:"), input("enter a price:")])
        writer.writerow(["Tuesday", input("enter a food nember one for tuesday:"), input("enter a price:") \
                            , input("enter a food nember two for tuesday:"), input("enter a price:")])
        writer.writerow(["Wednesday", input("enter a food nember one for wednsday:"), input("enter a price:") \
                            , input("enter a food nember two for wednsday:"), input("enter a price:")])
        writer.writerow(["Thursday", input("enter a food nember one for thirsday:"), input("enter a price:") \
                            , input("enter a food nember two for thirsday:"), input("enter a price:")])
        writer.writerow(["Friday", input("enter a food nember one for friday:"), input("enter a price:") \
>>>>>>> 2275aa70a7129695759486b907e701b4608e5329
                            , input("enter a food nember two for friday:"), input("enter a price:")])

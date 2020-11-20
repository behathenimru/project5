import csv
def Food_list():
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
        writer.writerow(["Wednesday", input("enter a food number one for Wednesday:"), input("enter a price:") \
                            , input("enter a food number two for Wednesday:"), input("enter a price:")])
        writer.writerow(["Thursday", input("enter a food number one for Thursday:"), input("enter a price:") \
                            , input("enter a food number two for Thursday:"), input("enter a price:")])
        writer.writerow(["Friday", input("enter a food number one for Friday:"), input("enter a price:") \
                            , input("enter a food number two for Friday:"), input("enter a price:")])
# Food_list()
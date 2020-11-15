import csv
with open('undertaking_user_pass.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["user", "password","hash(pass)"])
    writer.writerow([100,"123456ali",hash("123456ali")])
    writer.writerow([200,"maryam654321",hash("maryam654321")])
import csv
with open('undertaking_user_pass.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["user", "password"])
    writer.writerow([100,hash(123456)])
    writer.writerow([200,hash(654321)])
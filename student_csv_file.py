import csv
with open('studen_user_pass.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["user", "password"])
    for i in range(9910010,9910041):
        writer.writerow([i,hash(i-9900000)])
import csv
L=["Balance info","Charging balance","Weekly food menu","Food reservation","exit"]
with open('student_page.csv', 'w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["User menu:"])
    for i in range(len(L)):
        writer.writerow([L[i]])
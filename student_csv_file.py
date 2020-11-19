import csv
import random
with open('studen_user_pass.csv', 'w', newline='') as file:
    writer = csv.writer(file)
<<<<<<< HEAD
    writer.writerow(["user", "password","hash(pass)","credit","saturday","sunday","monday","tuesday","wednsday","thirsday","friday"])
=======
    writer.writerow(["user", "password","hash(pass)","Credit","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"])
>>>>>>> 2275aa70a7129695759486b907e701b4608e5329
    ch=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",\
        "s","t","u","v","w","x","y","z","@","#","$","&","*"]
    for i in range(9910010,9910041):
        writer.writerow([i,random.choice(ch)+str(i-9900000)+random.choice(ch),\
<<<<<<< HEAD
                         hash(random.choice(ch)+str(i-9900000)+random.choice(ch)),1500])
=======
                         hash(random.choice(ch)+str(i-9900000)+random.choice(ch)),1500,"","","","","","",""])
>>>>>>> 2275aa70a7129695759486b907e701b4608e5329

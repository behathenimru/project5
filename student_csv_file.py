import csv
import random
import os
os.remove("studen_user_pass.csv")

with open('studen_user_pass.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["user", "password","hash(pass)","credit","saturday","sunday","monday",\
                     "tuesday","wednsday","thirsday","friday"])
    ch=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",\
        "s","t","u","v","w","x","y","z","@","#","$","&","*"]
    for i in range(9910010,9910041):
        writer.writerow([i,random.choice(ch)+str(i-9900000)+random.choice(ch),\
                         hash(random.choice(ch)+str(i-9900000)+random.choice(ch)),1500])
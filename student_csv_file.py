import csv
import random
import hashlib
with open('studen_user_pass.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["user", "password","hash(pass)","Credit","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"])
    ch=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",\
        "s","t","u","v","w","x","y","z","@","#","$","&","*"]
    for i in range(9910010,9910041):
        str_hash=random.choice(ch)+str(i-9900000)+random.choice(ch)
        hash_object = hashlib.md5(str_hash.encode())
        print(hash_object.hexdigest())
        writer.writerow([i,str_hash,hash_object.hexdigest(),1500,"","","","","","",""])
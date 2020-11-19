import csv
import hashlib
with open('undertaking_user_pass.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["user", "password","hash(pass)"])
    str_hash_one ="123456ali"
    hash_object_one= hashlib.md5(str_hash_one.encode())
    writer.writerow([100,"123456ali",hash_object_one.hexdigest()])
    str_hash_two ="maryam654321"
    hash_object_two= hashlib.md5(str_hash_two.encode())
    writer.writerow([200,"maryam654321",hash_object_two.hexdigest()])
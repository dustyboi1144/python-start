print("####Password Generator####")
import random
import string
pool = string.ascii_letters + string.digits + string.punctuation
lenght = int(input("enter the lenght of the password:"));
password =""
for i in range(lenght):
    password += random.choice(pool)
print("generated password is :",password)

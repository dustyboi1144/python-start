print("####Password Generator####")
import secrets
import string
pool = string.ascii_letters + string.digits + string.punctuation
length = int(input("enter the lenght of the password:"))
password =""
for i in range(length):
    password += secrets.choice(pool)
print("generated password is :",password)

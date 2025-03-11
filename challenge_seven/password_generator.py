import random

all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

lenght = int(input("Enter lenght: "))
password = ""

for a in range(lenght):
    password += random.choice(all_chars)

print(f"You'r password is:{password}")
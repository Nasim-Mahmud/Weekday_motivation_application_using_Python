from smtplib import *
import datetime as dt
import random

# Finding the day of the week.
today = dt.datetime.now()
current_weekday = today.weekday()  # 1 means Monday
# print(current_weekday)

# Reading the quote file.
with open("quotes.txt", "r") as data:
    all_quotes = data.readlines()
    quote = random.choice(all_quotes)
    # print(quote)

# Sending mail
sender_email = "tmailone01@gmail.com"
sender_email_pass = "rteqejuqqdhcgpzx"  # Not the actual password.

receiver_email = "tmailtwo02@yahoo.com"

if current_weekday == 4:
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_email_pass)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:WeekDay Motivation For You \n"
                                f"{quote}")

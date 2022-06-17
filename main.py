from smtplib import *
import datetime as dt
import random

# Finding the day of the week.
today = dt.datetime.now()
current_weekday = today.weekday()


# Reading the quote file.
with open("quotes.txt", "r") as data:
    all_quotes = data.readlines()
    quote = random.choice(all_quotes)
    print(quote)


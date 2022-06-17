from smtplib import *
import datetime as dt
import pandas

today = dt.datetime.now()
current_weekday = today.weekday()

with open("quotes.txt", "r") as data:
    quotes = data.readlines()
    print(quotes)


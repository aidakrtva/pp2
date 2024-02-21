#Write a Python program to subtract five days from current date.
import datetime

today = datetime.datetime.now()
five_days_later = today - datetime.timedelta(days = 5)

print (today, five_days_later)
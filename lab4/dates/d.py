#Write a Python program to calculate two date difference in seconds.

import datetime 


date1 = datetime.datetime.now()
date2 = date1 - datetime.timedelta(days = 3655)
differ = date1 - date2
print (differ.total_seconds())


"""
print ("todays date is:", *{today})
print ("date", *{daaa} , "days ago was ", *{differ})
insecond = daaa * 24 * 60 * 60
print ("difference between two days on seconds is:" , *{insecond}) 
"""





"""
import datetime

today = datetime.datetime.now()

print(today.strftime("%S"))
"""
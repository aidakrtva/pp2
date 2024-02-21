#Write a Python program to drop microseconds from datetime.
import datetime

time = datetime.datetime.now()
time_without_microseconds = time.replace( microsecond=0)
print(time, time_without_microseconds)


#for fun i wanna delete the date 
today = datetime.datetime.now()
print (today.strftime(f"%H:%M:%S.%f"))
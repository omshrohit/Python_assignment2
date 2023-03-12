''' write a python script to display current date and time. First create variables to  store date and time, then display
date and time in proper format (like:13-8-2022 and 9:00 PM)
'''
import time
import datetime
t=time.localtime()
current_time=time.strftime("%H:%M:%S",t)
print(current_time)

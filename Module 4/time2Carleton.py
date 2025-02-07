#Jadan Carleton
#Friday, February 7th, 2025

#This program calculates when to set off an alarm


str_time = input("What time is it now (in hours 0-23)?")
str_wait_time = input("What is the number of hours to wait?")

time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = (time + wait_time) % 24

print("Your alarm will go off at " + str(time_when_alarm_go_off) + ":00")

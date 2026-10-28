import datetime

date = datetime.date(2023, 6, 15)
today = datetime.date.today()

time = datetime.time(14, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")

target_datetime = datetime.datetime(2028, 6, 15, 14, 30, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print(" target date has passed.")
    
else:
    print(" target date has not passed yet.")
 

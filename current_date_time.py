import datetime
current_date_time= datetime.datetime.now()
format_date=current_date_time.strftime("%d - %m - %y   %H:%M:%S")
print(f"current date and time : {format_date}")
string="ASTRING"
print(string[1:5:2])
print(string[::-1])
from datetime import datetime,timedelta
today=datetime.now()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("yesterday:",yesterday.strftime("%Y-%m-%d"))
print("today:",today.strftime("%Y-%m-%d"))
print("tomorrow:",tomorrow.strftime("%Y-%m-%d"))



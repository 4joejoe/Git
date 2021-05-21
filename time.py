# %% 
import datetime as dt
date = dt.date.today()
datetime = dt.datetime
now = datetime.now()
current_time = dt.time(now.hour,now.minute,now.second)
go = dt.datetime.combine(date,current_time)
print(go)
from datetime import date, timedelta

x=date.today()
y=x-timedelta(days=1)
t=x+timedelta(days=1)
print("Yesterday:", y)
print("Today:", x)
print("tomorrow:", t)
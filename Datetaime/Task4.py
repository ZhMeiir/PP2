import datetime

x=[]
for i in range(12):
    y=int(input())
    x.append(y)

date1 = datetime.datetime(x[0], x[1], x[2], x[3], x[4], x[5])
date2 = datetime.datetime(x[6], x[7], x[8], x[9], x[10], x[11])

dif = date2 - date1
sec = dif.total_seconds()

print("Time difference in seconds:", sec)
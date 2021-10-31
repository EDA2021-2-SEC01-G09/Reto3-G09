from datetime import datetime

time_1 = '2022/10/29 09:17:30'
date_1 = datetime.strptime(time_1, "%Y/%m/%d %H:%M:%S")
time_2 = '2021/10/30 09:17:31'
date_2 = datetime.strptime(time_2, "%Y/%m/%d %H:%M:%S")

print(date_1 < date_2) 


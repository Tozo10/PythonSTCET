import datetime
from datetime import datetime
m1 = 0
month = range(1,13)
for year in range(2014, 2022):
    for m in month:
        if datetime(year, m, 1).weekday() == 0:
            m1 += 1
print(m1)

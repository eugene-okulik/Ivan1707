import datetime
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.normpath(os.path.join(script_dir, '../../../homework/eugene_okulik/hw_13/data.txt'))

with open(file_path, encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

dates = []
for line in lines:
    without_number = line.split('. ', 1)[-1]
    date_str = without_number.split(' - ')[0]
    dates.append(date_str)

dt1 = datetime.datetime.strptime(dates[0], '%Y-%m-%d %H:%M:%S.%f')
dt1_week = dt1 + datetime.timedelta(days=7)
print(dt1_week.strftime('%Y-%m-%d %H:%M:%S.%f'))

dt2 = datetime.datetime.strptime(dates[1], '%Y-%m-%d %H:%M:%S.%f')
print(dt2.strftime('%A'))

dt3 = datetime.datetime.strptime(dates[2], '%Y-%m-%d %H:%M:%S.%f')
days_ago = (datetime.datetime.now() - dt3).days
print(days_ago)

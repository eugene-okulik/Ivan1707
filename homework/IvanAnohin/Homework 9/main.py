import datetime

date_string = "Jan 15, 2023 - 12:05:33"
dt = datetime.datetime.strptime(date_string, "%b %d, %Y - %H:%M:%S")

month_full = dt.strftime("%B")
print(month_full)
formatted_date = dt.strftime("%d.%m.%Y, %H:%M")
print(formatted_date)

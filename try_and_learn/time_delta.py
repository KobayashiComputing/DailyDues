from datetime import timedelta, datetime

day1 = datetime.now()
day0 = datetime.strptime("1985-08-10 04:32:00", "%Y-%m-%d %H:%M:%S")
td1 = day1 - day0
print(f"TD1: {td1}")

one_day = timedelta(days=1)
print(f"One Day: {one_day}")
one_hour = timedelta(hours=1)
print(f"One Hour: {one_hour}")

      

# Example timedelta
td = timedelta(days=2, hours=3, minutes=45)
td2 = timedelta(years=3, )

# Convert to string (total seconds)
td_str = str(td)
print(td_str)  # Output: "2 days, 3:45:00"

# Convert back to timedelta
td_parsed = timedelta(seconds=sum(int(x) * 60 ** i for i, x in enumerate(reversed(td_str.split(":")[-1].split(":")))))
print(td_parsed)  # Output: "2 days, 3:45:00"

import datetime

def get_today_date_and_weekday():
    today = datetime.date.today()
    weekday_name = today.strftime("%A")
    return today, weekday_name

# Example usage:
date, weekday = get_today_date_and_weekday()
print(f"Today's date: {date}")
print(f"Day of the week: {weekday}")

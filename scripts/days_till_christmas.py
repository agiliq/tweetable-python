import datetime

def days_till_christmas():
    return (datetime.date(year=datetime.datetime.now().year, month=12, day=25) - datetime.datetime.now().date()).days

from enum import Enum

class WeekStr:
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

def is_weekend_str(week_day):
    return week_day == WeekStr.SATURDAY or week_day == WeekStr.SUNDAY

class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def is_weekend_(week_day):
    return week_day is Week.SATURDAY or week_day is Week.SUNDAY

friday = Week.FRIDAY
print(friday)
print(friday.name, friday.value)

print(friday is Week.FRIDAY)
print(friday is Week.MONDAY)
friday = Week.FRIDAY
print(is_weekend_(Week.SUNDAY))
print(is_weekend_str(WeekStr.SUNDAY))

print (is_weekend_str("SUNDAY"))
print(is_weekend_(7))
print(is_weekend_str("Sunday"))

print(is_weekend_str("Sunday"))


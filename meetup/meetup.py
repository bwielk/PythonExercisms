from calendar import monthcalendar
from datetime import date

def meetup_day(year, month, day_of_the_week, which):
    days_of_week = {'Monday': 0,
                    'Tuesday': 1,
                    'Wednesday': 2,
                    'Thursday': 3,
                    'Friday': 4,
                    'Saturday': 5,
                    'Sunday': 6}
    index_of_the_day_of_the_week = days_of_week[day_of_the_week]
    matrix_of_month_days = monthcalendar(year, month)
    result = 0
    try:
        if which != 'last':
            for week in matrix_of_month_days:
                if which == '1st' and week[index_of_the_day_of_the_week] in range(0, 10) and result is 0:
                    result = week[index_of_the_day_of_the_week]
                if which == '2nd' and week[index_of_the_day_of_the_week] in range(8, 15):
                    result = week[index_of_the_day_of_the_week]
                if which == '3rd' and week[index_of_the_day_of_the_week] in range(15, 22):
                    result = week[index_of_the_day_of_the_week]
                if which == '4th' and week[index_of_the_day_of_the_week] in range(22, 29):
                    result = week[index_of_the_day_of_the_week]
                if which == '5th' and week[index_of_the_day_of_the_week] in range(24, 31):
                    result = week[index_of_the_day_of_the_week]
                if which == 'teenth' and week[index_of_the_day_of_the_week] in range(10, 20):
                    result = week[index_of_the_day_of_the_week]
        else:
            current_index_of_last_week = len(matrix_of_month_days)-1
            while result is 0:
                last_week = matrix_of_month_days[current_index_of_last_week]
                result = last_week[index_of_the_day_of_the_week]
                current_index_of_last_week -= 1
        return date(year, month, result)
    except ValueError as exc:
        raise MeetupDayException from exc


class MeetupDayException(Exception):
    def __init__(self):
        super().__init__('The day does not exist. Please review the date arguments')
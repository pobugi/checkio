"""What’s your favourite day of the week? Check if it's the most common day of the week in a year.

You are given a year as an integer (e. g. 2001). You should return the most frequent day(s) of 
the week in that particular year. The result has to be a list of days sorted by the order of days 
in a week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.
"""

import datetime
from collections import Counter


def most_frequent_days(a):

    base_date = datetime.datetime(year=a, month=1, day=1)
    date_list = [base_date]
    while base_date.year < a + 1:
        base_date += datetime.timedelta(days=1)
        date_list.append(base_date)
    weekday_list = [date.weekday() for date in date_list[:-1]]

    c = Counter()

    for weekday in weekday_list:
        c[weekday] += 1
    c = dict(c)
    res = [list(c.keys())[0]]

    for key in list(c.keys())[1:]:
        if c[key] == c[res[0]]:
            res.append(key)

    weekdays = {0: 'monday', 1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'sunday'}

    ans = []
    for i in sorted(res):
        ans.append(weekdays[i].capitalize())
    return ans


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
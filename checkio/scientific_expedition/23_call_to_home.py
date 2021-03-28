from typing import List
import math, datetime

def total_cost(calls: List) -> int:
    
    def calc(duration):
        if duration < 100:
            price = duration
        else:
            price = 100 + (duration - 100) * 2
        return price
    d = {}
    for record in calls:
        record = record.split()
        print(record)
        time = str(record[0]) + ' ' + str(record[1])
        duration = record[2]
        time_start = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        time_end = time_start + datetime.timedelta(seconds=int(duration))
        date = time_start.date()
        try:
            d[date] += math.ceil(int(duration)/60)
        except KeyError:
            d.update({date: math.ceil(int(duration)/60)})
    print(d)
    for key in d:
        price = calc(int(d[key]))
        d.update({key: price})
    print(d)
    res = 0
    for price in d.items():
        res += price[1]
    return res

print(total_cost((  "2014-01-01 01:12:13 181",
                    "2014-01-02 20:11:10 600",
                    "2014-01-03 01:12:13 6009",
                    "2014-01-03 12:13:55 200")))



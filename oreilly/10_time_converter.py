"""You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places.
Your task is to convert the time from the 12-h format into 24-h by following the next rules:
- the output format should be 'hh:mm'
- if the output hour is less than 10 - write '0' before it. For example: '09:05'
Here you can find some useful information about the 12-hour format."""


def time_converter(time):
    time_lst = time.split()
    if time_lst[-1] == 'p.m.':
        hm = time_lst[0].split(':')
        hours = int(hm[0])
        minutes = int(hm[1])
        h = hours if hours == 12 else hours + 12
        time = str(h).zfill(2) + ':' + str(minutes).zfill(2)
    elif time_lst[-1] == 'a.m.':
        hm = time_lst[0].split(':')
        hours = int(hm[0])
        minutes = int(hm[1])
        h = 0 if hours == 12 else hours
        time = str(h).zfill(2) + ':' + str(minutes).zfill(2)
    return time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")

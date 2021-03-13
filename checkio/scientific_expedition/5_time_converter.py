"""You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format
and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format
by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Here you can find some useful information about the 12-hour format."""


def time_converter(time):
    hours = int(time[:2])
    minutes = int(time[3:])
    if 23 >= hours >= 12:
        if hours == 12:

            if minutes == 0:

                marker = ' p.m.'
            else:
                marker = ' p.m.'
        else:
            hours = hours - 12
            marker = ' p.m.'
    elif 11 >= hours >= 0:
        if hours == 0 and minutes == 0:
            hours = 12
            marker = ' a.m.'
        else:
            marker = ' a.m.'

    if 9 >= minutes >= 0:
        text_minutes = '0' + str(minutes)
    else:
        text_minutes = str(minutes)

    return str(hours) + ':' + text_minutes + marker


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")

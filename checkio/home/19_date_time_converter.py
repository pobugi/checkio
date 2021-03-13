"""Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format."""


def date_time(source: str) -> str:
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    source_split = source.rpartition(' ')
    date = source_split[0].split('.')
    time = source_split[-1].split(':')

    day = int(date[0])
    month = date[1]
    year = date[2]

    hours = int(time[0])
    hours_ending = ' hour ' if str(hours)[-1] == '1' else ' hours '
    minutes = int(time[1])
    minutes_ending = ' minute' if str(minutes)[-1] == '1' else ' minutes'

    dt = str(day) + ' ' + months[int(month)] + ' ' + year + ' ' + 'year '
    tm = str(hours) + hours_ending + str(minutes) + minutes_ending
    return dt + tm


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")

"""How old are you in a number of days? It's easy to calculate - just subtract your birthday from today.
We could make this a real challenge though and count the difference between any dates.

You are given two dates as an array with three numbers - a year, month and day.
For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days between the given dates.
For example between today and tomorrow = 1 day. The difference will always be either a positive number or zero,
so don't forget about the absolute value."""

from datetime import date


def days_diff(a, b):
    return abs((date(a[0], a[1], a[2]) - date(b[0], b[1], b[2])).days)


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")

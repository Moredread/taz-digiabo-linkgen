"""
Taz digiabo download link generator

Usage: digiabo.py [-d N | --days N]

Options:
    -d N --days N  number of days in the past to generate download links for [default: 1]

"""
from datetime import date, datetime, timedelta
from docopt import docopt


def generate_past_dates(d, from_date=None):
    """
    Generates a tuple of date objects for the d last days, including the current one.

    >>> generate_past_dates(1, date(2013, 11, 4))
    (datetime.date(2013, 11, 4),)
    >>> generate_past_dates(5, date(2013, 11, 4))
    (datetime.date(2013, 10, 31), datetime.date(2013, 11, 1), datetime.date(2013, 11, 2), datetime.date(2013, 11, 3), datetime.date(2013, 11, 4))

    :param d: number of days to generate
    :type d: Integer
    :param from_date: date to consider today, defaults to today
    :type from_date: date

    :returns tuple of days
    """
    if from_date is None:
        from_date = date.today()

    day_interval = timedelta(days=-1)

    return tuple(sorted([from_date + i * day_interval for i in range(d)]))

def main():
    arguments = docopt(__doc__, version="0.0.1")
    print arguments
    print generate_past_dates(int(arguments["--days"]))

if __name__ == '__main__':
    main()
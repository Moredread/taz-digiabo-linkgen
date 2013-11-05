"""
Taz digiabo download link generator

Usage: digiabo.py [-d N | --days N]

Options:
    -d N --days N  number of days in the past to generate download links for [default: 1]

"""
from datetime import date, timedelta
from docopt import docopt

templates = [
    "https://dl.taz.de/abo/{}_{:0=2}_{:0=2}.pdf",
    "https://dl.taz.de/abo/{}_{:0=2}_{:0=2}_PDF.zip",
    "https://dl.taz.de/abo/taz_{}_{:0=2}_{:0=2}.epub",
    "https://dl.taz.de/abo/tazt_{}_{:0=2}_{:0=2}.epub",
    "https://dl.taz.de/abo/taz_{}_{:0=2}_{:0=2}.mobi",
    "https://dl.taz.de/abo/tazt_{}_{:0=2}_{:0=2}.mobi",
    "https://dl.taz.de/abo/{}_{:0=2}_{:0=2}_HTM.zip",
    "https://dl.taz.de/abo/{}_{:0=2}_{:0=2}.txt",
    "https://dl.taz.de/abo/{}_{:0=2}_{:0=2}_ASCII.zip"
]


def past_dates(d, from_date=None):
    """
    Generates a tuple of date objects for the d last days, including the current one.

    >>> past_dates(1, date(2013, 11, 4))
    (datetime.date(2013, 11, 4),)
    >>> past_dates(5, date(2013, 11, 4))
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


def print_templates(this_date):
    """
    Prints the list a list of format templates with the given this_date

    :type this_date: date
    """
    for template in templates:
        print template.format(this_date.year, this_date.month, this_date.day)


def main():
    arguments = docopt(__doc__, version="0.0.1")
    dates = past_dates(int(arguments["--days"]))

    for d in dates:
        print_templates(d)

if __name__ == '__main__':
    main()
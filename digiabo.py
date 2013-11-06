"""
Taz digiabo download link generator

Usage: digiabo.py [-d N | --days N] | --license

Options:
    -d N --days N  generate links for N days in the past, including today [default: 1]
    --license  Print the license of this script
"""

__license__ = """Taz digiabo download link generator

Copyright (c) 2013, Andre-Patrick Bubel <code@andre-bubel.de>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from datetime import date, timedelta
from docopt import docopt

templates = [
    "https://dl.taz.de/abo/{0}_{1:0=2}_{2:0=2}.pdf",
    "https://dl.taz.de/abo/{0}_{1:0=2}_{2:0=2}_PDF.zip",
    "https://dl.taz.de/abo/taz_{0}_{1:0=2}_{2:0=2}.epub",
    "https://dl.taz.de/abo/tazt_{0}_{1:0=2}_{2:0=2}.epub",
    "https://dl.taz.de/abo/taz_{0}_{1:0=2}_{2:0=2}.mobi",
    "https://dl.taz.de/abo/tazt_{0}_{1:0=2}_{2:0=2}.mobi",
    "https://dl.taz.de/abo/{0}_{1:0=2}_{2:0=2}_HTM.zip",
    "https://dl.taz.de/abo/{0}_{1:0=2}_{2:0=2}.txt",
    "https://dl.taz.de/abo/{0}_{1:0=2}_{2:0=2}_ASCII.zip"
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
    arguments = docopt(__doc__, version="0.1.0")
    dates = past_dates(int(arguments["--days"]))

    if arguments["--license"]:
        print __license__
        exit(0)

    for d in dates:
        print_templates(d)

if __name__ == '__main__':
    main()
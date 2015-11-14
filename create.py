from datetime import date

from phildb.create import create
from phildb.database import PhilDB

create('pypi_downloads')

from count import write_downloads

db = PhilDB('pypi_downloads')
db.add_source('pypi', 'pypi.python.org')
db.add_measurand('last_day', 'last_day', 'Downloads in the last day')
db.add_measurand('last_week', 'last_week',  'Downloads in the last week')
db.add_measurand('last_month', 'last_month',  'Downloads in the last month')
db.add_measurand('total', 'total',  'Total downloads')

# Write some download information I had manually collected over the last few days
write_downloads(
    {
        'info': {
            'name': 'PhilDB',
            'downloads': {'last_day': 6, 'last_month': 572, 'last_week': 74}
        }
    }, date(2015, 11, 12)
)
write_downloads(
    {
        'info': {
            'name': 'PhilDB',
            'downloads': {'last_day': 20, 'last_month': 596, 'last_week': 92}
        }
    }, date(2015, 11, 13)
)
write_downloads(
    {
        'info': {
            'name': 'PhilDB',
            'downloads': {'last_day': 15, 'last_month': 603, 'last_week': 91}
        }
    }, date(2015, 11, 14)
)

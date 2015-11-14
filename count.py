from datetime import date
import pandas as pd
import requests

from phildb.database import PhilDB
from phildb.exceptions import DuplicateError

MEASURANDS = ['last_day', 'last_week', 'last_month']

db = PhilDB('pypi_downloads')

def get_pypi_info(package_name):
    r = requests.get('https://pypi.python.org/pypi/{0}/json'.format(package_name))
    return r.json()

def write_downloads(json, day = None):

    if day is None:
        today = date.today()
    else:
        today = day

    pkg_name = json['info']['name']

    try:
        db.add_timeseries(pkg_name)
    except DuplicateError:
        pass

    for m in MEASURANDS:
        try:
            db.add_timeseries_instance(pkg_name, 'D', '', source='pypi', measurand = m)
        except DuplicateError:
            pass

        db.write(pkg_name, 'D', pd.Series([json['info']['downloads'][m]], [today]), measurand = m, source = 'pypi')


import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


# Complete the function below.
# Base query: https://jsonmock.hackerrank.com/api/stocks

import datetime


DATE_FORMAT = '%d-%B-%Y'
URL_TEMPLATE = 'https://jsonmock.hackerrank.com/api/stocks?date={date}&page={page}'


def openAndClosePrices(firstDate, lastDate):
    for dt in get_dates_range(parse_date(firstDate), parse_date(lastDate)):
        for item in load_date(dt):
            print('{}   {:.2f}   {:.2f}'.format(item['date'], item['open'], item['close']))


def parse_date(date_str):
    return datetime.datetime.strptime(date_str, DATE_FORMAT).date()


def date2str(dt):
    res = dt.strftime(DATE_FORMAT)
    # ugly fix to get rid of zero padding in day of month
    # have not found how to do it in the docs with strftime
    if res.startswith('0'):
        return res[1:]
    return res


def get_dates_range(start_date, end_date):
    res = []
    curr_date = start_date
    while curr_date <= end_date:
        res.append(curr_date)
        curr_date = curr_date + datetime.timedelta(days=1)
    return res


def load_date(dt):
    try:
        page = 1
        while True:
            with urlopen(URL_TEMPLATE.format(date=date2str(dt), page=page)) as response:
                data = json.loads(response.read())
                for item in data['data']:
                    yield item
                if page >= data['total_pages']:
                    break
                page += 1
    except URLError as e:
        print('Couldn\'t reach server: {}'.format(e.reason))


try:
    _firstDate = str(input())
except:
    _firstDate = None


try:
    _lastDate = str(input())
except:
    _lastDate = None

openAndClosePrices(_firstDate, _lastDate)

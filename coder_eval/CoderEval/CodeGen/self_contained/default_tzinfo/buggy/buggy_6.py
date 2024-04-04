def default_tzinfo(dt, tzinfo):
	"""
	Sets the ``tzinfo`` parameter on naive datetimes only

This is useful for example when you are provided a datetime that may have
either an implicit or explicit time zone, such as when parsing a time zone
string.

.. doctest::

    >>> from dateutil.tz import tzoffset
    >>> from dateutil.parser import parse
    >>> from dateutil.utils import default_tzinfo
    >>> dflt_tz = tzoffset("EST", -18000)
    >>> print(default_tzinfo(parse('2014-01-01 12:30 UTC'), dflt_tz))
    2014-01-01 12:30:00+00:00
    >>> print(default_tzinfo(parse('2014-01-01 12:30'), dflt_tz))
    2014-01-01 12:30:00-05:00

:param dt:
    The datetime on which to replace the time zone

:param tzinfo:
    The :py:class:`datetime.tzinfo` subclass instance to assign to
    ``dt`` if (and only if) it is naive.

:return:
    Returns an aware :py:class:`datetime.datetime`.
	"""
	if dt.tzinfo is not None:
		return dt
	else:
		return dt.replace(tzinfo=tzinfo)
import time
import datetime
import threading
import re

from datetime import timedelta
from pymongo import MongoClient

from utils import DB_CONN, HOST_DB, DATABASE_NAME, MONGODB_CONN
from config import DB_TYPE, DB_SETTINGS

class DateTime:
    def __init__(self, time_string):
        self.time_string = time_string

    def parse_time(self):
        try:
            self.time_string = time.strftime("%H:%M:%S", time.strptime(self.time_string, '%H:%M:%S'))
        except ValueError as e:
            raise Exception(e)

class MongoDB:
    def __init__(self, db_name, collection_name):
        self.db_name = db_name
        self.collection_name = collection_name
        self.mongo_connection = self._connect()

    def _connect(self):
        return MongoClient(host=DB_SETTINGS[self.db_name]["host"],
                           port=DB_SETTINGS[self.db_name]["port"],
                           username=DB_SETTINGS[self.db_name]["username"],
                           password=DB_SETTINGS[self.db_name]["password"],
                           authSource=DB_SETTINGS[self.db_name]["authSource"])

    def insert_record(self, collection_name, data):
        collection = self.mongo_connection[self.db_name][collection_name]
        if collection.find_one({"_id": data["_id"]}) is None:
            collection.insert_one(data)
        else:
            collection.update_one({"_id": data["_id"]}, {"$set": data})
        return collection

    def find_record(self, collection_name, data):
        collection = self.mongo_connection[self.db_name][collection_name]
        doc = collection.find_one({"_id": data["_id"]})
        if doc is None:
            return None
        else:
            return doc

    def find_records(self, collection_name, data):
        collection = self.mongo_connection[self.db_name][collection_name]
        documents = collection.find({"_id": data["_id"]})
        return documents

    def update_record(self, collection_name, data):
        collection = self.mongo_connection[self.db_name][collection_name]
        collection.update_one({"_id": data["_id"]}, {"$set": data})
        return collection

    def delete_record(self, collection_name):
        collection = self.mongo_connection[self.db_name][self.collection_name]
        collection.delete_one({"_id":
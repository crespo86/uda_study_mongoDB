#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Let's assume that you combined the code from the previous 2 exercises with code
from the lesson on how to build requests, and downloaded all the data locally.
The files are in a directory "data", named after the carrier and airport:
"{}-{}.html".format(carrier, airport), for example "FL-ATL.html".

The table with flight info has a table class="dataTDRight". Your task is to
extract the flight data from that table as a list of dictionaries, each
dictionary containing relevant data from the file and table row. This is an
example of the data structure you should return:

data = [{"courier": "FL",
         "airport": "ATL",
         "year": 2012,
         "month": 12,
         "flights": {"domestic": 100,
                     "international": 100}
        },
         {"courier": "..."}
]

Note - year, month, and the flight data should be integers.
You should skip the rows that contain the TOTAL data for a year.

There are couple of helper functions to deal with the data files.
Please do not change them for grading purposes.
All your changes should be in the 'process_file' function.
"""
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")
    with open("{}/{}".format(datadir, f), "r") as html:
        soup = BeautifulSoup(html, "lxml")
        for yearly_data in soup.find_all('tr',"dataTDRight"):
            courier_data = {"courier": info["courier"], "airport": info["airport"], "year": None, "month": None,
                           "flights": {"domestic": None, "international": None}
                           }
            for n in range(0,4):
                if n == 0:
                    courier_data["year"] = int(yearly_data.find_all('td')[n].text)
                elif n == 1:
                    if yearly_data.find_all('td')[n].text != "TOTAL":
                        courier_data["month"] = int(yearly_data.find_all('td')[n].text)
                elif n == 2:
                    courier_data["flights"]["domestic"] = int(yearly_data.find_all('td')[n].text.replace(',',""))
                else:
                    courier_data["flights"]["international"] = int(yearly_data.find_all('td')[n].text.replace(',',""))
            if courier_data['month'] != None:
                data.append(courier_data)
    return data


def test():
    print "Running a simple test..."
    open_zip(datadir)
    files = process_all(datadir)
    data = []
    # Test will loop over three data files.
    for f in files:
        data += process_file(f)

    assert len(data) == 399  # Total number of rows
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[0]["courier"] == 'FL'
    assert data[0]["month"] == 10
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}

    print "... success!"

if __name__ == "__main__":
    test()

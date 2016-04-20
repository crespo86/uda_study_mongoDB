# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports' function so that it returns a list of airport
codes, excluding any combinations like "All".
"""

from bs4 import BeautifulSoup
html_page = "vergin_and_logan_airport.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        for line in soup.find(id="AirportList").find_all('option'):
            words = str(line).split('"')
            if words[0] == '<option value=' and len(words[1]) == 3:
                data.append(words[1])
    print data
    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()

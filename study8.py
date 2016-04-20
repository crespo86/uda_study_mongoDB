import requests
from bs4 import BeautifulSoup

s = requests.Session()

r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup = BeautifulSoup(r.text,"lxml")

f = open("vergin_and_logan_airport.html","w")
f.write(r.text)

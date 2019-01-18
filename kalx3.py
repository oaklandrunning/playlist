#created for Py2.7
#updated for Python3-July 19 2018

# import libraries
from urllib3 import PoolManager
from bs4 import BeautifulSoup
import html5lib
import requests

#specify the url
music_page = 'https://www.kalx.berkeley.edu/playlists'

#query the website and return the html to the variable 'page'
manager = PoolManager(10)
page = manager.request('GET', 'https://www.kalx.berkeley.edu/playlists')
page2 = manager.urlopen(page)
print(page2)

# with open('http://www.kalx.berkeley.edu/playlists/index.html') as fp:
#     soup = BeautifulSoup(fp)

#page = open("http://www.kalx.berkeley.edu/playlists/")
#parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html5lib')

#Take out the <div> of name and get its value
name_box = soup.find('td', attrs={'class': 'views-field views-field-nothing'})

#name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name_box)

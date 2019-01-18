# from https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=with%20open#making-the-soup

from bs4 import BeautifulSoup
import urllib3

music_page = "https://www.kalx.berkeley.edu/playlists/index.html"

with open(music_page) as fp:
    data = fp.read()

soup = BeautifulSoup(fp)

print(soup.prettify())

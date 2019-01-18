from bs4 import BeautifulSoup
import html5lib
import requests
import string
import pandas as pd
import re

#Downloads the content of webpage
r = requests.get('https://www.kalx.berkeley.edu/playlists')
soup = BeautifulSoup(r.content, 'html5lib')
soup.prettify()

#Find the tags you are looking for
name_box = soup('td', attrs={'class': 'views-field views-field-nothing'})

#Convert to a string
results = str(name_box)

#Clean up results, by stripping tags and replacing with commas or some other delimiter
stripped = results.split


#output = results.strip("<strong>")
print(stripped)

#Convert to a list so I can clean up
#For each "line", search and replace with artist, song, album


#Use to move data to a table
#panda_list = pd.read_csv(results)

#Append results to a separate file
# test_file = open("kalx_list.txt", mode="w")
# test_file.write(results)
# test_file.close()

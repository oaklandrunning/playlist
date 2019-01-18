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
#stripped = results.split() <----I think this turns it into a list?
#---------------------------------------------
#remove ending and trailing tags of string
nobeg_noend = re.sub(r'\s]', '\n', results)

#remove <strong> and </strong> tags, replace with a colon
string_matches = re.sub('<strong>', '\n', nobeg_noend)
# replace class tag with \n
stripped = re.sub(r'\s<td class="views-field views-field-nothing">', '\n', string_matches)

#replace </strong> with song: 
stripped2 = re.sub(r'\s</strong>- ', '; ', stripped)
stripped3 = re.sub('</strong>-', '; ', stripped2)
stripped4 = re.sub()

#replace "-" with album:
almost_done = re.sub(r'\s- ', '; ', stripped3)

#replace the ')\s</td>,' with a comma
almost_there = re.sub(r'\s</td>,', ';', almost_done)

#print output
print(almost_there)

#Use to move data to a table
#panda_list = pd.read_csv(almost_there, ";")

#Append results to a separate file
test_file = open("kalx.csv", mode="w")
test_file.write(almost_there)
test_file.close()
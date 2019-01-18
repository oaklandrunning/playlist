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
#stripped = results.split()

#remove <strong> and </strong> tags, replace with a colon
string_matches = re.sub('<strong>', '', results)

# replace class tag with \n
stripped = re.sub('<td class="views-field views-field-nothing">', '\n', string_matches)

#replace </strong> with song: 
stripped2 = re.sub('</strong>- ', ' ,song: ', stripped)

#replace "-" with album:
almost_done = re.sub(' - ', ' ,album: ', stripped2)

#replace the ')\s</td>,' with a comma
almost_there = re.sub(r'\s</td>,', ';', almost_done)

#print output
#print(string_matches

#Use to move data to a table
panda_list = pd.read_csv(almost_there, sep=';')
print(panda_list)

#Append results to a separate file
# test_file = open("kalx_list.txt", mode="w")
# test_file.write(results)
# test_file.close()

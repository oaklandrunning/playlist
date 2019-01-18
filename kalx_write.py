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
string_matches = re.sub('<strong>', 'artist: ', results)
# replace class tag with \n
stripped = re.sub('<td class="views-field views-field-nothing">', '\n', string_matches)

#replace </strong> with song: 
stripped2 = re.sub('</strong>- ', ' song: ', stripped)

#print output
print(stripped2)


#Use to move data to a table
#panda_list = pd.read_csv(clean_results)

#Append results to a separate file
# test_file = open("kalx_list.txt", mode="w")
# test_file.write(results)
# test_file.close()

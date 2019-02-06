from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import lxml
import requests
import string
import time

r = requests.get('https://www.kalx.berkeley.edu/programs/dj')
tags_with_article = SoupStrainer('article')
soup = BeautifulSoup(r.content, 'lxml', parse_only=tags_with_article).prettify()
print(soup)

#Find the tags you are looking for
#dj_names = soup('span', attrs={'property': 'dc:title'})

#Convert to a string
# results = str(dj_names)
# print(results)

# #### CLEANING AND STRIPPING ####
# clean_results = results.find("content=") ### THIS only give us a count as to how many djs there are: 39
# print(clean_results)


##### GETTING EMAILS #####
# for link in soup.find_all('a'):
#     print(link.get('href'))

#for content in soup.find_all('span', attrs={'property': 'dc:title'}):
#        print(str(content))


##### THIS IS WORKING DO NOT TOUCH
# all_links = []
# for link in soup.find_all('a'):
#     all_links.append(str(link))
# print(all_links)

# for line in all_links:
#     if "mailto" in line:
#         print(line)
##### This is working do not touch ####

# filename = "dj_list.csv"

# ### OPEN FILE WITH THE TIME AND DATE STAMP OH YEAH ###
# write_file = open(filename, mode ="w")
# write_file.write(results)
# write_file.close()


# get this tag: span property="dc:title" and  <a href="mailto: >
# dj_emails = []
# for 

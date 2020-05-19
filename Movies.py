'''
Top Rated 250 Movie by Imdb By Web Scraping
@author: Suyash Shivaji Phatak
Date: 10/05/2020
'''

# Importing Modules
from bs4 import BeautifulSoup
import urllib

# Giving url
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# Reading all content
content = urllib.request.urlopen(url).read()

# Passing the content to function
soup = BeautifulSoup(content, features="lxml")

print('_________________________________________________________________________')

# Printing content
print('\nAll contents of Websites')
print(soup.prettify())

# Printing title of website
print('_________________________________________________________________________')
print(soup.find('title'))
print('_________________________________________________________________________')

# Printing all elements of images and their alt text of 250 TV shows
print('These are the Top Rated 250 Pictures.\n')
for link in soup.find_all('img'):
    print(link.get('alt'))
    
print('_________________________________________________________________________')

# Printing the ratings inside the tags
print('This is ratings inside strong tag.\n')
print(soup.find_all('strong'))


'''
Top Rated 250 TV Shows by Imdb By Web Scraping
@author: Suyash Shivaji Phatak
Date: 10/05/2020
'''

# Importing Modules
from bs4 import BeautifulSoup
import urllib

# Giving url
url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

# Reading all content
content = urllib.request.urlopen(url).read()

# Passing the content to function
soup = BeautifulSoup(content, features="lxml")

print('_________________________________________________________________________')

# Printing content
print('\nAll contents of Websites')
print(soup.prettify())


# Printing title
print('_________________________________________________________________________')
print(soup.find('title'))
print('_________________________________________________________________________')

# Printing all elements of images and their alt text of 250 TV shows
print('These are the Top Rated 250 TV Shows.\n')
for link in soup.find_all('img'):
    print(link.get('alt'))
    
# Printing the ratings inside the tags
print('_________________________________________________________________________\n')
print('This is ratings inside strong tag.\n')
print(soup.find_all('strong'))


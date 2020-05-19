'''
Top 250 Oscar Wining Movie by Imdb By Web Scraping
@author: Suyash Shivaji Phatak
Date: 10/05/2020
'''

# Importing Modules
from bs4 import BeautifulSoup
import urllib

# Giving url
url = "https://www.imdb.com/search/title/?count=100&groups=oscar_best_picture_winners&sort=year%2Cdesc&ref_=nv_ch_osc"

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
print('These are the Top 250 Oscar Wining Pictures.\n')
for link in soup.find_all('img'):
    print(link.get('alt'))
    
print('_________________________________________________________________________')

# Printing the ratings inside the tags
print('This is ratings inside strong tag.\n')
print(soup.find_all('strong'))


import requests
from bs4 import BeautifulSoup as bs

gh_user = input('Enter GitHub username: ')
url = 'https://github.com/' + gh_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
avatar_url = soup.find('img', {'alt' : 'Avatar'})['src']
print(avatar_url)
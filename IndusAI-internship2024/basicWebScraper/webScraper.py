import requests
from bs4 import BeautifulSoup

url = 'http://www.amazon.in'
print(f'Scraping website: {url}\n')

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for heading in headings:
        print(heading.text.strip())
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

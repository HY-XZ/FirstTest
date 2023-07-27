import requests
from bs4 import BeautifulSoup

url = 'https://www.jjwxc.net/onebook.php?novelid=2835099'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.encoding = 'gbk'

soup = BeautifulSoup(response.text, 'html.parser')

novel_title = soup.find('span', class_='novel_category').find('a').text.strip()
content = []

for item in soup.select('#oneboolt tbody tr'):
    if item.select('td')[0].find('div', class_='noveltext'):
        content.append(item.select('td')[0].text.strip())

with open(f'{novel_title}.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(content))
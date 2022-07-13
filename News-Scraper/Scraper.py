import requests
from bs4 import BeautifulSoup


class PerformScrape:
    @staticmethod
    def extractor(url):
        print("Extracting news...")
        content = ''
        content += ('<h1>Hacker News Top Stories:</h1>\n' + '<h1>' + '-' * 50 + '<br>')
        res = requests.get(url)
        cont_1 = res.content
        soup = BeautifulSoup(cont_1, 'html.parser')
        for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
            content += ((str(i + 1) + ' :: ' + '<a=href"' + tag.a.get(
                'href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text != 'More' else '')
        return content

from bs4 import BeautifulSoup
import webbrowser as wb
import requests
import re
import sys

r = requests.get('https://www.folha.uol.com.br/')
r.encoding = 'UTF-8'
HTML = r.text
soup = BeautifulSoup(HTML, 'html.parser')

# Pega os títulos das matérias
def scrap_title():
    a = soup.find_all('a', {'class':"c-main-headline__url"}) + soup.find_all('a', {'class':"c-list-links__url"})
    Titles = []
    for i in range(len(a)):
        x = re.sub(r'<.*?>', '', str(a[i]))
        x = re.sub(r'\s+\s.*?\s+\s', '', x)
        Titles.append(x.strip())
    return Titles

# Pega só os links 
def scrap_title_link():
    b = soup.find_all('a', {'class':"c-main-headline__url"}, href=True) + soup.find_all('a', {'class':"c-list-links__url"}, href=True)
    links = []
    for i in range(len(b)):
        links.append(b[i]['href'])
    return links


def main():
    calls = scrap_title()
    links = scrap_title_link()

    try: c = int(sys.argv[1])
    except IndexError: c = None

    # abre a n-ésima matéria caso tenha sido passado 'n' como arg
    if c:
        wb.open_new(links[c])
    else:
        for i in range(len(calls)):
            print(f'[{i}] ', calls[i])

if __name__ == '__main__':
    main()

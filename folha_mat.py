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

# Pega o conteúdo da matéria
def scrap_article(n):
    links = scrap_title_link()
    news = requests.get(links[n])
    news.encoding = 'UTF-8'
    sopa = BeautifulSoup(news.text, 'html.parser')

    article = sopa.find_all('p')
    formated_lines = []
    for arc in article:
        x = str(arc)
        if x.startswith('<p>'):
            x = re.sub(r'<.*?>', '', x)
            formated_lines.append(x.strip())
    return formated_lines[:-2]

def main():
    calls = scrap_title()
    links = scrap_title_link()

    try: c = int(sys.argv[1])
    except IndexError: c = None
    try: n = sys.argv[2]
    except IndexError: n = None

    # abre a n-ésima matéria caso tenha sido passado 'n' como arg
    if c and not n:
        wb.open_new(links[c])
    elif c and n:
        for line in scrap_article(c):
            print(line)
    else:
        for i in range(len(calls)):
            print(f'[{i}] ', calls[i])

if __name__ == '__main__':
    main()

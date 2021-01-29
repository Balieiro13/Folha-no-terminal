from bs4 import BeautifulSoup
import webbrowser as wb
import requests
import re
import sys

r          = requests.get('https://www.folha.uol.com.br/')
r.encoding = 'UTF-8'
HTML       = r.text
soup       = BeautifulSoup(HTML, 'html.parser')

# Pega os títulos das matérias
def scrap_title():
    a = soup.find_all('a', {'class': "c-main-headline__url"}) + \
            soup.find_all('a', {'class': "c-list-links__url"})
    Titles = []
    for i in range(len(a)):
        x = re.sub(r'<.*?>', '', str(a[i]))
        x = re.sub(r'\s+\s.*?\s+\s', '', x)
        Titles.append(x.strip())
    return Titles

# Pega só os links
def scrap_title_link():
    b = soup.find_all('a', {'class': "c-main-headline__url"}, href=True) + \
            soup.find_all('a', {'class': "c-list-links__url"}, href=True)
    links = []
    for i in range(len(b)):
        links.append(b[i]['href'])
    return links

# Pega o conteúdo da matéria
def scrap_article(n):
    links         = scrap_title_link()
    news          = requests.get(links[n])
    news.encoding = 'UTF-8'
    sopa          = BeautifulSoup(news.text, 'html.parser')

    article = sopa.find_all('div', {'class':"c-news__body"})
    formated_lines = []
    for arc in article:
        for line in arc.find_all('p'):
            a = '\t' + line.getText().strip()
            formated_lines.append(a)
    return formated_lines

def main():
    calls = scrap_title()
    links = scrap_title_link()
    args  = sys.argv

    # abre a n-ésima matéria caso tenha sido passado 'n' como arg
    if len(args)   == 2:
        wb.open_new(links[int(args[1])-1])
    elif len(args) == 3:
        for line in scrap_article(int(args[1])-1):
            print(line)
    else:
        for i in range(len(calls)):
            print(f'[{i+1}] ', calls[i])

if __name__ == '__main__':
    main()

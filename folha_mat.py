from bs4 import BeautifulSoup
import webbrowser as wb
import requests
import sys

r          = requests.get('https://www.folha.uol.com.br/')
r.encoding = 'UTF-8'
HTML       = r.text
soup       = BeautifulSoup(HTML, 'html.parser')

# Pega os títulos das matérias
def scrap_title():
    title_from_soup = soup.find_all('a', {'class': "c-main-headline__url"}) + \
                      soup.find_all('a', {'class': "c-list-links__url"})
    Titles = []

    for t in title_from_soup:
        Titles.append(t.getText().strip())

    return Titles


# Pega só os links
def scrap_title_link():
    links_from_soup = soup.find_all('a', {'class': "c-main-headline__url"}, href=True) + \
                      soup.find_all('a', {'class': "c-list-links__url"}, href=True)
    Links = []

    for l in range(len(links_from_soup)):
        Links.append(links_from_soup[l]['href'])
        
    return Links


# Pega o conteúdo da matéria
def scrap_article(n):
    #request da página específica da matéria
    links              = scrap_title_link()
    news               = requests.get(links[n])
    news.encoding      = 'UTF-8'
    sopa               = BeautifulSoup(news.text, 'html.parser')
    articles_from_soup = sopa.find_all('div', {'class':"c-news__body"})
    formated_lines     = []

    for arc in articles_from_soup:
        for line in arc.find_all('p'):
            formated_lines.append('\t' + line.getText().strip())

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
            print(f'[{i+1}]', calls[i])


if __name__ == '__main__':
    main()

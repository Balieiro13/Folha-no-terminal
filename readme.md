# O que é?
`folha_mat.py` é um programinha inspirado no bot de telegram @WBonner_bot, para printar os títulos das matéria da Folha de SP. nos terminais Linux/MAC ou prompt cmd do Windows.

## Por que?
Bem, eu sou preguiçoso e sempre tenho um terminal aberto. Então se você

* tem um terminal sempre aberto
* quer ver apenas as chamadas das matérias
* quer abrir só uma matéria específica para ler

O programa serve muito bem.

## Instalação
O programa é escrito em python, então você vai precisar do interpretador e alguns módulos como `bs4` para fazer o scrapping.

### Requisitos
Além do python você irá precisar:
* `bs4`: Beautiful Soup para parsear o HTML
* `requests`: Para fazer o scrapping da pág
* `webbrowser`: Caso queira abrir a matéria.


    pip install bs4 requests webbrowser


## Utilização
Usando o bash do Linux, como exemplo, você pode utilizar

    $ python3 .../folha_mat.py

Para printar os títulos das matérias na página da Folha de SP. Ou utilizar

    $ python3 .../folha_mat.py i

Cujo `i` é um inteiro, para abrir a página da i-ésima matéria.

Caso você queira ler a matéria direto no terminal, utilize

    $ python3 .../folha_mat.py i -l

## Quero adicionar
* ~~Um scrap do conteúdo da matéria para ser lida direto no terminal~~
* Uma maneira de encontrar máterias com palavras específicas

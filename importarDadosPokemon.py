
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request('https://pokemondb.net/pokedex/all', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html5lib')
list_item = soup.find_all('a', attrs={'class': 'ent-name'})
name = list_item
lista = [a.get_text() for a in name]
lista1 = []
j =1

for i in range(len(lista)-1):
    if lista[i] != lista[i+1]:
        lista1.append(str(j)+";"+lista[i]+"\n")
        j+=1
lista1.append(str(j)+";"+lista[i])

data = "".join(lista1)

listaPokemon = open("Lista de Pokemon.csv", "w",encoding='utf-8')
listaPokemon.write("Lista de Pokemon:\n" + "Numero;Nome\n" + data)
listaPokemon.close()



#Jako stronę utworzę listę która będzie posiadała w sobie 5 mniejszych list i każda z nich będzie miała 2 elementy: wartość i częstotliwość
import random
SEED = 44
random.seed(SEED)

"""W eksperymencie pierwszym generujemy 150 procesów o małych wartościach z przedziału od 1 do 10 dla 5 stron pamięci."""
def eksperyment1(liczba):
    lista_procesow = []
    for i in range(1, liczba + 1):
        wartosc = random.randint(1, 10)
        czestotliwosc = 1
        lista = [wartosc, czestotliwosc]
        lista_procesow.append(lista)
    print("Lista procesów: ", lista_procesow)
    return lista_procesow

"""W eksperymencie drugim generujemy 200 procesów o średnich wielkościach wartości z przedziału od 1 do 10 dla 5 stron pamięci."""
def eksperyment2(liczba):
    lista_procesow = []
    for i in range(1, liczba + 1):
        wartosc = random.randint(1, 10)
        czestotliwosc = 1
        lista = [wartosc, czestotliwosc]
        lista_procesow.append(lista)
    print("Lista procesów: ", lista_procesow)
    return lista_procesow

"""W eksperymencie trzecim generujemy 250 procesów o dużych wielkościach wartości z przedziału od 1 do 10 dla 5 stron pamięci."""
def eksperyment3(liczba):
    lista_procesow = []
    for i in range(1, liczba + 1):
        wartosc = random.randint(1, 10)
        czestotliwosc = 1
        lista = [wartosc, czestotliwosc]
        lista_procesow.append(lista)
    print("Lista procesów: ", lista_procesow)
    return lista_procesow

"""W eksperymencie czwartym generujemy 250 procesów o małych wielkościach wartości z przedziału od 1 do 25 dla 5 stron pamięci."""
def eksperyment4(liczba):
    lista_procesow = []
    for i in range(1, liczba + 1):
        wartosc = random.randint(1, 25)
        czestotliwosc = 1
        lista = [wartosc, czestotliwosc]
        lista_procesow.append(lista)
    print("Lista procesów: ", lista_procesow)
    return lista_procesow

"""W eksperymencie piątym generujemy 250 procesów o średnich wielkościach wartości z przedziału od 1 do 8 dla 5 stron pamięci."""
def eksperyment5(liczba):
    lista_procesow = []
    for i in range(1, liczba + 1):
        wartosc = random.randint(1, 8)
        czestotliwosc = 1
        lista = [wartosc, czestotliwosc]
        lista_procesow.append(lista)
    print("Lista procesów: ", lista_procesow)
    return lista_procesow
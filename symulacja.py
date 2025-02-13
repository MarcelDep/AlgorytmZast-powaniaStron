from generatordanych import eksperyment1, eksperyment2, eksperyment3, eksperyment4, eksperyment5
from algorytmy_zmieniania_stron import LFU, MFU, LRU
def symulacja(dane, algorytm):
    #tworzymy słownik zawierący 5 elementów - te elementy będą naszymi stronami w symulacji
    strony = {
        'strona1': None,
        'strona2': None,
        'strona3': None,
        'strona4': None,
        'strona5': None,
    }
    ilosc_obecych_bledow = []
    #definiujemy zmienną informującą o tym w jakim czasie informacja zostałą dodana do pamięci
    ostatnie_uzycie = 0
    # definiujemy listę do której będziemy umieszczali błedy
    bledy = []
    #tworzymy pętle która będzie decydowała co zrobić z każdą informacją która "wejdzie" do pamięci, czy ją włoży w któreś puste miejsce
    #czy zwiększy częstowliwość jednego z elementów czy zastąpi inny element
    for indeks, (wartosc, czestotliwosc) in enumerate(dane):
        #zwiększamy czas w którym proces wpadł do pamięci dla każdego nowego procesu
        ostatnie_uzycie += 1
        #wprowadzamy zmienną informującą nas o tym ile jest pustych stron po to, żeby później móc wykonywać pewną część procesu, aż
        #zapełnią się wszystkie strony
        ilosc_pustych_stron = len([podslownik for podslownik in strony.values() if podslownik is None])

        #jeżeli pustych stron jest więcej od 0 to każda informacja jaka wpadnie do pamięci umiesczamy w miejsce strony, jeżeli dana o danej
        #wartości istnieje już w którejś ze stron to zwiększymy jego częstotliwość
        if ilosc_pustych_stron > 0:
            for strona, podslownik in strony.items():
                if podslownik is not None and podslownik[0] == wartosc:
                    podslownik[1] += 1
                    podslownik[2] = ostatnie_uzycie
                    break
                elif podslownik is None:
                    strony[strona] = [wartosc, czestotliwosc, ostatnie_uzycie]
                    bledy.append([wartosc, czestotliwosc, ostatnie_uzycie])
                    blad_z_indeksem = [indeks, len(bledy)]
                    ilosc_obecych_bledow.append(blad_z_indeksem)
                    break
        #jeżeli ilość pustych stron jest równa 0 to przechodzimy do drugiej części naszego algorytmu zastępowania stron
        else:
            #ponownie sprawdzamy czy dany element jest już w stronie czy nie, jeżeli jest to zwiększamy jego częstotliwość
            for strona, podslownik in strony.items():
                if podslownik[0] == wartosc:
                    podslownik[1] += 1
                    podslownik[2] = ostatnie_uzycie
                    break
            #jeżeli naszego elementu nie ma w stronach to:
            else:
                #w zależności od algorytmu podejmujemy decyzję o tym jaką stronę zastapić: dla LFU i MFU sprawdzimy częstotliwości procesów
                #w stronach i do zastąpienia wybierzemy kolejno stronę z najmniejszą i największą częstotliwością. Natomiast dla FIFO wybierzemy
                #tę stronę, w której najwcześniej została umieszczona jakaś informacja
                if algorytm == LFU:
                    LFU(strony, bledy, wartosc, czestotliwosc, ostatnie_uzycie, ilosc_obecych_bledow, indeks)
                elif algorytm == MFU:
                    MFU(strony, bledy, wartosc, czestotliwosc, ostatnie_uzycie, ilosc_obecych_bledow, indeks)
                else:
                    LRU(strony, bledy, wartosc, czestotliwosc, ostatnie_uzycie, ilosc_obecych_bledow, indeks)

    print("Ostatnie strony jakie zostały po symulacji:", strony)
    print("Błędy które wystąpiły podczas symulacji:", bledy)
    print("Indeksy błedów, i numer błedu:", ilosc_obecych_bledow)
    print("Ilość błędów:", len(bledy))
    return strony, bledy

x = eksperyment1(150)
print('')
print("_____________________________________________________________________")
print("Scenariusz pierwszy - generujemy 150 procesów wartościach z przedziału od 1 do 10 dla 5 stron.")
print("_____________________________________________________________________")
print('')
print("- Wyniki symulacji dla algorytmu LFU")
symulacja(x, LFU)
print('')
# print("- Wyniki symulacji dla algorytmu MFU")
# symulacja(x, MFU)
# print('')
# print("- Wyniki symulacji dla algorytmu LRU")
# symulacja(x, LRU)

# y = eksperyment2(200)
# print('')
# print("_____________________________________________________________________")
# print("Scenariusz drugi - generujemy 200 procesów wielkościach wartości z przedziału od 1 do 10 dla 5 stron pamięci.")
# print("_____________________________________________________________________")
# print('')
# print("- Wyniki symulacji dla algorytmu LFU")
# symulacja(y, LFU)
# print('')
# print("- Wyniki symulacji dla algorytmu MFU")
# symulacja(y, MFU)
# print('')
# print("- Wyniki symulacji dla algorytmu LRU")
# symulacja(y, LRU)

# z = eksperyment3(250)
# print('')
# print("_____________________________________________________________________")
# print("Scenariusz trzeci - 250 procesów o wielkościach wartości z przedziału od 1 do 10 dla 5 stron pamięci.")
# print("_____________________________________________________________________")
# print('')
# print("- Wyniki symulacji dla algorytmu LFU")
# symulacja(z, LFU)
# print('')
# print("- Wyniki symulacji dla algorytmu MFU")
# symulacja(z, MFU)
# print('')
# print("- Wyniki symulacji dla algorytmu LRU")
# symulacja(z, LRU)

# a = eksperyment4(250)
# print('')
# print("_____________________________________________________________________")
# print("Scenariusz czwarty - 250 procesów o wielkościach wartości z przedziału od 1 do 25 dla 5 stron pamięci.")
# print("_____________________________________________________________________")
# print('')
# print("- Wyniki symulacji dla algorytmu LFU")
# symulacja(a, LFU)
# print('')
# print("- Wyniki symulacji dla algorytmu MFU")
# symulacja(a, MFU)
# print('')
# print("- Wyniki symulacji dla algorytmu LRU")
# symulacja(a, LRU)

# b = eksperyment5(250)
# print('')
# print("_____________________________________________________________________")
# print("Scenariusz czwarty - 250 procesów o wielkościach wartości z przedziału od 1 do 8 dla 5 stron pamięci.")
# print("_____________________________________________________________________")
# print('')
# print("- Wyniki symulacji dla algorytmu LFU")
# symulacja(b, LFU)
# print('')
# print("- Wyniki symulacji dla algorytmu MFU")
# symulacja(b, MFU)
# print('')
# print("- Wyniki symulacji dla algorytmu LRU")
# symulacja(b, LRU)
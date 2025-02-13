#Algorytm LFU wybiera do zastąpienia tę stronę która ma najmnijeszą częstotliwość użycia (drugi parametr wartości słownika)
def LFU(strony, bledy, wartosc, czestotliwosc, ostatnie_uzycie, ilosc_obecych_bledow, indeks):
    #z wartości stron w słowniku wybieramy 2 element list (częstotliwość)
    czestotliwosci = [czestotliwosc_procesu[1] for czestotliwosc_procesu in strony.values()]
    #wybieramy najmniejszą wartość częstotliwości
    najmniejsza_czestotliwosc = min(czestotliwosci)
    #sprawdzamy ile jest list z najmniejszą częstowliwością spośród list w słowniku
    ilosc_najmniejszych_czestotliwosci = czestotliwosci.count(najmniejsza_czestotliwosc)
    if ilosc_najmniejszych_czestotliwosci > 1:
        #jeżeli mamy więcej niż jedną listę która ma najmniejszą częstotliwość, wybieramy z nich tę która ma najmniejszy czas przyjścia (LRU)
        strona_do_zastapienia1 = min(strony.items(), key=lambda item: (item[1][1], item[1][2]))
        #wybraną stronę zastępujemy stroną po której obecnie iterujemy i dodajemy ją do błędów (wcześniej sprawdzaliśmy czy się powtarza)
        strony[strona_do_zastapienia1[0]] = [wartosc, czestotliwosc, ostatnie_uzycie]
        bledy.append([wartosc, czestotliwosc, ostatnie_uzycie])
        blad_z_indeksem = [indeks, len(bledy)]
        ilosc_obecych_bledow.append(blad_z_indeksem)
        return strony, bledy, strona_do_zastapienia1, ilosc_obecych_bledow
    else:
        #jeżeli mamy tylko jeden element o najmniejszej częstotliwości to go zastępujemy
        strona_do_zastapienia2 = min(strony.items(), key=lambda item: item[1][1])
        # wybraną stronę zastępujemy stroną po której obecnie iterujemy i dodajemy ją do błędów (wcześniej sprawdzaliśmy czy się powtarza)
        strony[strona_do_zastapienia2[0]] = [wartosc, czestotliwosc, ostatnie_uzycie]
        bledy.append([wartosc, czestotliwosc, ostatnie_uzycie])
        blad_z_indeksem = [indeks, len(bledy)]
        ilosc_obecych_bledow.append(blad_z_indeksem)
        return strony, bledy, strona_do_zastapienia2, ilosc_obecych_bledow


#Algorytm MFU wybiera do zastąpienia tę stronę która ma największą częstotliwość użycia (drugi parametr wartości słownika)
def MFU(strony, bledy, wartosc, czestotliwosc, ostatnie_uzycie, ilosc_obecych_bledow, indeks):
    # z wartości stron w słowniku wybieramy 2 element list (częstotliwość)
    czestotliwosci = [czestotliwosc_procesu[1] for czestotliwosc_procesu in strony.values()]
    # wybieramy największą wartość częstotliwości
    najwieksza_czestotliwosc = max(czestotliwosci)
    # sprawdzamy ile jest list z największą częstowliwością spośród list w słowniku
    ilosc_najwiekszych_czestotliwosci = czestotliwosci.count(najwieksza_czestotliwosc)
    if ilosc_najwiekszych_czestotliwosci > 1:
        # jeżeli mamy więcej niż jedną listę która ma największą częstotliwość, wybieramy z nich tę która ma najmniejszy czas przyjścia (LRU)
        strona_do_zastapienia1 = min(strony.items(), key=lambda item: (-item[1][1], item[1][2]))
        # wybraną stronę zastępujemy stroną po której obecnie iterujemy i dodajemy ją do błędów (wcześniej sprawdzaliśmy czy się powtarza)
        strony[strona_do_zastapienia1[0]] = [wartosc, czestotliwosc, ostatnie_uzycie]
        bledy.append([wartosc, czestotliwosc, ostatnie_uzycie])
        blad_z_indeksem = [indeks, len(bledy)]
        ilosc_obecych_bledow.append(blad_z_indeksem)
        return strony, bledy, strona_do_zastapienia1, ilosc_obecych_bledow
    else:
        # jeżeli mamy tylko jeden element o najmniejszej częstotliwości to go zastępujemy
        strona_do_zastapienia2 = max(strony.items(), key=lambda item: item[1][1])
        # wybraną stronę zastępujemy stroną po której obecnie iterujemy i dodajemy ją do błędów (wcześniej sprawdzaliśmy czy się powtarza)
        strony[strona_do_zastapienia2[0]] = [wartosc, czestotliwosc, ostatnie_uzycie]
        bledy.append([wartosc, czestotliwosc, ostatnie_uzycie])
        blad_z_indeksem = [indeks, len(bledy)]
        ilosc_obecych_bledow.append(blad_z_indeksem)
        return strony, bledy, strona_do_zastapienia2, ilosc_obecych_bledow

#Algorytm LRU wybiera do zastąpienia tę stronę która najwcześniej została umieszczona w pamięci RAM (trzeci parametr wartości słownika)
def LRU(strony, bledy, wartosc, czestotliwosc, ostatnie_uzycie, ilosc_obecych_bledow, indeks):
    #z wartości stron w słowniku wybieramy tę stronę która ma najmniejszy czas przyjścia - 3 element listy
    strona_do_zastapienia3 = min(strony.items(), key=lambda item: item[1][2])
    # wybraną stronę zastępujemy stroną po której obecnie iterujemy i dodajemy ją do błędów (wcześniej sprawdzaliśmy czy się powtarza)
    strony[strona_do_zastapienia3[0]] = [wartosc, czestotliwosc, ostatnie_uzycie]
    bledy.append([wartosc, czestotliwosc, ostatnie_uzycie])
    blad_z_indeksem = [indeks, len(bledy)]
    ilosc_obecych_bledow.append(blad_z_indeksem)
    return strony, bledy, strona_do_zastapienia3, ilosc_obecych_bledow
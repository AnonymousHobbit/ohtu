from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []

    def tavaroita_korissa(self):
        print(self.kori)
        return len(self.kori)

    def hinta(self):
        # return price of all items in the cart
        return sum([ostos.hinta() for ostos in self.kori])

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen ostoskoriin
        # jos tuote on jo korissa, lisää tuotteen määrää yhdellä
        
        # if the item is already in the cart, increase the quantity by 1
        if lisattava in [ostos.tuote for ostos in self.kori]:
            for ostos in self.kori:
                if ostos.tuote == lisattava:
                    ostos.muuta_lukumaaraa(1)
        else:
            self.kori.append(Ostos(lisattava))
        

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on

        return self.kori

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
        if lisattava in [ostos.tuote for ostos in self.kori]:
            for ostos in self.kori:
                if ostos.tuote == lisattava:
                    ostos.muuta_lukumaaraa(1)
        else:
            self.kori.append(Ostos(lisattava))
        

    def poista_tuote(self, poistettava: Tuote):
        if poistettava in [ostos.tuote for ostos in self.kori]:
            for ostos in self.kori:
                if ostos.tuote == poistettava:
                    ostos.muuta_lukumaaraa(-1)
                    if ostos.lukumaara() == 0:
                        self.kori.remove(ostos)
                    


    def tyhjenna(self):
        self.kori = []

    def ostokset(self):
        return self.kori

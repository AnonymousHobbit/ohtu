import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):

        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipa", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta(self):
            
            maito = Tuote("Maito", 3)
            leipa = Tuote("Leipa", 2)
    
            self.kori.lisaa_tuote(maito)
            self.kori.lisaa_tuote(leipa)
    
            self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta(self):

        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")

        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):

        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipa", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):

        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_jos_korissa_oleva_tuote_poistetaan_korista_korissa_ei_ole_enaa_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)

    def test_jos_korissa_oleva_tuote_poistetaan_korista_korissa_on_yksi_jaljella(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].lukumaara(), 1)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kori_voidaan_tyhjentaa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)

    

    



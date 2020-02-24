import unittest

from ykbl import Samaj


class RutojtobenïkSamaj(unittest.TestCase):
    @classmethod
    def setUpClass(rwch):
        rwch.samaj = Samaj('ruxeeltzij')

    def test_retal_jaloj(ri):
        ri.assertSetEqual(ri.samaj.retal_jaloj, {"Tz'ujal chirij ulew"})

    def test_rejqalem(ri):
        print(ri.samaj.rejqalem("Tz'ujal chirij ulew"))
        ri.samaj.rejqalem("Jun retal jaloj k'o ka'i' taq ruxe'el tzij")
        ri.samaj.runimilem("Retal jaloj")
        ri.samaj.rejqalem("retal jaloj", chupam="")
        ri.samaj.rejqalem("retal jaloj", chupam="", stricte=True)
        ri.samaj.rejqalem("retal jaloj", chupam="Pan Ajache'l")
        ri.samaj.rejqalem("retal jaloj", chupam="Panajachel")
        ri.samaj.rejqalem("retal jaloj", chupam="701")
        ri.samaj.rejqalem("retal jaloj", chupam=701)

        ri.samaj.rejqalem("retal jaloj", periodo="", )
        ri.samaj.rejqalem("retal jaloj", qij="", )

        ri.samaj.rejqalem("mismo variable en español")
        ri.samaj.rejqalem("rïn man in ta jun retal jaloj")

        ri.samaj.rejqalem("retal jaloj moltz'ïk", chupam=(lat, lon))
        ri.samaj.rejqalem("retal jaloj moltz'ïk", chupam="Loya'")
        ri.samaj.rejqalem("retal jaloj moltz'ïk", chupam='Tinamït')  # rub'i' setul shp

        ri.samaj.rejqalem("retal jaloj shp", chupam=(lat, lon))
        ri.samaj.rejqalem("retal jaloj shp", chupam=(lat2, lon2))  # Interpolation (kriging)
        ri.samaj.rejqalem("retal jaloj shp", chupam="Loya'")  # ¿Interpolation (kriging)?

        # retal jaloj man xtzibaxïk ta chupam samaj
        # k'olib'äl man k'o ta chupam setul

        #
        tojtobenïk = Tojtobenïk(We().KaRi())
        ri.samaj.tojtobenïk()
        # --> Retal jaloj man xok ta chupam choltzij
        # --> Retal jaloj man nok ta kejqalem chupam kik'ulb'at

        setul.kolibäl
        setul.chupam("K'olibäl")

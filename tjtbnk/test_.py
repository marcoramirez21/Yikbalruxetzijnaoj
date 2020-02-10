import unittest

from ykbl import Samaj


class RutojtobenïkSamaj(unittest.TestCase):
    @classmethod
    def setUpClass(rwch):
        rwch.samaj = Samaj('ruxeeltzij')

    def test_retal_jaloj(ri):
        ri.assertSetEqual(ri.samaj.retal_jaloj, {"Tz'ujal chirij ulew"})

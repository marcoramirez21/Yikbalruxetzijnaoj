from atitlán.rtljlj import kichelaj
from ykbl import RuxeelTzijMoltzïk, CholanilRuxakMoltzïk, RetamabälRuxeelTzij

retamabäl = RetamabälRuxeelTzij(
    qijxjunimaxïk="21-2-2020",
    xjunumaxïkroma="جسيكا بو نصّار",
    tzibanel="IARNA-URL",
    ruqijlem=None,
    tzijowäch="Rukusaxïk ulew pa ri junab' 2012."
)
ruxak = CholanilRuxakMoltzïk(
    """
    "Ruk'u'x tinamït": 1,
    "": 4,
    "Ya'": 5,
    "Juna'il tiko'n": 21,
    "": 23,
    "Xolon taq tiko'n": 24,
    "": 33,
    "": 221,
    "": 223,
    "Kok'ol taq che": 230,
    "Ri'il taq che'": 231,
    "Kape'": 233,
    "Kik'ache'": 234,
    "K'i'p richin Aprika": 235,
    "Aji'j": 236,
    "Tiko'n": [21, 23, 24, 221, 223, 233, 234, 235, 236],
    """

    '1', tununem={
        Tn(kichelaj, 3),
        Tn(che, [3, 223, 233, 234, 235])
    }
)

rukusaxïkulew2012 = RuxeelTzijMoltzïk(
    "Rukusaxïk ulew pa 2012",
    rochochibäl='clipped_landuse_2012_iarna.tif.aux/clipped_landuse_2012_iarna.tif',
    ruxak=ruxak, retamabäl=retamabäl,
    ramaj=2012
)

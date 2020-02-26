import os

from atitlán.rtljlj import kichelaj, che, tikon, kokoltaqche
from ykbl import RuxeelTzijMoltzïk, CholanilRuxakMoltzïk, RetamabälRuxeelTzij
from ykbl.ruxeeltzij.moltzïk import TununemRetalJalojCholanilMolztïk as Tn


retamabäl = RetamabälRuxeelTzij(
    qijxjunimaxïk="21-2-2020",
    xjunumaxïkroma="جسيكا بو نصّار",
    tzibanel="IARNA-URL",
    ruqijlem=None,
    tzijowäch="Rukusaxïk ulew pa ri junab' 2012."
)
"""

4 zonas humedales
23 pastizales

33 espacios abiertos, sin o con poco vegetacion
221 cultivos permanentes herbaceos
223 cultivos permanentes arboreos

"Ruk'u'x tinamït": 1,
"": 4,
"Ya'": 5,
"Juna'il tiko'n": 21,
"": 23,
"Xolon taq tiko'n": 24,
"": 33,
"": 221,
"": 223,
"Ri'il taq che'": 231,
"Kape'": 233,
"Kik'ache'": 234,
"K'i'p richin Aprika": 235,
"Aji'j": 236,
"""

ruxak = CholanilRuxakMoltzïk(
    '1',
    tununem={
        Tn(kichelaj, 3),
        Tn(che, [3, 223, 233, 234, 235]),
        Tn(kokoltaqche, 230),
        Tn(tikon, [21, 23, 24, 221, 223, 233, 234, 235, 236])
    }
)

rukusaxïkulew2012 = RuxeelTzijMoltzïk(
    "Rukusaxïk ulew pa 2012",
    rochochibäl=os.path.join(os.path.dirname(__file__), 'rukusaxïk_ulew_2012.tif'),
    ruxak=ruxak, retamabäl=retamabäl,
    ramaj=2012
)

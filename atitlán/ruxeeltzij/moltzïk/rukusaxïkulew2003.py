import os

from atitlán.rtljlj import kichelaj, che, tikon, kokoltaqche
from ykbl import RuxeelTzijMoltzïk, CholanilRuxakMoltzïk, RetamabälRuxeelTzij
from ykbl.ruxeeltzij.moltzïk import TununemRetalJalojCholanilMolztïk as Tn

"""
1	Granos básicos
2	Arbustos - matorrales
3	Bosque mixto
4	Bosque conífero
5	Pastos naturales y/o yerbazal
7	Hortaliza - ornamental
9	Centros poblados
10	Mosaico de cultivos
11	Aguacate
12	Café
13	Bosque latifoliado
14	Playa y/o arena
15	Lago - laguna
17	Arena y/o material piroclástic
"""

retamabäl = RetamabälRuxeelTzij(
    qijxjunimaxïk="21-2-2020",
    xjunumaxïkroma="جسيكا بو نصّار",
    tzibanel=None,
    ruqijlem=None,
    tzijowäch="Rukusaxïk ulew pa ri junab' 2003."
)

ruxak = CholanilRuxakMoltzïk(
    '1',
    tununem={
        Tn(kokoltaqche, 2),
        Tn(kichelaj, [3, 4, 13]),
        Tn(che, [3, 4, 13, 11, 12]),
        Tn(tikon, [1, 7, 10, 11, 12])
    }
)

rukusaxïkulew2003 = RuxeelTzijMoltzïk(
    "Rukusaxïk ulew pa 2003",
    rochochibäl=os.path.join(os.path.dirname(__file__), 'rukusaxïk_ulew_2003.tif'),
    ruxak=ruxak, retamabäl=retamabäl,
    ramaj=2003
)

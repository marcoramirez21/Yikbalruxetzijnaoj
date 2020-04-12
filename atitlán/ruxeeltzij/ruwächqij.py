import os

from atitlán.rtljlj import ruwächqij_retal_jaloj_DICA_AMSCLAE
from ykbl import RuxeelTzijCSV, RetamabälRuxeelTzij, TununemRetalJaloj
from ykbl.ruxeeltzij.csv_ import RucheelRamaj

#ToDo: Create retamabäls and RuxeelTzij Objects for all variables in the DICA-AMSCLAE FILES.
#ToDo: Figure out the correct date-string format string for the DICA-AMSCLAE FILES.


retamabälRuwächQij = RetamabälRuxeelTzij(
    qijxjunimaxïk="10-04-2020", xjunumaxïkroma="جسيكا بو نصّار", tzibanel=None
)

rxltzjRuwächQij = RetamabälRuxeelTzij(
    "",
    rochochibäl=os.path.join(os.path.dirname(__file__), "csv/DATOS CLIMATICOS DICA-AMSCLAE-Barreneche-2011.csv"), retamabäl=retamabäl,
    kolibäl=None, ramaj=RucheelRamaj(rucheel="Date", rubeyal="%Y%m"),
    tununem=TununemRetalJaloj(tzujalchirijulew, rucheel='mm', junilal='mm')
)
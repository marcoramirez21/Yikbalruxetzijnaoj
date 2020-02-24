from atitlán.rtljlj import tzujalchirijulew
from ykbl import RuxeelTzijCSV, RetamabälRuxeelTzij, TununemRetalJaloj
from ykbl.ruxeeltzij.csv_ import RucheelRamaj

retamabäl = RetamabälRuxeelTzij(
    qijxjunimaxïk="10-2-2020", xjunumaxïkroma="جسيكا بو نصّار", tzibanel=None
)

rxltzj = RuxeelTzijCSV(
    "Tz'ujal chirij ulew",
    rochochibäl="csv/Atitlan_Runoff.csv", retamabäl=retamabäl,
    kolibäl=None, ramaj=RucheelRamaj(rucheel="Date", rubeyal="%Y%m"),
    tununem=TununemRetalJaloj(tzujalchirijulew, rucheel='mm', junilal='mm')
)

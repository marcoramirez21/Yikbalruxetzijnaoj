import os

from atitlán.rtljlj import ruwächqij_retal_jaloj_DICA_AMSCLAE, nevada, jab
from ykbl import RuxeelTzijCSV, RetamabälRuxeelTzij, TununemRetalJaloj
from ykbl.ruxeeltzij.csv_ import RucheelRamaj

# ToDo: Create retamabäls and RuxeelTzij Objects for all variables in the DICA-AMSCLAE FILES.
# ToDo: Figure out the correct date-string format string for the DICA-AMSCLAE FILES.
# ToDo: Automate the reading of the weather files for all years and stations of DICA-AMSCLAE.
"""
Estaciones Climáticas:
Barreneche
El Tablon
Finca Santa Victoria
Los Saminez
Pamesebal
Panajachel
San Jose Chacaya
San Juan La Laguna
San Lucas Toliman
Santa Lucia Utatlan
Santiago Atitlan


"""
retamabälRuwächQij = RetamabälRuxeelTzij(
    qijxjunimaxïk="10-04-2020", xjunumaxïkroma="Joel Z. Harms", tzibanel=
    "Autoridad Para el Manejo Sustentable de la Cuenca del Lago Atitlan y su Entorno (AMSCLAE)"
    " Departamento de Investigacion y Calidad Ambiental (DICA)"
)

headers_DICA_AMSCLAE = ["Temp. Min. Abs. (°C)", "Temp. Prom (°C)", "Temp. Max Abs. (°C)", "Hum. (%)",
                        "Precipitacion (mm)", "Rad. Solar (W/m2)", "Rad. Solar Max Abs.(W/m2)",
                        "Indice UV (Unidad)", "Indice UV Max Abs. (Unidad)", "Direccion Viento Max",
                        "Velocidad Viento Max. (km/h)"]

tununemRuwächQij_DICA_AMSCLAE = [TununemRetalJaloj(ruwächqij_retal_jaloj_DICA_AMSCLAE[i],
                                                   headers_DICA_AMSCLAE[i],
                                                   ruwächqij_retal_jaloj_DICA_AMSCLAE[i].junilal)
                                 for i in range(0, len(ruwächqij_retal_jaloj_DICA_AMSCLAE))]

rxltzjRuwächQij = RuxeelTzijCSV(
    "",# add name here
    rochochibäl=os.path.join(os.path.dirname(__file__), "csv/DATOS CLIMATICOS DICA-AMSCLAE-Barreneche-2011.csv"),
    retamabäl=retamabälRuwächQij,
    kolibäl=None, ramaj=RucheelRamaj(rucheel="Mes", rubeyal="%Y-%m-%d"),
    tununem=tununemRuwächQij_DICA_AMSCLAE
)

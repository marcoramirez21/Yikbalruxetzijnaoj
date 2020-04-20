import os

from atitlán.rtljlj import ruwächqij_retal_jaloj_DICA_AMSCLAE, nevada, jab
from ykbl import RuxeelTzijCSV, RetamabälRuxeelTzij, TununemRetalJaloj
from ykbl.ruxeeltzij.csv_ import RucheelRamaj

"""
Estaciones Climáticas:
Barreneche: 14.826742, -91.220013 (422,514.00, 1,639,619.00)
El Tablon:  14.797717, -91.181482 (426,653.00, 1,636,400.00)
Finca Santa Victoria 
Los Saminez
Pamesebal
Panajachel (429,740.00, 1,630,030.00)
San Jose Chacaya (423,012.00, 1,633,566.00)
San Juan La Laguna (415,227.00, 1,625,033.00)
San Lucas Toliman (430,826.00, 1,618,247.00)
Santa Lucia Utatlan (417,487.00, 1,633,474.00)
Santiago Atitlan (421,129.00, 	1,619,029.00)
"""
janilaCholRetalJaloj = [cholRetalJaloj
      for cholRetalJaloj in os.listdir("C:\\Users\\Joel\\PycharmProjects\\Yikbalruxetzijnaoj\\atitlán\\ruxeeltzij\csv")
      if "DATOS CLIMATICOS DICA-AMSCLAE" in cholRetalJaloj]

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
                                                   rucheel=headers_DICA_AMSCLAE[i],
                                                   junilal=ruwächqij_retal_jaloj_DICA_AMSCLAE[i].junilal)
                                 for i in range(0, len(ruwächqij_retal_jaloj_DICA_AMSCLAE))]



rxltzjRuwächQij = [RuxeelTzijCSV(
    (cholRetalJaloj.split("-")[2]+cholRetalJaloj.split("-")[3]).split(".")[0],
    rochochibäl=os.path.join(os.path.dirname(__file__), "csv/"+ cholRetalJaloj),
    retamabäl=retamabälRuwächQij,
    kolibäl=None, ramaj=RucheelRamaj(rucheel="Día", rubeyal="%Y-%m-%d"),
    tununem=tununemRuwächQij_DICA_AMSCLAE) for cholRetalJaloj in janilaCholRetalJaloj]

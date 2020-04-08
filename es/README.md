# Yikbalruxetzijnaoj
Es un repositorio central de datos para la modelización del lago Atitlán.  

**Esta es una traducción al castellano de la documentación prelimiaria de este repositorio.**

## Extracción de valores de variables
Se pueden extraer los valores de los variables para un lugár específico, tanto como para cada polígono de un mapa.
Seguir leyendo para ver cómo se especifica variables, mapas y bases de datos.

```python
# Obtener la cobertura de árboles para cada municipio de la cuenca
miproyecto.rejqalem(árboles, Munis)

# Se pueden pedir los resultados en otro idioma
miproyecto.tatzijoj(["español", "Tz'utujil", "Kaqchikel"])
miproyecto.rejqalem(árboles, Munis)

# Solamente devolver datos para Pan Ajache'l y Tz'ikinajay
miproyecto.rejqalem(árboles, Munis[["Pan Ajache'l", "Tz'ikinajay"]])
```

## Variables
Se agregan datos con los cuales quiere trabajar.

```python
from ykbl import RetalJaloj as Variable

árboles = Variable("Árboles", kulbat=(0, None), junilal='ha')
temp = Variable("Temperatura", kulbat=None, junilal='C')
lluvia = Variable("Lluvia", kulbat=(0, None), junilal='cm')

# También se pueden especificar variables en varios idiomas
agricultura = Variable({
        "Kaqchikel": "Tiko'n", "español": "Agricultura"
    }, kulbat=(0, None), junilal='ha'
)

variables = [árboles, temp, lluvia, agricultura]

```

## Bases de datos
Se pueden conectar datos en formato CSV o Raster.
Al conectar una base de datos, hay que especificar sus metadatos (`ykbl.RetamabälRuxeelTzij`)
con el autor, su licencia, etc.

### Datos CSV
```python
from ykbl import RuxeelTzijCSV as DatosCSV, RetamabälRuxeelTzij as Metadatos, TununemRetalJaloj as ConexiónVariable
from ykbl.ruxeeltzij.csv_ import RucheelRamaj as ColumnaTiempo

meta = Metadatos(
    qijxjunimaxïk="10-2-2020", xjunumaxïkroma="Usted", tzibanel=None
)

datos = DatosCSV(
    "BD Temperatura",
    rochochibäl="mis datos/temperatura.csv", retamabäl=meta,
    kolibäl=None, ramaj=ColumnaTiempo(rucheel="Día", rubeyal="%Y%m"),
    tununem=[ConexiónVariable(temperatura, rucheel='tewktnl', junilal='K')]
)

```
El objeto `ConexiónVariable` (`TununemRetalJaloj`) especifica la conexión entre el `Variable` (`RetalJaloj`) y los 
`DatosCSV` (`RuxeelTzijCSV`). Las unidades se convertirán de manera automática en el caso que no sean iguales entre
la base de datos y la especificación del variable.

Si los datos del CSV se refieren a únicamente una fecha o lugar, se pueden especificar allí. Si al contrario se
se especificarón en una columna del CSV, los puede identificar con una `ColumnaTiempo` (`RucheelRamaj`) o una
`ColumnaLugar` (`RucheelKolibäl`).

### Datos raster
Hay dos formas de datos raster, los categóricos y los numéricos. Además, un archivo raster (como `.tif`) puede 
contener varias hojas de datos. Se dará como ejemplo abajo una base de datos con dos hojas, una categórica y la otra
numérica.

Cuando se extraen datos de unos DatosRaster (`MoltzïkRuxeelTzij`), se debe aplicar un mapa `.shp` (ver ejemplo abajo).
``ykbl`` identificará los puntos del raster que caen adentro de cada polígono del mapa, y calculará los valores de los
variables según estos puntos.

```python
from ykbl import RuxeelTzijMoltzïk as DatosRaster, CholanilRuxakMoltzïk as HojaRasterCateg, CholajilRuxakMoltzïk as HojaRasterNum, RetamabälRuxeelTzij as Metadatos
from ykbl.ruxeeltzij.moltzïk import TununemRetalJalojCholanilMolztïk as CnxVarCateg, TununemRetalJalojCholajilMolztïk as CnxVarNum


meta = Metadatos(
    qijxjunimaxïk="21-2-2020",
    xjunumaxïkroma="yo",
    tzibanel="nosotres",
    ruqijlem=None
)

hoja1 = HojaRasterCateg(
    '1',
    tununem={
        CnxVarCateg(árbol, 3),  # 3 es el código para árboles en el .tif

        # Si una categoría tiene varios códigos, se pueden incluir en forma de lista
        CnxVarCateg(agricultura, [3, 4, 5])
    }
)

hoja2 = HojaRasterNum(
    '2',
    tununem={
        CnxVarNum(lluvia, junilal='mm')
    }
)

usodetierra2012 = DatosRaster(
    "Otra base de datos",
    rochochibäl='mimaparaster.tif',
    ruxak=[hoja1, hoja2], retamabäl=meta,
    ramaj=2012
)
```


## Proyecto
Por fin, combinamos todo en un `Proyecto` (`Samäj`):

```python

from ykbl import Samäj as Proyecto
miproyecto = Proyecto(retal_jaloj=variables, ruxeel_tzij=bases_de_datos)

```

## Mapa
Se especifica la geografía del proyecto con un mapa.

```python

from ykbl.setul import SetulShp as MapaShp, RucheelPeraj as ColumnaSuperficie

lugares = {
    '701': {'Kaqchikel': "Tz'olöj Ya'", 'español': 'Sololá'},
    '702': {'Kaqchikel': "Chaqaya'", 'español': 'San José Chacayá'},
    # ...
    '710': {'Kaqchikel': "Pan Ajache'l", 'español': 'Panajachel'},
    '711': {'Kaqchikel': "Kata'l Po'j", 'español': 'Santa Catarina Palopó'},
    '712': {'Kaqchikel': "Antun Po'j", 'español': 'San Antonio Palopó'},
    '713': {'Kaqchikel': "Loya'", 'español': 'San Lucas Tolimán'},
    # ...
    '717': {'Kaqchikel': "Xe' Kuku' Ab'äj", 'español': 'San Juan La Laguna', "Tz'utujil": "Xe' Kuku' Aab'aj"},
    '718': {'Kaqchikel': "Tzunun Ya'", 'español': 'San Pedro La Laguna'},
    '719': {'Kaqchikel': "Tz'ikinajay", 'español': 'Santiago Atitlán'}
}

Munis = MapaShp(
    'Munis',
    'mimapa.shp',
    rucheel_etal='COD_MUNI',
    # Si no hay columna con áreas precalculados, no hay problema; `ykbl` lo calculará sí mismo 
    rucheel_peraj=ColumnaSuperficie('HECTARES', 'ha'),
    kolibäl=lugares
)

```

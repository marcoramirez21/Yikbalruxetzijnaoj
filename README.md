# Yikbalruxetzijnaoj
Jawra k'olib'al rxin yikb'al ruxe'tzij na'ouj rxin k'utb'al samaj konxik tzrij Ya' Atitlán.  

## Retal jaloj
Nab'ey tajunumaj ri taq retal jaloj achojik'in nawajo nasamaj.

```python
from ykbl import RetalJaloj

che = RetalJaloj("Che'", kulbat=(0, None), junilal='ha')
tewkatanil = RetalJaloj("Tewk'atanil", kulbat=None, junilal='C')
jab = RetalJaloj("Jab'", kulbat=(0, None), junilal='cm')

# Yatkowin naya rub'i' pa k'iy taq ch'ab'äl chuqa'
tikon = RetalJaloj({
        "Kaqchikel": "Che'", "español": "Árboles"
    }, kulbat=(0, None), junilal='ha'
)

retal_jaloj = [che, tikon, tewkatanil, jab]

```

## Ruxe'el tzij
K'o ka'i' taq kiwäch ruxe'el tzij, CSV chuqa' moltzïk (richin setul).
Toq najunumaj jun ruxe'el tzij, k'o chi naya' retamab'äl (`ykbl.RetamabälRuxeelTzij`)
nuya' rutz'ib'anel, ruq'ijlem, ...

### CSV taq ruxe'el tzij

```python
from ykbl import RuxeelTzijCSV, RetamabälRuxeelTzij, TununemRetalJaloj
from ykbl.ruxeeltzij.csv_ import RucheelRamaj

retamabäl = RetamabälRuxeelTzij(
    qijxjunimaxïk="10-2-2020", xjunumaxïkroma="rat", tzibanel=None
)

rxltzj = RuxeelTzijCSV(
    "Tewk'atanil",
    rochochibäl="tewk'atanil.csv", retamabäl=retamabäl,
    kolibäl=None, ramaj=RucheelRamaj(rucheel="Q'ij", rubeyal="%Y%m"),
    tununem=[TununemRetalJaloj(tewkatanil, rucheel='tewktnl', junilal='K')]
)

```
Ri `TununemRetalJaloj` nub'ij achike rub'eyal xtijunumaxïk ri `RetalJaloj` rik'in ri 
`RuxeelTzijCSV`. Xtik'exwachixïk ri junilal awoma we man junan ta ri junilal ri
ruxe'el tzij rik'in ri junilal ri retal jaloj.

We xajun ramaj o k'olib'äl k'o chupam aCSV, yattikïr naya' kela'. We
xtz'ib'axïk kik'olibäl/kiramaj konojel taq cholaj chupam jun chïk ruche'el ruxe'el atzij,
yatkowin naya' jun `RucheelRamaj` chuqa' jun `RucheelKolibäl`.

### Moltzïk taq ruxe'el tzij
K'o ka'i' taq kiwäch retal jaloj richin moltzïk, cholajil chuqa' cholanil.
Jun moltzïk ruxe'el tzij (achi'el `.tif`) yetikïr ye'ok jujun taq ruxak chupam.
Roma tz'eb'äl, xkojsamaj rik'in jun ruxe'el tzij k'o ka'i' taq ruxak, jun cholajil
chuqa' jun cholanil. 

Toq natelesaj kirejqalem retal jaloj richin jun `MoltzïkRuxeelTzij`, k'o chi naya' 
jun setul `.shp` chire (tatz'eta' wawe chuxe). ``ykbl`` xtitz'u achike taq tzïk richin
moltzïk ye'ok chupam konojel taq k'iyatz'uk k'o chupam asetul, k'a ri' xtajilaj 
kirejqalem retal jaloj kik'in re tzïk re'. 

```python
from ykbl import RuxeelTzijMoltzïk, CholanilRuxakMoltzïk, CholajilRuxakMoltzïk, RetamabälRuxeelTzij
from ykbl.ruxeeltzij.moltzïk import TununemRetalJalojCholanilMolztïk as TnChln, TununemRetalJalojCholajilMolztïk as TnChlj


retamabäl = RetamabälRuxeelTzij(
    qijxjunimaxïk="21-2-2020",
    xjunumaxïkroma="rïn",
    tzibanel="roj",
    ruqijlem=None
)

ruxak1 = CholanilRuxakMoltzïk(
    '1',
    tununem={
        TnChln(che, 3),  # 3 runuk' richin che' chupam ri .tif

        # Toq k'iy taq runuk' jun peraj, yattikïr najunumaja' achi'el jun cholajem
        TnChln(tikon, [3, 4, 5])
    }
)

ruxak2 = CholajilRuxakMoltzïk(
    '2',
    tununem={
        TnChlj(jab, junilal='mm')
    }
)

rukusaxïkulew2012 = RuxeelTzijMoltzïk(
    "Jun chïk ruxe'el tzij",
    rochochibäl='nusetulmoltzïk.tif',
    ruxak=[ruxak1, ruxak2], retamabäl=retamabäl,
    ramaj=2012
)
```


## Samäj
Pa k'isb'äl, tajunumaj konojel chupam jun `Samäj`:

```python

from ykbl import Samäj
nusamaj = Samäj(retal_jaloj=retal_jaloj, ruxeel_tzij=ruxeel_tzij)

```

## Setul
Jun setul nub'ij chire `ykbl` kib'i' taq k'olib'äl pa asamaj.

```python

from ykbl.setul import SetulShp, RucheelPeraj

kolibäl = {
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

Tinamït = SetulShp(
    'Tinamït',
    'nusetul.shp',
    rucheel_etal='COD_MUNI',
    # We majun ta ruche'el richin peraj, majun k'ayew ta, `ykbl` xtajilaj awoma 
    rucheel_peraj=RucheelPeraj('HECTARES', 'ha'),
    kolibäl=kolibäl
)

```

## Relesaxïk kirejqalem retal jaloj
Yattikïr natelesaj kirejqalem retal jaloj richin jun k'olib'äl chuqa' kichin konojel taq
k'iyatz'uk chupam jun setul.

```python
nusamaj.rejqalem(che, nusetul)

# We nawajo' ri taq tzolitzij pa jun chïk ch'ab'äl
nusamaj.rejqalem(che, nusetul, chabäl="Tz'utujil")

# Xaxe kichin ri taq tinamït Pan Ajache'l chuqa Tz'ikinajay
nusamaj.rejqalem(che, nusetul[["Pan Ajache'l", "Tz'ikinajay"]])
```
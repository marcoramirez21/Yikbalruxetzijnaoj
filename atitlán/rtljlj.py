from ykbl import RetalJaloj
#ToDo: Sort variables in rucheel jaloj ruwäch q'ij according to DICA-AMSCLAE convention
#ToDo: Call Variables Monthly  "ik'" meaning month
etabälqij = RetalJaloj(
    {"Kaqchikel": "Etab'äl qi'j", "español": "Radiación Solar"}, kulbat=(0, None), junilal="W/(m*m)"
)
max_etabälqij = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Radiación Solar Maximal"}, kulbat=(0, None), junilal="W/(m*m)"
)
max_temp = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Temperatura Maximal"}, kulbat=(0, None), junilal="°C"
)
min_temp = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Temperatura Minimal"}, kulbat=(0, None), junilal="°C"
)
prom_temp = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Temperatura Prom."}, kulbat=(0, None), junilal="°C"
)
etabälräxkaqïq = RetalJaloj(
    {"Kaqchikel": "Etab'äl räx kaq’ïq", "español": "Humedad"}, kulbat=(0, None), junilal="%"
)
indiceUV = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Indice UV"}, kulbat=(0, None), junilal=None
)
max_indiceUV = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Indice UV Maximal"}, kulbat=(0, None), junilal=None
)
max_apokaqïq = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Direccion Viento Max"}, kulbat=(0, None), junilal=None
)

max_ruchuqakaqiq = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Velocidad Viento Maximal"}, kulbat=(0, None), junilal="km/h"
)
precipitación = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Precipitación"}, kulbat=(0, None), junilal="mm"
)

nevada = RetalJaloj(
    {"Kaqchikel": "ask julien", "español": "Nevada"}, kulbat=(0, None), junilal="mm"
)

tzujalchirijulew = RetalJaloj(
    {"Kaqchikel": "Tz'ujal chirij ulew", "español": "Escorrentía"}, kulbat=(0, None), junilal="mm"
)
jab = RetalJaloj(
    {"Kaqchikel": "Jab'", "español": "Lluvia"},
    kulbat=(0, None), junilal="mm"
)
kichelaj = RetalJaloj(
    {"Kaqchikel": "K'ichelaj", "español": "Bosque"},
    kulbat=(0, None), junilal='ha'
)
che = RetalJaloj(
    {"Kaqchikel": "Che'", "español": "Árboles"},
    kulbat=(0, None), junilal='ha'
)
tikon = RetalJaloj(
    {"Kaqchikel": "Tiko'n", "Tz'utujil": "Tijko'n", "español": "Árboles"},
    kulbat=(0, None), junilal='ha'
)
kokoltaqche = RetalJaloj(
    {"Kaqchikel": "Kok'ol taq che'", "español": "Arbustales"},
    kulbat=(0, None), junilal='ha'
)

ruwächqij_retal_jaloj_DICA_AMSCLAE = [etabälqij, max_etabälqij, max_temp, min_temp, prom_temp, etabälräxkaqïq, indiceUV,
                         max_indiceUV, max_apokaqïq, max_ruchuqakaqiq, precipitación, nevada, jab]

taq_retal_jaloj = [tzujalchirijulew, jab, kichelaj, che, tikon, kokoltaqche, etabälqij, max_etabälqij, max_temp,
                   min_temp, prom_temp, etabälräxkaqïq, indiceUV, max_indiceUV, max_apokaqïq, max_ruchuqakaqiq,
                   precipitación, nevada]

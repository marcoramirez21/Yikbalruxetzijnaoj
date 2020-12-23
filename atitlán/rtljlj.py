from ykbl import RetalJaloj

etabälqij = RetalJaloj(
    {"Kaqchikel": "Etab'äl qi'j", "español": "Radiación Solar"}, kulbat=(0, None), junilal="W/(m*m)"
)
nïm_etabälqij = RetalJaloj(
    {"Kaqchikel": "Nïm etabälqij", "español": "Radiación Solar Maximal"}, kulbat=(0, None), junilal="W/(m*m)"
)
nïm_tewkatanil = RetalJaloj(
    {"Kaqchikel": "Nïm tewk'atanil", "español": "Temperatura Maximal"}, kulbat=(None, None), junilal="°C"
)
koöl_tewkatanil = RetalJaloj(
    {"Kaqchikel": "Ko'öl tewk’atanil ", "español": "Temperatura Minimal"}, kulbat=(None, None), junilal="°C"
)
cholajil_tewkatanil = RetalJaloj(
    {"Kaqchikel": "Cholajil tewk'atanil", "español": "Temperatura Prom."}, kulbat=(None, None), junilal="°C"
)
etabälräxkaqïq = RetalJaloj(
    {"Kaqchikel": "Etab'äl räx kaq’ïq", "español": "Humedad"}, kulbat=(0, 100), junilal="%"
)
etabälMetzetelSaqil = RetalJaloj(
    {"Kaqchikel": "Etab'äl metz’etel saqil", "español": "Indice UV"}, kulbat=(0, None), junilal="Unid"
)
nïm_etabälMetzetelSaqil = RetalJaloj(
    {"Kaqchikel": "Etab'äl metz'etel saqil nïm", "español": "Indice UV Mayor"}, kulbat=(0, None), junilal="Unid"
)
nïm_ochochibälKaqïq = RetalJaloj(
    {"Kaqchikel": "Ochochib’äl nïm kaq'ïq'", "español": "Dirección Viento Max"}, kulbat=(0, None), junilal="NESW"
)

nïm_aninemKaqïq = RetalJaloj(
    {"Kaqchikel": "Nïm aninem kaq'ïq'", "español": "Velocidad Viento Maximal"}, kulbat=(0, None), junilal="km/h"
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

ruwächqij_retal_jaloj_DICA_AMSCLAE = [koöl_tewkatanil, cholajil_tewkatanil, nïm_tewkatanil, etabälräxkaqïq, precipitación, etabälqij,
                                      nïm_etabälqij, etabälMetzetelSaqil, nïm_ochochibälKaqïq, nïm_aninemKaqïq, nïm_aninemKaqïq]

taq_retal_jaloj = [tzujalchirijulew, jab, kichelaj, che, tikon, kokoltaqche]

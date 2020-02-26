from ykbl import RetalJaloj

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
taq_retal_jaloj = [
    tzujalchirijulew, jab, kichelaj, che, tikon, kokoltaqche
]

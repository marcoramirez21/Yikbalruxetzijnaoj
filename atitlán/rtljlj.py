from ykbl import RetalJaloj

tzujalchirijulew = RetalJaloj(
    {"Kaqchikel": "Tz'ujal chirij ulew", "español": "Escorrentía"}, kulbat=(0, None), junanil="mm"
)
jab = RetalJaloj(
    {"Kaqchikel": "Jab'", "español": "Lluvia"},
    kulbat=(0, None), junanil="mm"
)
kichelaj = RetalJaloj(
    {"Kaqchikel": "K'ichelaj", "español": "Bosque"},
    kulbat=(0, None), junanil='ha'
)
che = RetalJaloj(
    {"Kaqchikel": "Che'", "español": "Árboles"},
    kulbat=(0, None), junanil='ha'
)

taq_retal_jaloj = [
    tzujalchirijulew, jab, kichelaj, che
]

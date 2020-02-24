from .samajibäl import rubanom_kulbat


class RetalJaloj(object):
    def __init__(ri, rubi, kulbat, junanil):
        ri.rubi = rubi
        ri.kulbat = rubanom_kulbat(kulbat)
        ri.junanil = junanil

    def rubi_pa(ri, chabäl):
        chabäl = [chabäl] if isinstance(chabäl, str) else chabäl
        if isinstance(ri.rubi, dict):
            return next((ri.rubi[chb] for chb in chabäl if chb in ri.rubi), list(ri.rubi.values())[0])
        return ri.rubi


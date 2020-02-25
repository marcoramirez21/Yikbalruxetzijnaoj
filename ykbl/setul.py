import geopandas


class KolibälSetul(object):
    def __init__(ri, setul, retal):
        ri.setul = setul
        ri.retal = retal


class Setul(object):
    def __init__(ri, rubi, kolibäl=None):
        ri.rubi = rubi
        ri.kolibäl = kolibäl or {}

    @property
    def taq_etal(ri):
        raise NotImplementedError

    def rubi_pa(ri, retal, chabäl):
        if chabäl in ri.kolibäl and retal in ri.kolibäl[chabäl]:
            return ri.kolibäl[chabäl][retal]
        return retal

    def retal(ri, rubi):
        if rubi in ri.taq_etal:
            return rubi
        for retal, kibi in ri.kolibäl.items():
            if next((rubi_chb for rubi_chb in kibi.values() if rubi_chb == rubi), None):
                return retal
        raise KeyError(rubi)

    def __getitem__(ri, rubi):
        if isinstance(rubi, str):
            return KolibälSetul(ri, [ri.retal(rubi)])
        else:
            return KolibälSetul(ri, [ri.retal(rb) for rb in rubi])




class SetulShp(Setul):
    def __init__(ri, rubi, rochochibäl, rucheel_etal, kolibäl=None):
        ri.tzij = geopandas.read_file(rochochibäl)
        ri.rucheel_etal = rucheel_etal
        super().__init__(rubi, kolibäl=kolibäl)

    @property
    def taq_etal(ri):
        return ri.tzij[ri.rucheel_etal]

    def kiyatzuk(ri, etal, chojmilem):
        return ri.tzij.to_crs(epsg=chojmilem)['geometry'][ri.tzij[ri.rucheel_etal] == etal].item()

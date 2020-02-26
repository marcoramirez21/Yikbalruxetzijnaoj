import geopandas

from ykbl.samajibäl import ruqaxanïk_junilal


class KolibälSetul(object):
    def __init__(ri, setul, retal):
        ri.setul = setul
        ri.retal = retal


class RucheelPeraj(object):
    def __init__(ri, rucheel, junilal):
        ri.rucheel = rucheel
        ri.junilal = junilal


class Setul(object):
    def __init__(ri, rubi, kolibäl=None):
        ri.rubi = rubi
        ri.kolibäl = kolibäl or {}

    @property
    def taq_etal(ri):
        raise NotImplementedError

    def rubi_pa(ri, retal, chabäl):
        for chb in chabäl:
            if retal in ri.kolibäl and chb in ri.kolibäl[retal]:
                rubi = ri.kolibäl[retal][chb]
                return rubi or retal
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
    def __init__(ri, rubi, rochochibäl, rucheel_etal, rucheel_peraj=None, kolibäl=None):
        ri.tzij = geopandas.read_file(rochochibäl).set_index(rucheel_etal)
        ri.tzij.index = ri.tzij.index.map(str)

        ri.rucheel_etal = rucheel_etal
        ri.rucheel_peraj = rucheel_peraj
        if ri.rucheel_peraj:
            ri.peraj = ri.tzij[ri.rucheel_peraj.rucheel]
            ri.junilal_peraj = ri.rucheel_peraj.junilal
        else:
            ri.peraj = ri.tzij.to_crs({'proj': 'cea'})['geometry'].area / 1e4
            ri.junilal_peraj = 'ha'
        super().__init__(rubi, kolibäl=kolibäl)

    @property
    def taq_etal(ri):
        return ri.tzij.index.values

    def kiyatzuk(ri, etal, chojmilem):
        return ri.tzij.to_crs(crs=chojmilem)['geometry'].loc[etal]

    def peraj_kiyatzuk(ri, etal, junilal):
        if junilal is None:
            return 1
        elif junilal == '%':
            return 100
        else:
            return ri.peraj.loc[etal] * ruqaxanïk_junilal(ri.junilal_peraj, junilal)

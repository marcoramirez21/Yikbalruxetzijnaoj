import geopandas


class SetulShp(object):
    def __init__(ri, rubi, rochochibäl, rucheel_etal, kolibäl=None):
        ri.rubi = rubi
        ri.tzij = geopandas.read_file(rochochibäl)
        ri.rucheel_etal = rucheel_etal
        ri.kolibäl = kolibäl

    @property
    def taq_etal(ri):
        return ri.tzij[ri.rucheel_etal]

    def kiyatzuk(ri, etal, chojmilem):
        return ri.tzij.to_crs(epsg=chojmilem)['geometry'][ri.tzij[ri.rucheel_etal] == etal].item()

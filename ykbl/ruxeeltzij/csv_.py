import os

import pandas as pd

from ykbl.samajibäl import _, rubanom_ramaj
from .ruxeeltzij import RuxeelTzij, TununemRetalJaloj


class RucheelRamaj(object):
    def __init__(ri, rucheel, rubeyal=None):
        ri.rucheel = rucheel
        ri.rubeyal = rubeyal


class RucheelKolibäl(object):
    def __init__(ri, rucheel):
        ri.rucheel = rucheel


class RuxeelTzijCSV(RuxeelTzij):
    def __init__(ri, rubi, rochochibäl, tununem, retamabäl, kolibäl, ramaj):
        ri.rochochibäl = rochochibäl
        ri.cache = f'{ri.rochochibäl}.parquet'

        ri.kolibäl = kolibäl
        ri.ramaj = ramaj

        ri.tununem = [tununem] if isinstance(tununem, TununemRetalJaloj) else tununem
        super().__init__(rubi, retal_jaloj={tnm.retal_jaloj for tnm in ri.tununem}, retamabäl=retamabäl)

    def jalixïk_cache(ri):
        return os.path.isfile(ri.cache) and os.path.getmtime(ri.rochochibäl) > os.path.getmtime(ri.cache)

    def rejqalem(ri, retal_jaloj, kolibäl, ramaj, chabäl):

        rucheel = ri._rucheel_csv(retal_jaloj)
        rucheel_kolibäl, rucheel_ramaj = _("K'olib'äl", chabäl), _("Ramaj", chabäl)

        if ri.jalixïk_cache():
            tzj = pd.read_parquet(ri.cache, columns=rucheel)
        else:
            tzj = pd.read_csv(ri.rochochibäl, usecols=rucheel)
            tzj.to_parquet(ri.cache)

        if isinstance(ri.kolibäl, RucheelKolibäl):
            raise NotImplementedError  # Ruqaxanik pa etal
        elif ri.kolibäl:
            tzj[rucheel_kolibäl] = ri.kolibäl

        if isinstance(ri.ramaj, RucheelRamaj):
            tzj[ri.ramaj.rucheel] = pd.to_datetime(tzj[ri.ramaj.rucheel], format=ri.ramaj.rubeyal)
        elif ri.ramaj:
            tzj[rucheel_ramaj] = rubanom_ramaj(ri.ramaj)

        tzj = tzj.rename(columns=ri._kibi_retaljaloj_rucheel(chabäl))
        return tzj

    def _rucheel_csv(ri, retal_jaloj):
        rucheel = [tnm.rucheel for tnm in ri.tununem if tnm.retal_jaloj in retal_jaloj]
        if isinstance(ri.ramaj, RucheelRamaj):
            rucheel.append(ri.ramaj.rucheel)
        if isinstance(ri.kolibäl, RucheelKolibäl):
            rucheel.append(ri.kolibäl.rucheel)

        return rucheel

    def _kibi_retaljaloj_rucheel(ri, chabäl):
        kibi = {tnm.rucheel: tnm.retal_jaloj.rubi_pa(chabäl) for tnm in ri.tununem}

        if isinstance(ri.ramaj, RucheelRamaj):
            kibi.update({ri.ramaj.rucheel: _("Ramaj", chabäl)})
        if isinstance(ri.kolibäl, RucheelKolibäl):
            kibi.update({ri.kolibäl.rucheel: _("K'olib'äl", chabäl)})

        return kibi

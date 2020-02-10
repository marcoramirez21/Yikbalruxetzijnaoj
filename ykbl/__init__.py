import glob
import json
import os

import numpy as np
import pandas as pd


def rubanom_kulbat(kulbat):
    if kulbat is None:
        return -np.inf, np.inf
    if kulbat[0] > kulbat[1]:
        raise ValueError(kulbat)
    return -np.inf if kulbat[0] is None else kulbat[0], np.inf if kulbat[1] is None else kulbat[1]


class RetalJaloj(object):
    def __init__(ri, rubi, kulbat):
        ri.rubi = rubi
        ri.kulbat = rubanom_kulbat(kulbat)


class RetamabälRuxeelTzij(dict):
    def __init__(ri, rochochibäl):
        ri.rochochibäl = rochochibäl
        with open(rochochibäl, 'r', encoding='utf8') as w:
            wuj = json.load(w)
        super().__init__(**wuj)


class RuxeelTzij(object):
    def __init__(ri, retamabäl):
        ri.retamabäl = RetamabälRuxeelTzij(retamabäl)
        ri.rochochibäl = os.path.join(
            os.path.split(retamabäl)[0],
            ri.retamabäl["rochochib'äl"]
        )

        rikoxik = os.path.splitext(ri.rochochibäl)[1].lower()
        if rikoxik == '.csv':
            ri.tzij = TzijCSV(ri.rochochibäl, ri.retamabäl)
        else:
            raise ValueError(rikoxik)
        ri.retal_jaloj = list(ri.retamabäl["retal jaloj"])


class Tzij(object):
    pass


class TzijCSV(Tzij):
    def __init__(ri, rochochibäl, retamabäl):
        ri.rochochibäl = rochochibäl
        ri.retamabäl = retamabäl
        ri.tzij = ri._rejqanïk_tzij()

        ri.retal_jaloj = ri.tzij.columns

    def _rejqanïk_tzij(ri):
        cache = f'{ri.rochochibäl}.feather'

        kakawuj = os.path.getmtime(ri.rochochibäl) > os.path.getmtime(cache)
        kakaretamabäl = os.path.getmtime(ri.retamabäl.rochochibäl) > os.path.getmtime(cache)

        if not os.path.isfile(cache) or kakawuj or kakaretamabäl:
            tzj = pd.read_csv(ri.rochochibäl)
            tzj.to_feather(cache)
        else:
            tzj = pd.read_feather(cache)
        retaljaloj = {rjl["rub'i'"]: rp for rp, rjl in ri.retamabäl['retal jaloj'].items()}
        tzj = tzj.rename(columns=retaljaloj)

        if isinstance(ri.retamabäl["k'olib'äl"], str):  # chi ninb'an: catégories
            tzj = tzj.assign(**{"k'olib'äl": ri.retamabäl["k'olib'äl"]})
        else:
            tzj = tzj.rename(columns={ri.retamabäl["k'olib'äl"]["ruche'el'"]: "k'olib'äl"})
        if isinstance(ri.retamabäl["q'ij"], str):
            raise NotImplementedError
        else:
            tzj = tzj.assign(**{"q'ij": pd.to_datetime(tzj[ri.retamabäl["q'ij"]["ruche'el'"]], format=ri.retamabäl["q'ij"]["rub'eyal"])})

        return tzj[list(retaljaloj.values()) + ["q'ij", "k'olib'äl"]]


class Samaj(object):
    def __init__(ri, rochochibäl):
        ri.rochochibäl = rochochibäl
        ri.ruxeeltzij = [RuxeelTzij(r) for r in glob.glob('**/*.rtmbl.json', recursive=True)]
        ri.retal_jaloj = {r for rxl in ri.ruxeeltzij for r in rxl.retal_jaloj}

    def runimilem(ri, retal_jaloj):
        return {
            'ramaj': (),
            "k'olib'äl": {klb}
        }

    def ruxeel(ri, retal_jaloj):
        return [rxl for rxl in ri.ruxeeltzij if retal_jaloj in rxl.retal_jaloj]

    def rejqalem(ri, retal_jaloj):
        return pd.concat([rxl.tzij.tzij[retal_jaloj] for rxl in ri.ruxeel(retal_jaloj)])

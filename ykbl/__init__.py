import glob
import json
import os

import pandas as pd


class RetamabälRuxeelTzij(dict):
    def __init__(ri, chltzj):
        super().__init__(**chltzj)


class RuxeelTzij(object):
    def __init__(ri, retamabäl):
        with open(retamabäl, 'r', encoding='utf8') as w:
            ri.retamabäl = RetamabälRuxeelTzij(json.load(w))

        ri.rochochibäl = os.path.join(
            os.path.split(retamabäl)[0],
            ri.retamabäl["rochochib'äl"]
        )

        rikoxik = os.path.splitext(ri.rochochibäl)[1].lower()
        if rikoxik == '.csv':
            ri.tzij = TzijCSV(ri.rochochibäl)
        else:
            raise ValueError(rikoxik)
        ri.retal_jaloj = list(ri.retamabäl["retal jaloj"])


class Tzij(object):
    pass


class TzijCSV(Tzij):
    def __init__(ri, rochochibäl):
        ri.rochochibäl = rochochibäl
        ri.tzij = ri._rejqanïk_tzij()

        ri.retal_jaloj = ri.tzij.columns

    def _rejqanïk_tzij(ri):
        cache = f'{ri.rochochibäl}.feather'
        if not os.path.isfile(cache) or (os.path.getmtime(ri.rochochibäl) > os.path.getmtime(cache)):
            tzj = pd.read_csv(ri.rochochibäl)
            tzj.to_feather(cache)
        else:
            tzj = pd.read_feather(cache)
        return tzj


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
        pass

    def rejqalem(ri, retal_jaloj):
        pass

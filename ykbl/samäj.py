import pandas as pd

from .retal_jaloj import RetalJaloj
from .ruxeeltzij import RuxeelTzijMoltzïk
from .samajibäl import _
from .setul import SetulShp


class Samäj(object):
    def __init__(ri, retal_jaloj, ruxeel_tzij, chabäl='Kaqchikel'):
        ri.retal_jaloj = retal_jaloj
        ri.ruxeel_tzij = ruxeel_tzij

        ri.chabäl = [chabäl] if isinstance(chabäl, str) else chabäl

    def tatzijoj(ri, chabäl):
        chabäl = [chabäl] if isinstance(chabäl, str) else chabäl
        ri.chabäl = chabäl

    def rejqalem(ri, retal_jaloj, kolibäl, ramaj):
        retal_jaloj = ri._rusikxïk_retal_jaloj(retal_jaloj)
        rucheel = [rtl.rubi_pa(ri.chabäl) for rtl in retal_jaloj]

        tzolinïk = pd.DataFrame(columns=rucheel + [_("Ramaj", ri.chabäl), _("K'olibäl", ri.chabäl)])
        for rxl in ri.ruxeel_tzij:
            # RuxeelTzijMoltzïk rajwaxïk jun ruSetulShp chi nelesaj rutzij
            if not isinstance(rxl, RuxeelTzijMoltzïk) or isinstance(kolibäl, SetulShp):
                tzij = rxl.rejqalem(retal_jaloj, kolibäl=kolibäl, ramaj=ramaj, chabäl=ri.chabäl)
                if tzij:
                    tzij[_("Ruxe'el", ri.chabäl)] = rxl.rubi
                    tzolinïk = tzolinïk.append(tzij)

        return tzolinïk

    def _rusikxïk_retal_jaloj(ri, retal_jaloj):
        if not retal_jaloj:
            return ri.retal_jaloj
        retal_jaloj = retal_jaloj if isinstance(retal_jaloj, (list, tuple, set)) else [retal_jaloj]
        tzolinïk = set()
        for rtl in retal_jaloj:
            if isinstance(retal_jaloj, RetalJaloj):
                tzolinïk.add(rtl)
            else:
                tzolinïk.add(next(retal for retal in ri.retal_jaloj if retal.rubi_pa(ri.chabäl)))

        return tzolinïk

import pandas as pd

from .retal_jaloj import RetalJaloj
from .samajibäl import _
from .setul import KolibälSetul, Setul


class Samäj(object):
    def __init__(ri, retal_jaloj, ruxeel_tzij, chabäl='Kaqchikel'):
        ri.retal_jaloj = retal_jaloj
        ri.ruxeel_tzij = ruxeel_tzij

        ri.chabäl = [chabäl] if isinstance(chabäl, str) else chabäl

    def tatzijoj(ri, chabäl):
        chabäl = [chabäl] if isinstance(chabäl, str) else chabäl
        ri.chabäl = chabäl

    def rejqalem(ri, retal_jaloj, kolibäl, ramaj):
        if ramaj is not None:
            raise NotImplementedError("K'o na chi nintz'ib'aj ri runuk' kematz'ib' re. Takuyu numaq :)")

        kolibäl = ri._rusukxïk_kolibäl(kolibäl)

        retal_jaloj = ri._rusikxïk_retal_jaloj(retal_jaloj)
        rucheel = [rtl.rubi_pa(ri.chabäl) for rtl in retal_jaloj]

        rucheel_kankowi = [_("Ramaj", ri.chabäl), _("K'olibäl", ri.chabäl)]
        tzolinïk = pd.DataFrame(columns=rucheel + rucheel_kankowi)

        for rxl in ri.ruxeel_tzij:
            tzij = rxl.rejqalem(retal_jaloj, kolibäl=kolibäl, ramaj=ramaj, chabäl=ri.chabäl)
            if tzij is not None and len(tzij):
                tzij[_("Ruxe'el", ri.chabäl)] = rxl.rubi
                tzolinïk = tzolinïk.append(tzij)

        return tzolinïk.reset_index()

    @staticmethod
    def _rusukxïk_kolibäl(kolibäl):
        if kolibäl is None:
            return kolibäl
        if isinstance(kolibäl, (Setul, KolibälSetul)):
            return kolibäl
        if isinstance(kolibäl, str):
            raise TypeError(
                "Rajwaxïk naya' jun setul chuqa', achi'el pa `KolibälSetul(nusetul, {})`.".format(kolibäl)
            )
        raise TypeError(kolibäl)

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

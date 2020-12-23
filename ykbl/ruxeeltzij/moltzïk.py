import numpy as np
import pandas as pd
import rasterio
from rasterio import features

from ykbl.samajibäl import rubanom_ramaj, _
from ykbl.setul import SetulShp, KolibälSetul
from .ruxeeltzij import RuxeelTzij, TununemRetalJaloj


class RuxakMoltzïk(object):
    def __init__(ri, runuk, ramaj, tununem):
        ri.runuk = runuk
        ri.ramaj = rubanom_ramaj(ramaj)
        ri.tununem = [tununem] if isinstance(tununem, TununemRetalJaloj) else tununem
        ri.retal_jaloj = [tnm.retal_jaloj for tnm in tununem]


class CholanilRuxakMoltzïk(RuxakMoltzïk):
    def __init__(ri, runuk, tununem, ramaj=None):
        super().__init__(runuk, ramaj, tununem)


class CholajilRuxakMoltzïk(RuxakMoltzïk):
    def __init__(ri, runuk, tununem, ramaj=None):
        if not isinstance(tununem, TununemRetalJaloj):
            raise TypeError(type(tununem))
        super().__init__(runuk, ramaj, tununem)


class RuxeelTzijMoltzïk(RuxeelTzij):
    def __init__(ri, rubi, rochochibäl, ruxak, retamabäl, ramaj=None):
        ri.rochochibäl = rochochibäl
        ri.ruxak = [ruxak] if isinstance(ruxak, RuxakMoltzïk) else ruxak
        ri.ramaj = rubanom_ramaj(ramaj)

        if not ri.ramaj and not all(xak.ramaj for xak in ri.ruxak):
            raise ValueError(
                "K'o chi naya kiramaj chike konojel ri taq xak richin ri ruxe'el tzij {rubi} rub'i'.".format(
                    rubi=ri.rubi
                )
            )
        ri.xak = {}
        with rasterio.open(rochochibäl) as wj:
            ri.crs = wj.crs
            ri.kexonem = wj.transform
            ri.banikil = wj.shape
            for xak in ri.ruxak:
                ri.xak[str(xak.runuk)] = wj.read(int(xak.runuk))

        super().__init__(rubi, tununem={tnm for xak in ri.ruxak for tnm in xak.tununem}, retamabäl=retamabäl)

    def rejqalem(ri, retal_jaloj, kolibäl, ramaj, chabäl):
        retal_jaloj = ri._rusikxïk_retal_jaloj(retal_jaloj)

        xak = [xak for xak in ri.ruxak if any(rtl in retal_jaloj for rtl in xak.retal_jaloj)]
        if not xak:
            return

        # RuxeelTzijMoltzïk rajwaxïk jun ruSetulShp chi nelesaj rutzij
        if isinstance(kolibäl, SetulShp):
            setul = kolibäl
            taq_kolibäl = kolibäl.taq_etal
        elif isinstance(kolibäl, KolibälSetul) and isinstance(kolibäl.setul, SetulShp):
            setul = kolibäl.setul
            taq_kolibäl = kolibäl.retal
        else:
            return

        koj_kiyatzuk = {}
        for etal in taq_kolibäl:
            koj_kiyatzuk[etal] = features.rasterize(
                ((setul.kiyatzuk(etal, chojmilem=ri.crs), 1),),
                out_shape=ri.banikil,
                transform=ri.kexonem
            )
        rucheel_kolbäl, rucheel_ramaj = _("K'olib'äl", chabäl), _("Ramaj", chabäl)

        tzij = pd.DataFrame(columns=[rucheel_kolbäl, rucheel_ramaj])
        for xk in xak:
            tununem = [tnm for tnm in xk.tununem if tnm.retal_jaloj in retal_jaloj]

            for etal, koj in koj_kiyatzuk.items():
                m = np.where(koj, ri.xak[xk.runuk], np.nan)

                rubi_kolibäl = setul.rubi_pa(etal, chabäl)
                ramaj_xak = xk.ramaj or ri.ramaj
                rucheel_konojel = {
                    rucheel_kolbäl: rubi_kolibäl, rucheel_ramaj: ramaj_xak
                }

                if isinstance(xk, CholanilRuxakMoltzïk):
                    rucheel_retaljaloj = {
                        tnm.retal_jaloj.rubi_pa(chabäl): np.mean(
                            np.isin(m[~np.isnan(m)], tnm.rucheel)
                        ) * setul.peraj_kiyatzuk(etal, tnm.retal_jaloj.junilal) for tnm in tununem
                    }

                else:
                    # Xaxe k'o jun kitununem ri taq cholajil moltzïk
                    rubi_retaljaloj = tununem[0].rubi_pa(chabäl)
                    rucheel_retaljaloj = {rubi_retaljaloj: np.nanmean(m)}

                akuchi = (tzij[rucheel_kolbäl] == rubi_kolibäl) & (tzij[rucheel_ramaj] == ramaj_xak)
                if len(tzij.loc[akuchi]):
                    tzij.loc[akuchi, list(rucheel_retaljaloj)] = list(rucheel_retaljaloj.values())
                else:
                    tzij = tzij.append({**rucheel_konojel, **rucheel_retaljaloj}, ignore_index=True)

        return tzij


class TununemRetalJalojCholanilMoltzïk(TununemRetalJaloj):
    def __init__(ri, retal_jaloj, runuk):
        if isinstance(runuk, (int, float, str)):
            runuk = [runuk]
        super().__init__(retal_jaloj, rucheel=runuk, junilal=None, jaloj=1)


class TununemRetalJalojCholajilMoltzïk(TununemRetalJaloj):
    def __init__(ri, retal_jaloj, junilal):
        super().__init__(retal_jaloj, rucheel=None, junilal=junilal)

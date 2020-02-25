import numpy as np
import pandas as pd
import rasterio
from rasterio import features

from ykbl.samajibäl import rubanom_ramaj, _
from ykbl.setul import SetulShp, KolibälSetul
from .ruxeeltzij import RuxeelTzij


class RuxakMoltzïk(object):
    def __init__(ri, runuk, ramaj):
        ri.runuk = runuk
        ri.ramaj = rubanom_ramaj(ramaj)


class CholanilRuxakMoltzïk(RuxakMoltzïk):
    def __init__(ri, runuk, tununem, ramaj=None):
        super().__init__(runuk, ramaj)
        ri.tununem = tununem
        ri.retal_jaloj = []


class CholajilRuxakMoltzïk(RuxakMoltzïk):
    def __init__(ri, runuk, tununem, ramaj=None):
        super().__init__(runuk, ramaj)
        ri.rununem = tununem
        ri.retal_jaloj = tununem.retal_jaloj


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
            ri.crs = wj.crs.to_epsg()
            ri.kexonem = wj.transform
            ri.banikil = wj.shape
            for xak in retamabäl.xak:
                ri.xak[str(xak)] = wj.read(int(xak))

        super().__init__(rubi, retal_jaloj={rtl for xak in ri.ruxak for rtl in xak.retal_jaloj}, retamabäl=retamabäl)

    def rejqalem(ri, retal_jaloj, kolibäl, ramaj, chabäl):
        xak = [xak.runuk for xak in ri.ruxak if any(rtl in retal_jaloj for rtl in xak.retal_jaloj)]
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

        tzij = pd.DataFrame(data={rucheel_kolbäl: taq_kolibäl})
        for xk in xak:
            for etal, koj in koj_kiyatzuk:
                m = np.where(koj, ri.xak[xk], np.nan)

                rubi_kolibäl = setul.rubi(etal, chabäl)
                ramaj_xak = xk.ramaj or ri.ramaj
                rucheel_konojel = {
                    rucheel_kolbäl: rubi_kolibäl, rucheel_ramaj: ramaj_xak
                }

                if isinstance(xk, CholanilRuxakMoltzïk):
                    rucheel_retaljaloj = {
                        tnm.retal_jaloj.rubi_pa(chabäl): np.nanmean(
                            (m == tnm.rucheel if isinstance(tnm.rucheel, int) else np.isin(m, tnm.rucheel))
                        ) for tnm in xk.tununem
                    }
                    # Chi ninb'an: ruq'axanïk juna'il

                else:
                    rubi_retaljaloj = xk.tununem.retal_jaloj.rubi_pa(chabäl)
                    rucheel_retaljaloj = {rubi_retaljaloj: np.nanmean(m)}

                akuchi = (tzij[rucheel_kolbäl] == rubi_kolibäl) & (tzij[rucheel_ramaj] == ramaj_xak)
                if len(tzij.loc[akuchi]):
                    tzij.loc[akuchi, list(rucheel_retaljaloj)] = list(rucheel_retaljaloj.values())
                else:
                    tzij.append({**rucheel_konojel, **rucheel_retaljaloj})

        return tzij

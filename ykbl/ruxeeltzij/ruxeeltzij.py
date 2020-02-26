from ykbl.samajibäl import ruqaxanïk_junilal


class RetamabälRuxeelTzij(object):
    def __init__(ri, qijxjunimaxïk, xjunumaxïkroma, tzibanel, tzijowäch='', ruqijlem=None):
        ri.qijxjunimaxïk = qijxjunimaxïk
        ri.xjunumaxïkroma = xjunumaxïkroma
        ri.tzibanel = tzibanel
        ri.tzijowäch = tzijowäch
        ri.ruqijlem = ruqijlem


class RuxeelTzij(object):
    def __init__(ri, rubi, tununem, retamabäl):
        ri.rubi = rubi
        ri.tununem = [tununem] if isinstance(tununem, TununemRetalJaloj) else tununem
        ri.retamabäl = retamabäl

        ri.retal_jaloj = [tnm.retal_jaloj for tnm in ri.tununem]

    def rejqalem(ri, retal_jaloj, kolibäl, ramaj, chabäl):
        raise NotImplementedError

    def _rusikxïk_retal_jaloj(ri, retal_jaloj):
        return [tnm.retal_jaloj for tnm in ri.tununem if tnm.retal_jaloj in retal_jaloj]


class TununemRetalJaloj(object):
    def __init__(ri, retal_jaloj, rucheel, junilal, jaloj=None):
        ri.rucheel = rucheel
        ri.retal_jaloj = retal_jaloj
        ri.junilal = junilal
        if jaloj:
            ri.jaloj = jaloj
        else:
            ri.jaloj = ruqaxanïk_junilal(ri.junilal, retal_jaloj.junilal)

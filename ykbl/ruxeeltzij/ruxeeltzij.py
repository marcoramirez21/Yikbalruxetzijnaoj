from warnings import warn

import pint

ureg = pint.UnitRegistry()


class RetamabälRuxeelTzij(object):
    def __init__(ri, qijxjunimaxïk, xjunumaxïkroma, tzibanel, tzijowäch='', ruqijlem=None):
        ri.qijxjunimaxïk = qijxjunimaxïk
        ri.xjunumaxïkroma = xjunumaxïkroma
        ri.tzibanel = tzibanel
        ri.tzijowäch = tzijowäch
        ri.ruqijlem = ruqijlem


class RuxeelTzij(object):
    def __init__(ri, rubi, retal_jaloj, retamabäl):
        ri.rubi = rubi
        ri.retal_jaloj = retal_jaloj
        ri.retamabäl = retamabäl

    def rejqalem(ri, retal_jaloj, kolibäl, ramaj, chabäl):
        raise NotImplementedError


class TununemRetalJaloj(object):
    def __init__(ri, retal_jaloj, rucheel, junilal):
        ri.rubi = rucheel
        ri.retal_jaloj = retal_jaloj
        ri.junilal = junilal
        jnl_rtljlj = retal_jaloj.junilal
        try:
            ri.jaloj = ureg.parse_expression(ri.junilal).to(jnl_rtljlj)
        except pint.errors.UndefinedUnitError:
            ri.jaloj = 1
            warn("Man xojtikïr ta niqak'exwachij {jnl} pa {jnlrtl}.".format(jnl=ri.junilal, jnlrtl=jnl_rtljlj))

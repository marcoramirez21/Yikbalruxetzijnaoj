from datetime import datetime, date
from warnings import warn

import numpy as np
import pandas as pd
import pint
from pint import UnitRegistry

ureg = UnitRegistry()

_qaxantzij = {
    "Ramaj": {
        "Tz'utujil": "Ramaaj",
        "español": "Tiempo"
    },
    "K'olib'äl": {
        "español": "Lugar",
    },
    "Ruxe'el": {
        "español": "Fuente"
    }
}


def _(tzij, chabäl):
    if tzij in _qaxantzij:
        return next((_qaxantzij[tzij][chb] for chb in chabäl if chb in _qaxantzij[tzij]), tzij)
    return tzij


def rubanom_kulbat(kulbat):
    if kulbat is None:
        return -np.inf, np.inf
    kulbat = (-np.inf if kulbat[0] is None else kulbat[0], np.inf if kulbat[1] is None else kulbat[1])
    if kulbat[0] > kulbat[1]:
        raise ValueError(kulbat)
    return kulbat


def rubanom_ramaj(ramaj):
    if not ramaj:
        return ramaj
    if isinstance(ramaj, int):
        ramaj = str(ramaj)
    if isinstance(ramaj, (datetime, date, str)):
        return pd.to_datetime(ramaj)
    raise TypeError(ramaj, type(ramaj))


def ruqaxanïk_junilal(jnll1, jnll2):
    try:
        return ureg.parse_expression(jnll1).to(jnll2).magnitude
    except (pint.errors.UndefinedUnitError, pint.errors.DimensionalityError, AttributeError):
        warn("Man xojtikïr ta niqak'exwachij {jnll1} pa {jnll2}.".format(jnll1=jnll1, jnll2=jnll2))
        return 1

from datetime import datetime, date

import numpy as np
import pandas as pd

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
    if kulbat[0] > kulbat[1]:
        raise ValueError(kulbat)
    return -np.inf if kulbat[0] is None else kulbat[0], np.inf if kulbat[1] is None else kulbat[1]


def rubanom_ramaj(ramaj):
    if not ramaj:
        return ramaj
    if isinstance(ramaj, int):
        ramaj = str(ramaj)
    if isinstance(ramaj, (datetime, date, str)):
        return pd.to_datetime(ramaj)
    raise TypeError(ramaj, type(ramaj))

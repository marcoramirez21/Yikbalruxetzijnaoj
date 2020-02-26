import os

from ykbl.setul import SetulShp, RucheelPeraj

RujunilalTzolitzijYa = SetulShp(
    "'Rujunilal Tzolitzij Ya'",
    rochochibäl=os.path.join(os.path.dirname(__file__), 'actual_hru_atitlan/actual_hru_atitlan.shp'),
    rucheel_etal='HRUS',
    rucheel_peraj=RucheelPeraj('Area', 'km**2')
)

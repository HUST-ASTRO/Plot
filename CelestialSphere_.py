# -*- coding: utf-8 -*-
# @Time    : 18-2-1 下午2:36
# @Author  : YuLiu
# @Email   : 335992260@qq.com
# @File    : CelestialSphere.py
# @Software: PyCharm


import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord


class CelestialSphere:
    def __init__(self, frame):
        self._frame_choices = {'icrs': self._icrs,
                               'galactic': self._galactic}

        # simple test to validate frame
        if frame in self._frame_choices.keys():
            self.frame = frame
        else:
            raise ValueError("Invalid Value for frame: {0}".format(frame))

        plt.subplot(projection="aitoff")
        plt.grid(True)
        self._frame_choices[self.frame]()

    @staticmethod
    def _icrs():
        plt.title("ICRS")
        plt.setp(plt.gca(),
                 xticklabels=['14h', '16h', '18h', '20h', '22h', '0h', '2h', '4h', '6h', '8h', '10h'])

    @staticmethod
    def _galactic():
        plt.title("galactic")

    def add_point(self, x, y, unit=None):
        try:
            if unit is None:
                c = SkyCoord(x, y, frame=self.frame)
            else:
                c = SkyCoord(x, y, frame=self.frame, unit=unit)
        except u.UnitsError:
            raise u.UnitsError("No unit specified")
        except ValueError:
            raise ValueError('Unit keyword must have one to three unit values as '
                             'tuple or comma-separated string')

        if self.frame == 'galactic':
            longitude = c.l.wrap_at(180 * u.deg).radian
            dimensionality = c.b.radian
        else:
            longitude = c.ra.wrap_at(180 * u.deg).radian
            dimensionality = c.dec.radian
        plt.plot(longitude, dimensionality, linestyle='none', marker='.')


if __name__ == '__main__':
    figure = CelestialSphere('icrs')
    figure.add_point('1h', '30d')
    plt.show()

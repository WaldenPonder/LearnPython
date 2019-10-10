import numpy as np
import pylab as pl
from scipy import interpolate
import random
x_end = 2*np.pi

interpolate_cnt = 10000


def spline_interpolate(x, y):
    x_new = np.linspace(0, x_end, interpolate_cnt)
    tck = interpolate.splrep(x, y)  # 这个必须有，splrep()的结果作为splev()的第二个参数
    y_spline = interpolate.splev(x_new, tck, 0)
    return x_new, y_spline


def spline_der(x, y, der):
    tck = interpolate.splrep(x, y)
    x_new = np.linspace(0, x_end, interpolate_cnt)
    # d = interpolate.splev(x_new, tck, 0)
    d = interpolate.splev(x_new, tck, der)
    return d

##############################################################################


samples = [0, 0.25, 0, -.5] * 5
# samples = [np.sin(x/10) for x in range(0, 100, 1)]
x = np.linspace(0, x_end, len(samples))
y = np.array(samples)
little = .5
pl.plot([0, x_end], [little, little], '--')  # 水平直线
pl.plot([0, x_end], [-little, -little], '--')

##############################################################################

x_new, y_spline = spline_interpolate(x, y)
der2 = spline_der(x_new, y_spline, 2)
der3 = spline_der(x_new, y_spline, 3)


pl.plot(x, y, '*', markersize=20,  label='pts')
pl.plot(x_new, y_spline, 'y', linewidth=3, label='B_spline interpolation')
# pl.plot(x_new, der2, 'b', linewidth=3, label='D2')
# pl.plot(x_new, der3, 'r', linewidth=3, label='D3')
pl.legend()
pl.show()

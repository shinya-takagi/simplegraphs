import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, ListedColormap

from simplegraph.BasicFunctions import digit_max


def contour_map(ax, file_path, CBAR=None, fig=None,
                cmap=plt.get_cmap('jet'), scale="Linear", skiprows=0,
                x_axle=0, y_axle=1, z_axle=2,
                ):
    ''' Returns Matplotlib axes of contour map(LogScale)

    Args:
        ax: axis in figure.
        file_path: file path of contour map.

    Opts:
        CBAR: Set Color bar in the figure, require the figure("fig").
        fig: Figure, used as color bar at Figure.
        cmap: Set Color map.
        scale: scale of contour map. Default is Linear. Can set "Log" scale.

    Returns:
        axis in figure plotted contour map.
    '''

    data = np.loadtxt(file_path, skiprows=skiprows)

    bmap = ListedColormap(['black'])
    x, y, z = data[:, x_axle], data[:, y_axle], data[:, z_axle]
    x_element, y_element = np.unique(x), np.unique(y)
    XX, YY = np.meshgrid(x_element, y_element)
    ZZ = z.reshape(XX.shape)
    if scale == "Log":
        Zmask = np.ma.masked_where(ZZ <= 0, ZZ)
        Zfill = Zmask.filled(fill_value=1E-1)

        vmin, vmax = 1, max(z)
        digit_counter = digit_max(vmax)

        clev = (digit_counter+1)**2
        level = list(np.logspace(0, np.log10(vmax), num=clev))
        level_line = list(np.logspace(0, np.log10(vmax),
                                      num=(digit_counter+1)))
        #                             num=clev))
        # ticklevels = list(np.logspace(0, np.log10(vmax),
        #                               num=digit_counter+1))
        Norm = LogNorm(vmin=vmin, vmax=vmax)

        cs = ax.contourf(XX, YY, Zfill, levels=level, cmap=cmap, norm=Norm)
        ax.contour(XX, YY, Zfill, levels=level_line, cmap=bmap, norm=Norm)
    else:
        vmin, vmax = -60, 60
        num = 100
        level = np.linspace(vmin, vmax, num)
        level_line = np.linspace(vmin, vmax, int(num*0.2))
        cs = ax.contourf(XX, YY, ZZ, levels=level, cmap=cmap,
                         vmin=vmin, vmax=vmax)
        ax.contour(XX, YY, ZZ, levels=level_line, cmap=bmap,
                   vmin=vmin, vmax=vmax)

    if CBAR:
        pp = fig.colorbar(cs, ax=ax)
        # pp.set_clim(vmin, vmax)

    return ax

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from pylab import *
import cmocean
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd


def plot_bias_stations(bias,plat,plon,plot_title,var_unit_list,plot_outfile):

    # Make a graphic
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()

    cmap = plt.get_cmap('gist_rainbow_r')
    cax = plt.scatter(plon,plat,c=bias, s=(bias+abs(np.min(bias)))*30, vmin=min(bias), vmax=max(bias),cmap=cmap,edgecolors='black')
    cbar = plt.colorbar(cax, shrink=.78, pad=0.02)
    cbar.ax.set_title(var_units)
    plt.title(plot_title)
    plt.tight_layout()

    plt.savefig(plot_outfile,format='png',dpi=400, bbox_inches='tight')

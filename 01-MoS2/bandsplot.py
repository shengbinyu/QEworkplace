import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

#Parameters
Emin = -9
Emax = -1
Efermi = (-5.8883 -4.2790)/2
xticks = [0, 0.5774, 0.9107, 1.5774]
xticklabels=['$\Gamma$', 'M', 'K', '$\Gamma$']

# Figure setting
plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(6, 5)

# load data
data = np.loadtxt('bands.dat.gnu')

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, alpha=1, color='k')

plt.xlim(min(k), max(k))
plt.ylim(Emin, Emax)

# Fermi energy
plt.axhline(Efermi, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)
# High symmetry k-points (check bands_pp.out)
for tick in xticks:
    plt.axvline(tick, linewidth=0.75, color='k', alpha=0.5)

# text labels
plt.xticks(ticks=xticks, labels=xticklabels)
plt.ylabel("Energy (eV)")
plt.savefig("bands.png")
plt.show()

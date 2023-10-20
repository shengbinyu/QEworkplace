import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

#Parameters
Emin = -13
Emax = 7
Efermi = (6.2178 + 6.9259) /2 
xticks = [0, 0.8660, 1.8660,2.2196, 3.2802]
xticklabels=['L','$\Gamma$', 'X', 'K', '$\Gamma$']

# Figure setting
plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(6, 5)

# load data
data = np.loadtxt('bands.dat.gnu')

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))

for band in range(len(bands)):
    plt.plot(k, bands[band, :]-Efermi, linewidth=1, alpha=1, color='k')

plt.xlim(min(k), max(k))
plt.ylim(Emin, Emax)

# Fermi energy
plt.axhline(0.0, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)
# High symmetry k-points (check bands_pp.out)
for i in range(1,len(xticks)):
    plt.axvline(xticks[i], linewidth=0.75, color='k', alpha=0.5)

# text labels
plt.xticks(ticks=xticks, labels=xticklabels)
plt.ylabel("Energy (eV)")
plt.savefig("bands.png")
plt.show()

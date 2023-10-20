set terminal postscript eps enhanced 28 lw 2
set output "GaAs.eps"
set ylabel 'Energy (eV)'

set ytics 5

unset key

x1 = 0.8660
x2 = 1.8660
x3 = 2.2932
xmax = 3.2844
ymin = -13
ymax = 7
ef = 6.7106

set xrange [0:xmax]
set yrange [ymin:ymax]
set xtics ("L" 0,"{/Symbol G}" x1, "X" x2, "K,U" x3, "{/Symbol G}" xmax)
set arrow 1 nohead from x1,ymin to x1,ymax lt 2
set arrow 2 nohead from x2,ymin to x2,ymax lt 2
set arrow 3 nohead from x3,ymin to x3,ymax lt 2

plot './GaAs.band.gnu' using 1:($2-ef) w l

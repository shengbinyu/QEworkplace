#!/bin/bash

TAG=silicon
NODES=6

QE_BIN_DIR=/usr/local/bin
EXECPW=${QE_BIN_DIR}/pw.x
EXECBD=${QE_BIN_DIR}/bands.x
EXECPL=${QE_BIN_DIR}/plotband.x

echo "-------------------------------------------------"
echo "(1) scf calculation      (2) nscf calculation"
echo "(3) bands calculation    (4) bands_pp calculation"
echo "(0) exit"
echo "-------------------------------------------------"
echo -n "Please choose:"
read INDEX

case ${INDEX} in
    1)
        echo "Perform scf calculation ..."
        mpirun -np ${NODES} ${EXECPW} -inp scf.in > scf.out &;;

    2)
        echo "Perform nscf calculation ..."
        mpirun -np ${NODES} ${EXECPW} -inp nscf.in > nscf.out &;;

    3)
        echo "Perform bands calculation ..."
        mpirun -np ${NODES} ${EXECPW} -inp bands.in > bands.out &;;

    4)
        echo "Perform bands_pp calculation ..."
        mpirun -np ${NODES} ${EXECBD} -inp bands_pp.in > bands_pp.out &;;

    0)
        echo "--> EXIT SUCCESSFUL <--"
esac



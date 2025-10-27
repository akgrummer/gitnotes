# Intructions to install fw on labc1 computer


git clone -b feature/update_LC --recurse-submodules ssh://git@gitlab.cern.ch:7999/cms-hgcal-firmware/engine_zcu.git

./project list 
./project create zcu102-ldv3-r1p0
./project build zcu102-ldv3-r1p0
./project xml zcu102-ldv3-r1p0

./project clean zcu102-ldv3-r1p0


# To send the fw to the zcu copy the two files with the names “sendFW*” from here on labc1
/home/agrummer/cass-fw/multiEngine

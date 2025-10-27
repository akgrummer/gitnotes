# Notes on how to operate system with pre-refactor

Still in development

repo: hgc-engine-tools
branch: V3_aidan_dev_preRefactoredCosmics
running script:
./config_aidan4mod.sh
to get clock and lpgbts in initial configuration

repo: cass-sw
branch: akg-prerefactor
using: ./gui_cass_operation.py
to configure the ROCs
clocks and link capture needs to be reworked to match previous versions of code

repo: cass-sw
branch: main
was (probably) used in past for configuring all parts of system with refactored fw


## 2024 Jul 24

clocks now can be setup in
repo: cass-sw
branch: akg-prerefactor
without hgc-engine-tools
do need this line though:
./uhal_backend_v3.py -b enginev3-backend-0 --node CTL.INVERT_RX_DATA_ORDER --val 0
before LC windows - should be added as button

Would be good to have options to change polarities in the gui for EPRX inputs
offsets are set in the code - not in the gui


PUSMstatus of east lpgbt is cycling between 0x10 and 0x13
mostly stuck at 0x10. 0x13 means ready.
This is true also using the zcu102-ldv3-r1p0-ROCv3 (prefactored?) and -
branch: main, repo: cass-sw

Tomorrow: will try on zcu1 setup






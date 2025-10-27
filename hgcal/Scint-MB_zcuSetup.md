# 2024 Feb 29

install new pip version

# zcu zcu_multitool
after fw load may need:
./hgc/zcu_multitool.py --status
./hgc/zcu_multitool.py --setrefclk
-- then set polarities
./hgc/zcu_multitool.py --resetlink

# Polarity settings:

# ./uhal_backend_v3.py -b backend-transceiver-right-0 --node CTL.RX_POLARITY --val 1024
./uhal_backend_v3.py -b backend-transceiver-right-0 --node CTL.RX_POLARITY --val 1024
./uhal_backend_v3.py -b backend-transceiver-right-0 --node CTL.TX_POLARITY --val 256

for multi-engine fw design:
./uhal_backend_v3.py -b transceivers-transceiver-left-0 --node CTL.RX_POLARITY
./uhal_backend_v3.py -b transceivers-transceiver-right-0 --node CTL.RX_POLARITY
./uhal_backend_v3.py -b transceivers-transceiver-left-0 --node CTL.TX_POLARITY
./uhal_backend_v3.py -b transceivers-transceiver-right-0 --node CTL.TX_POLARITY

./uhal_backend_v3.py -b transceivers-transceiver-left-0 --node CTL.RX_POLARITY --val 2816
./uhal_backend_v3.py -b transceivers-transceiver-left-0 --node CTL.RX_POLARITY --val 768
./uhal_backend_v3.py -b transceivers-transceiver-left-0 --node CTL.TX_POLARITY --val 2048

# configure with:

source startup_scint.sh
./setup_train_scint.py --all

# lpgbt status registers

./lpgbt_status.py --mode SCINT_V0 --dump --target DAQ

./lpgbt_status.py --mode SCINT_V0 --old --target DAQ --protocol ICEC

./lpgbt_status.py --mode SCINT_V0 --old --target DAQ2 --protocol ICEC
./lpgbt_status.py --mode SCINT_V0 --old --target DAQ2 --protocol ICI2C

 ./lpgbt_status.py --mode SCINT_V0 --old --target TRIG --protocol ICEC
 ./lpgbt_status.py --mode SCINT_V0 --old --target TRIG --protocol ICI2C

 ./lpgbt_status.py --backend 5 --type scintillator --mode SCINT_V0 --old --target DAQ --protocol ICEC


# Buses and Addresses:

MUST be in ic/ec source 0
IC_SOURCE = SIMPLE (0)   EC_SOURCE = SIMPLE (0)

```bash
[agrummer@zcufnal (hgc)]$ ./i2c_scan_engine.py --mode SCINT_V0
Checking for responses down stream from TRIG lpGBT
{'device_addr': 113, 'icec_type': 'EC', 'indirect_path': 'DAQ', 'indirect_bus': 0, 'lpgbt_type': 'TRG'}
Checking I2C Bus 0
 Found responses on following addresses
   112 0x70
Checking I2C Bus 1
 Found responses on following addresses
   32 0x20
Checking I2C Bus 2
 Found responses on following addresses
   32 0x20
Checking for responses down stream from DAQ lpGBT
{'device_addr': 112, 'icec_type': 'IC', 'indirect_path': None, 'indirect_bus': None, 'lpgbt_type': 'DAQ'}
Checking I2C Bus 0
 Found responses on following addresses
   113 0x71
Checking I2C Bus 1
 Found responses on following addresses
   80 0x50
Checking I2C Bus 2
 Found responses on following addresses
```

# econ

econs are on buses 1 and 2 of the trig lpgbt
both are on address 0x20 (where as Jeremy's were on 0x21) - see full print out of i2c scan above

configured one bit (run bit) on both econs and read back some registers
using swamp train_v3-SCA branch
had to comment out cache line in ECON.py in functions read_some()

# Organization:

in directory
mb-sw/
cloned hgc-engine-tools (V3-refactorfw) to hgc
cloned swamp
clone lpgbt library

using import sys
and adding hgc to path
sys.path.append('hgc')


use to switch the IC sources
enableEngine.sh
enableSwamp.sh

use lines in here for old register readings: lpgbt_snapshots.sh


# eight engine design:


zcu captures

for i in 0 1 2 3 4 5 6 7; do echo "ZCU CAPTURES FOR BACKEND ${i}"; for j in 0 1 2; do echo "OLINK ${j}"; ./zcu_multitool.py --capture --olink ${j} --backend ${i}; done; done

LINK CAPTURES:

for i in 0 1 2 3 4 5 6 7; do echo "FIFO FOR BACKEND ${i}";  ./uhal_backend_v3.py --fifo --backend ${i} --lpgbt trig; done
for i in 0 1 2 3 4 5 6 7; do echo "FIFO FOR BACKEND ${i}";  ./uhal_backend_v3.py --fifo --backend ${i}; done


To summarize state with with eight-engine design (after a fw-load and configuration and then setting lpgbts to fixed pattern mode).

I saw fixed pattern data seen on zcu capture and not on LC capture (L1A mode)

non-sense data seen with zcu capture:
backend 3 olink 1
backend 4 olink 2
backend 6 olink 1 and 2
backend 7 olink 1

non-sense data on link capture:
DAQ:
backend 3
trig:
backend 4 links 7-13
backend 6 all links
backend 7 links 0-6

these engines aren't connected to anything (scint motherboard should be on engine 5)
**would match except: backend 3 olink 1 nonsense data should be on trigger links in LC not on DAQ links.**

for example, backend 4
zcu capture doesn't quite match LC capture:

```bash
[agrummer@zcufnal (hgc-engine-tools)]$ ./zcu_multitool.py --capture --olink 2 --backend 4
       0        1        2        3        4        5        6
294a5294 4a94a525 5294a529 ad694a52 5b5ad6b5 5ad6ad6b b5b5ad41
294a5294 4a94a525 5294a529 ad694a52 5b5ad6b5 5ad6ad6b b5b5ad41
294a5294 4a94a525 5294a529 ad694a52 5b5ad6b5 5ad6ad6b b5b5ad41
294a5294 4a94a525 5294a529 ad694a52 5b5ad6b5 5ad6ad6b b5b5ad41
```

```bash
[agrummer@zcufnal (hgc-engine-tools)]$ ./uhal_backend_v3.py --fifo --backend 4 --lpgbt trig
...
link 7    link 8    link 9    link 10    link 11    link 12    link 13
--------  --------  --------  ---------  ---------  ---------  ---------
294a5294  a4a52952  94a5294a  4a5296b5   ad6b5ada   d6b56b5a   82b5adad
294a5294  a4a52952  94a5294a  4a5296b5   ad6b5ada   d6b56b5a   82b5adad
294a5294  a4a52952  94a5294a  4a5296b5   ad6b5ada   d6b56b5a   82b5adad
294a5294  a4a52952  94a5294a  4a5296b5   ad6b5ada   d6b56b5a   82b5adad
294a5294  a4a52952  94a5294a  4a5296b5   ad6b5ada   d6b56b5a   82b5adad
294a5294  a4a52952  94a5294a  4a5296b5   ad6b5ada   d6b56b5a   82b5adad
```


# back to single scint fw

## ZCU capture:

./hgc/zcu_multitool.py --capture --lpgbtnum 0
./hgc/zcu_multitool.py --capture --lpgbtnum 1
./hgc/zcu_multitool.py --capture --lpgbtnum 2



loaded fw. and setrefclk
set normal polarizations (RX:1024, TX:256)
resetlink - DAQ clock DV is good

- used just Fabian confgis:
- had to power cycle but then: PUSMStatus good
- took snapshot (need to enableEngine.sh first)
(_fabianConfigs_and_startupScint3)
- clock rates not good for trig or daq2

- then ran startup_scint.sh
- trig clock good
PUSMStatus still good for all
- took snapshot (need to enableEngine.sh first)
(see _fabianConfigs_and_startupScint3 snapshots)


with open(self.regmapfile,'rb') as fin:
    self.regmap = pickle.load(fin)


for key,val  in regmap.items():
    print(int(val['address'],16), val['address'], key)



again:
loaded fw. and setrefclk: DAQ clk is only one that is good
set normal polarizations (RX:1024, TX:256)
resetlink - DAQ clock DV is good


- then ran startup_scint.sh
- sca check is good
- trig clk is good (daq2 clk bad)
- didn't check - but presumably PUSMStatus was still bad for daq2 lpgbt
- take a snapshot
(see _startupScint snaps)


the run fabian configs:
- PUSMStatus is good on daq2 lpgbt
- daq2 clk is still bad
- sca check broken
(see _startupScint_thenFabianConfigs snaps

run startup_scint again
- sca_check is good again
PUSMStatus good on all lpgbts
- clk rate is bad for daq2
- take another snapshot



Check snapshots:
startup_scint to fabian config
snap shot for DAQ lpgbt

PUSM becomes good for DAQ2
sca check becomes bad.





----------------

change ECLk4 to 39 (instead of 3c) in Fabians DAQ config
EPCLK4CHNCNTRH
reload fw
- no changes in results: DAQ2 PUSM good but DV-40 clk bad. No SCA


change in hgc gpio setup:
53 and 55 set to 0 (instead of 0x60
~/mb-sw/./hgc/setup_lpgbt.py
  1         if self.__mode.generalType() == Mode.SCINT:
331             for lpgbt_id in self.lpgbts:
  1                 if lpgbt_id in ["DAQ"]:
  2                     #gpio 0 is ECON_RE_Hb, gpio1 is ECON_RE_Sb, gpio13 is fake-DAQ-rest, gpio 14 is trigger lpgbt reset, gpio15 is trigg ready
  3                     # self.iic.write_lpgbt(0x053,0x60, lpgbt_id)
  4                     self.iic.write_lpgbt(0x053,0x00, lpgbt_id)
  5                     self.iic.write_lpgbt(0x054,0x03, lpgbt_id)
  6                     #cycle the reset for ECONs
  7                     # self.iic.write_lpgbt(0x055,0x60, lpgbt_id)
  8                     self.iic.write_lpgbt(0x055,0x00, lpgbt_id)
  9                     self.iic.write_lpgbt(0x056,0x00, lpgbt_id)
 10                     self.iic.write_lpgbt(0x056,0x03, lpgbt_id)






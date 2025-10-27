# Cold Tests 2023 Nov 27


797k events - NIM module counter
can we run for 2 weeks straight - to characterize a module?

Stopped overnight Run from Sunday at 2:45 fnal time (2023Nov22_TurkeyRun2)
Web cam for services


- RTDs connected in the box:
   1. Return C02 line 
   2. Supply line
   3. Ambient near services hole
   4. cooling plate (north side of modules)
   5. on ROC S1 (north west on module)
   6. on ROC (south on module)
   7. on ROC (NE on module)
   8. on DAQ lpgbt
   9. on VTRX
   10. Bottom  scintillator plane

   13. Hexaboard East
   14. SW corner on module East
   15. TOP scintillator plane

   19. LDO
   20. Rafael


Keep track of 
- Dew Point 
- Leakage Current 
- Cooling plate temperature
- supply line temp
- return line temp
- bit alignment on all links
- noise level

Timeline:

RTDs attached at 4:00 pm
took warm data Run 1 for a few minutes
Cooling started at 16:45
run 2 also started

taking intermittent lpgbt status snapshots


cooling plate 2 degrees
cooling plate -1 deg

16:54 - CO2 leaking noticed

16:55 dew point -36
coolin plate at -5
16:56 cooling plate at -8
16:57 cooling plate at -12
16:58 cooling plate at -16
16:59
RTD on daq lpgbt 13 deg

17:00 cooling plat at -20
17:02
hexaboard is -9
cooling plate -2
dew point -40

17:06 
data corruption on East module Roc1
module is -12
cooling plat -24

17:08 start run 3
Run3_afterroc1eIssue

17:11
cooling plat -25
module -15

17:15
cooling plate at -26
module at -20

17:17: co2 is leaking again

17:20
DAQ lpgbt at 0 deg
module at -21

17:27
cooling plate: -28
module -22
daq -2

17:30 start Run4
top scintillator at +11


full lpgbt reg scan:
./lpgbt_snapshot.sh 2023Nov27_coldTest_17h36



cooling plate -29
module -23

17:43
module -24
cooling plat -29
lpgbt -4
vtrx -3
box -2


17:49
nominal current draw for LV: 5.2A onthe 1.5V, 0.4V on the 1.2, 0.9A 
module -24
cooling plate -29
ambient is -2

18:05 
turn on fan

18:09
ambient temp -8
daq -7
vtrx -5 (always 2 deg warmer than daq)

18:16
reached ambient temperature -8
18:20 ambient temp -10
daq lpgbt -8

18:29
ambient -11.5
daq -8.5
cooling plate -30 (ambient temperature is skewing measurement)
top scintillator is -1

18:41 start Run 5
ambient -13
cooling -30.5
daq -9.5
top scintillator -3
module -25

18:45 Restart temperature run

18:55 run 5 looks good, idle patterns not bit shifted for all rocs, lpgbt status reports (--old) still reporting

22:34 started run 6
corruption observed in ADC data  in run 5 (pedestal has multiple peaks)
idle patterns look ok 
lpgbt status reports are still working

22:50 run 7 after trying LC re-configure
ADC peak is large
no cosmics observed on any roc

23:25 begin reconfig of system with

config_aidan2.sh
branch V3_aidan

reconfig was successful
output copied to file

23:29
data looks ok on manual trigger (gui)

23:34
took full lpgbt register snapshots after sys config (to compare with the snapshots after data corruption was observed)

EPRX CurrentPhase values are different now:
```
[agrummer@zcufnal (hgc-engine-tools)]$ diff snapshots/trg_e_2023Nov27_coldTest_23h34_afterSysReconfig.txt snapshots/trg_e_2023Nov27_coldTest_23h13_afterDataCorruptionObserved.txt
340c340
< 339,0x153,0xf6
---
> 339,0x153,0xf1
352c352
< 351,0x15f,0xf8
---
> 351,0x15f,0xf7
355c355
< 354,0x162,0xf9
---
> 354,0x162,0xf8
[agrummer@zcufnal (hgc-engine-tools)]$ diff snapshots/trg_w_2023Nov27_coldTest_23h34_afterSysReconfig.txt snapshots/trg_w_2023Nov27_coldTest_23h13_afterDataCorruptionObserved.txt
346c346
< 345,0x159,0xf9
---
> 345,0x159,0xf1
355c355
< 354,0x162,0xf7
---
> 354,0x162,0xf5
```

some clock related registers on the daq lpbgt are different:
```
agrummer@zcufnal (hgc-engine-tools)]$ diff snapshots/daq_2023Nov27_coldTest_23h34_afterSysReconfig.txt snapshots/daq_2023Nov27_coldTest_23h13_afterDataCorruptionObserved.txt
343c343
< 342,0x156,0xfd
---
> 342,0x156,0xf5
448c448
< 447,0x1bf,0x08
---
> 447,0x1bf,0x07
451c451
< 450,0x1c2,0xe8
---
> 450,0x1c2,0x68
475c475
< 474,0x1da,0x05
---
> 474,0x1da,0x04
479c479
< 478,0x1de,0x05
---
> 478,0x1de,0x04
492c492
< 491,0x1eb,0x15
---
> 491,0x1eb,0x12
```


23:52 data in run 8 is still corrupted
configure system attempt 2

```
for module e0, roc: 0x08
lpgbt_control_lib.lpgbt_exceptions.LpgbtI2CMasterTransactionError: The last transaction was not acknowledged by the I2C slave
```




reran roc configs for e0 roc 0x08 and roc 0x18
and w0 0x08


00:14 collected 1000 events for run 9


00:23 data corrupted still on all rocs in run 9
power down rocs (powerDownRocs.sh)
attempting to reconfigure trial 3

00:27 i2c failed to w0 roc 0x28
failed for both config files this time

```
lpgbt_control_lib.lpgbt_exceptions.LpgbtI2CMasterBusError: The SDA line is pulled low before initiating a transaction.
lpgbt_control_lib.lpgbt_exceptions.LpgbtTimeoutError: Timeout while waiting for I2C master to finish (status:0x00)
```


00:41 can't configure w0 roc 0x28 
gpio cycling didn't help

00:51 trial 4 reconfigure
all rocs on west module not accepting i2c:
```
lpgbt_control_lib.lpgbt_exceptions.LpgbtI2CMasterBusError: The SDA line is pulled low before initiating a transaction.
```

01:00 tried I2C master reset on west trigger lpgbt
same message as before
```
lpgbt_control_lib.lpgbt_exceptions.LpgbtI2CMasterBusError: The SDA line is pulled low before initiating a transaction.
```


01:01 try to reconfigure again trial 5
configuration successful
manual triggers data missing on 1 half roc on west module - only see idle words there

01:18 (TRIAL 6) reconfigure swamp section (rocs)
succsesful roc config
manual triggers look good (gui) packet is back to nominal offset (3 idles at beginning of capture)

01:20 started run 11
01:26 bit shift in one half roc
reconfigure LC, manual trigger capture looks good, back to nominal idles

01:29 start run 12
 
01:55 run appears to be stable
adc noise seems a bit large 
ADC plot looks much better than run 5


2023 Nov28
10:16
leakage current is too high - hit the limit
HV dropped to ~50V
noise would increase with capacitance
don't have log of dew point
dew point -38

WEST module is bent - stressed inside the box 
should have a camera inside the box
window in box

opening box dew point dropped
leakage current is getting worse
humidity 

10:40
HV at ~49V

10:54 start run 13
ColdTest_Run13_afterHVissueDiscovered

questions
What is the HV current limit?
dew point level:

18:51
- data wasn't triggering
- some several links had misaligned idle words
reconfigured the LCs - idles words are realigned, 3 words offset in capture
- tried starting run 14. No trigger.


19:00
West module is completely shorted
- died slowly
- hypothesis is that it was the warping
- had 4 screws on each module

now put 6 screws on the east module

19:02 start a new run for temperatures
everything is at room temp
21C

19:03
pmt HV was turned on and run 14 started 
- idle words on several EAST links were misaligned 
- stopped run and reconfigured LCs

19:06 started run 15
at room temperature
19:09 200 events, idles still look good



 we were hooked up to nitrogen
 pressure varies
- no sign of moisture
- west module was very bent
- 


19:20
co2 presssure is lower than last night
19:21
co2supply line at 3 deg
19:23
co2 supply is -18C
cooling plate is 21
19:29
cooling plate is 18
started cooling

19:36
cooling plate at 10

19:46
cooling plate 0
dew point is -40

cooling plate is -6
cooling plate is at -20


leakage current: 0.3 uA
one module connected

20:10 
last 1000 events of run 15 seem to have good noise.

2023 Nov 30
14:19 stopped run 15


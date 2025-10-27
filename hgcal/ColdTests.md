# ColdTest notes

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

   13. Hexaboard
   14. SW corner on module
   15. TOP scintillator plane
   
   19. LDO
   20. Rafael

around 2:05 Started at 40% humidity
quickly humidity was 37%
dew point 6 or 10 at start of run (should be double checked at room temp)
HV on module: -500nA (probably)

HV on at 2:11pm
CO2 opened a little


started RTD measurements at 2:14
Started run on zcu2 at 2:18 Oct21

humidiy
dew point -11

2:23 - supply line (RTD2) at -2 deg C
expect cooling plate (RTD4) to go down next

VTRX is the highest temp at ~31
2:25 cooling plate drops a degree
2:25 -400 nA 

2:27 - dew point -17
cooling plat - 16degC

2:30 leakage current: -330 nA 

stop run at zcut at 2:34 (corrupted data on ROC 3)
started run on zcut at 2:36 

2:37
leakage -300 nA
dew point -25

2:38:
cooling plate goes down one degree per minute
hexaboard is 11 and jk

2:46
cooling plat is -1
-280nA

2:52
dew point: -33 


2:54
dew point: -34
hexaboard temp: +1C

307
air is at 7
bottom scintillat still 17
leakage - not decreasing - 280nA
cooling plate caught up with supply RTD - probably supply RTD is not in contact anymore


stop run at 
stop run at zcut at 3:50 (some very noisy channels...??)
reconigure at 3:56 - issue reading I2C

4:25 - turn off cooling
4:29 - dew point: -49

# E lpgbt status stops working

```
Reading E
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools/./lpgbt_status.py", line 80, in <module>
    chipid = read_chip_ID(myengine, args.target)
  File "/home/agrummer/hgc-engine-tools/./lpgbt_status.py", line 12, in read_chip_ID
    fusedatavalid = myengine.read_lpgbt(fuse_ro_base+0,1,target)[0] & (1 << 2)
IndexError: list index out of range
EAST is the dll status good? 0x1d9 to read 13, press any key to continue...^C
```

# ROC GPIO resets fail
```
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
```

4:02 - hexaboard 1 degree colder - after powering off the rocs
4:03 - HV leakage current drops to 0.035 uA after power supply to module off
ROCs are cooling down

# DAQ STATus:

```
[agrummer@zcufnal (hgc-engine-tools)]$ ./lpgbt_status.py --mode V3_ALL -t DAQ --old
Reading DAQ
chipid : 2118439643 (0x7e44d2db)
000 : 00
001 : 00
002 : 00
003 : 00
004 : 00
005 : 00
006 : 00
007 : 00
033 : 00
053 : c0
054 : 00
055 : c0
056 : 00
0f9 : 00
0fa : 00
0fb : 06
150 : b2
152 : f2
155 : f2
168 : c0
169 : c0
16a : c0
16b : c0
16c : c0
16d : c0
16e : c0
1c6 : 00
1c7 : 00
1c8 : 00
1c9 : 00
1d9 : 13
1da : 00
1db : 00
1dc : 00
1dd : 01
1de : 00
1df : 00
1e8 : 05
1e9 : 00
1ea : 00
1eb : 03
```

# Trig status
git branch: V3_aidan
commit:
025d47db1a310ed9aabc3ca08aa0fba461283650

```
[agrummer@zcufnal (hgc-engine-tools)]$ ./lpgbt_status.py --mode V3_ALL -t E --old
Reading E
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools/./lpgbt_status.py", line 80, in <module>
    chipid = read_chip_ID(myengine, args.target)
  File "/home/agrummer/hgc-engine-tools/./lpgbt_status.py", line 12, in read_chip_ID
    fusedatavalid = myengine.read_lpgbt(fuse_ro_base+0,1,target)[0] & (1 << 2)
IndexError: list index out of range
```

# more DAQ

```
er@zcufnal (hgc-engine-tools)]$ ./lpgbt_status.py --mode V3_ALL -t DAQ
Reading DAQ
chipid : 2118439643 (0x7e44d2db)
Powerup State Machine : (0x13) READY
   PUSMCHANNELSTIMEOUT (Channel Locking Timeouts) : 0
   PUSMDLLTIMEOUT (DLL Timeouts) : 0
   PUSMPLLTIMEOUT (PLL Timeouts) : 0
   PUSMBROWNOUTWATCHDOG (Brownout counter) : 1
   PUSMDLLWATCHDOG (DLL Watchdog Errors) : 0
   PUSMPLLWATCHDOG (PLL Watchdog Errors) : 0
```

# ROC GPIO setup:

```
[agrummer@zcufnal (hgc-engine-tools2)]$ ./doSetup.sh
lpGBT Status
Reading daq lpgbt
chipid : 2118439643 (0x7e44d2db)
000 : 00
001 : 00
002 : 00
003 : 00
004 : 00
005 : 00
006 : 00
007 : 00
033 : 00
053 : c0
054 : 00
055 : c0
056 : 00
0f9 : 00
0fa : 00
0fb : 06
150 : b2
152 : f2
155 : f2
168 : c0
169 : c0
16a : c0
16b : c0
16c : c0
16d : c0
16e : c0
1c6 : 00
1c7 : 00
1c8 : 00
1c9 : 00
1d9 : 13
1da : 00
1db : 00
1dc : 00
1dd : 01
1de : 00
1df : 00
1e8 : 05
1e9 : 00
1ea : 00
1eb : 03
Starting Reset Line Status
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'EAST.HGCROC_RE_Sb0' => False
'EAST.PG_LDO0' => False
Come out of reset
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Reset ROC
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 141, in <module>
    write_many_substring(myiic,args.low,False)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Starting Reset Line Status
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'WEST.PG_LDO0' => False
Come out of reset
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Reset ROC
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 141, in <module>
    write_many_substring(myiic,args.low,False)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 141, in <module>
    write_many_substring(myiic,args.low,False)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Reset Line Status
'EAST.PWR_EN0' => False
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'EAST.PG_LDO0' => False
'WREADY' => True
'EREADY' => True
Reset Line Status
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'WEST.HGCROC_RE_Hb0' => False
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'WEST.PG_LDO0' => False
'WREADY' => True
'EREADY' => True
```

# Retry config at 4:35
-20 on the plate


no trig lpgbt status
some ROC gpios read false - many error messages though

```
[agrummer@zcufnal (hgc-engine-tools)]$ ./config_aidan2.sh 
going to load fw again, press any key to continue...
loading custom firmware
Time taken to load DTBO is 12499.000000 Milli Seconds
DTBO loaded through zynqMP FPGA manager successfully
Current polarity: 5
Current polarity: 7
 Back FW 0000  Backend Status = 0177711b
 Errors =     0   Unlocks =    0  RX Polarity = 3
     100 MHz: 100.00000000 MHz
         Ref: 320.64000000 MHz
          TX: 320.64010000 MHz
        TX40: 40.08000000 MHz
         RX0: 321.27410000 MHz
         RX1: 320.07350000 MHz
         RX2: 321.25280000 MHz
      RX0-DV: 0.00000000 MHz
      RX1-DV: 0.00000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes:
   EGROUP0: (0)          FastControl
   EGROUP1: (0)          FastControl
   EGROUP2: (0)          FastControl
   EGROUP3: (0)          FastControl
does polarity == 3?, press any key to continue...
Reseting the link
 Status = 0x777119
 Back FW 0000  Backend Status = 3175701b
 Errors =     0   Unlocks =    1  RX Polarity = 3
     100 MHz: 100.00000000 MHz
         Ref: 320.63990000 MHz
          TX: 320.63990000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.63990000 MHz
         RX1: 319.94180000 MHz
         RX2: 320.63990000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 40.08000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes:
   EGROUP0: (0)          FastControl
   EGROUP1: (0)          FastControl
   EGROUP2: (0)          FastControl
   EGROUP3: (0)          FastControl
is the daq RX0-40 correct?, press any key to continue...
setup VTRX:  1
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Run the link trick
DAQ
E
W
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Run the link trick
DAQ
W
E
 Back FW 0000  Backend Status = 7176701b
 Errors =     4   Unlocks =    1  RX Polarity = 3
     100 MHz: 100.00000000 MHz
         Ref: 320.63990000 MHz
          TX: 320.63990000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.63990000 MHz
         RX1: 320.64000000 MHz
         RX2: 320.63990000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 40.08000000 MHz
      RX2-DV: 40.08000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes:
   EGROUP0: (0)          FastControl
   EGROUP1: (0)          FastControl
   EGROUP2: (0)          FastControl
   EGROUP3: (0)          FastControl
are all clocks good?, press any key to continue...
Reading E
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools/./lpgbt_status.py", line 80, in <module>
    chipid = read_chip_ID(myengine, args.target)
  File "/home/agrummer/hgc-engine-tools/./lpgbt_status.py", line 12, in read_chip_ID
    fusedatavalid = myengine.read_lpgbt(fuse_ro_base+0,1,target)[0] & (1 << 2)
IndexError: list index out of range
EAST is the dll status good? 0x1d9 to read 13, press any key to continue...
Reading W
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools/./lpgbt_status.py", line 80, in <module>
    chipid = read_chip_ID(myengine, args.target)
  File "/home/agrummer/hgc-engine-tools/./lpgbt_status.py", line 14, in read_chip_ID
    fusedatavalid = myengine.read_lpgbt(fuse_ro_base+0,1,target)[0] & (1 << 2)
IndexError: list index out of range
WEST is the dll status good? 0x1d9 to read 13, press any key to continue...
changing directories "cd ~/hgc-engine-tools" to go back, press any key to continue...
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Run the link trick
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Run the link trick
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
 Back FW 0000  Backend Status = 7174701b
 Errors =     8   Unlocks =    1
     100 MHz: 100.00000000 MHz
         Ref: 320.63990000 MHz
          TX: 320.63990000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.63990000 MHz
         RX1: 320.64000000 MHz
         RX2: 320.63990000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 40.08000000 MHz
      RX2-DV: 40.08000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
lpGBT Status
Reading daq lpgbt
chipid : 2118439643 (0x7e44d2db)
000 : 00
001 : 00
002 : 00
003 : 00
004 : 00
005 : 00
006 : 00
007 : 00
033 : 00
053 : c0
054 : 00
055 : c0
056 : 00
0f9 : 00
0fa : 00
0fb : 06
150 : b2
152 : f2
155 : f2
168 : c0
169 : c0
16a : c0
16b : c0
16c : c0
16d : c0
16e : c0
1c6 : 00
1c7 : 00
1c8 : 00
1c9 : 00
1d9 : 13
1da : 00
1db : 00
1dc : 00
1dd : 01
1de : 00
1df : 00
1e8 : 05
1e9 : 00
1ea : 00
1eb : 03
Starting Reset Line Status
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'EAST.HGCROC_RE_Hb0' => False
'EAST.HGCROC_RE_Sb0' => False
'EAST.PG_LDO0' => False
Come out of reset
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Reset ROC
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 141, in <module>
    write_many_substring(myiic,args.low,False)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Starting Reset Line Status
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'WEST.HGCROC_RE_Hb0' => False
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'WEST.PG_LDO0' => False
Come out of reset
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Reset ROC
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 141, in <module>
    write_many_substring(myiic,args.low,False)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 141, in <module>
    write_many_substring(myiic,args.low,False)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 147, in <module>
    write_many_substring(myiic,args.high,True)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 117, in write_many_substring
    __iwrite(iic,gpio_map[item],value)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 77, in __iwrite
    if isinstance(rval,list): rval=rval[0]
IndexError: list index out of range
Reset Line Status
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'EAST.HGCROC_RE_Hb0' => False
'EAST.HGCROC_RE_Sb0' => False
'EAST.PG_LDO0' => False
'WREADY' => True
'EREADY' => True
Reset Line Status
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 150, in <module>
    values=read_many_substring(myiic,args.read)
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 111, in read_many_substring
    result[item]=__iread(iic,gpio_map[item])
  File "/home/agrummer/hgc-engine-tools2/./gpio_control.py", line 65, in __iread
    if isinstance(val,list): val=val[0]
IndexError: list index out of range
'WEST.HGCROC_RE_Sb0' => False
'WEST.PG_LDO0' => False
'WREADY' => True
'EREADY' => True
Setup HGCROC
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./roc_test.py", line 85, in <module>
    i2c.write_roc_direct(roc,45,0,0b10101011)
  File "/home/agrummer/hgc-engine-tools2/engine_comm.py", line 162, in write_roc_direct
    self.myiic.write_i2c_indirect(roc_full_addr0, [R0])
  File "/home/agrummer/hgc-engine-tools2/iic.py", line 165, in write_i2c_indirect
    status = self.read_lpgbt(i2cstatus_base+2)[0]
IndexError: list index out of range
 Back FW 0000  Backend Status = 7174701b
 Errors =     8   Unlocks =    1
     100 MHz: 100.00000000 MHz
         Ref: 320.63990000 MHz
          TX: 320.64000000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.63990000 MHz
         RX1: 320.63990000 MHz
         RX2: 320.64000000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 40.08000000 MHz
      RX2-DV: 40.08000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
roc:  1
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./lpgbt_aidan.py", line 214, in <module>
    gen_configROCread()
  File "/home/agrummer/hgc-engine-tools2/./lpgbt_aidan.py", line 168, in gen_configROCread
    train_v3.readROC_sub(i, 43, 14)
  File "/home/agrummer/hgc-engine-tools2/./lpgbt_aidan.py", line 67, in readROC_sub
    output = self.roci2c.read_roc_direct(roc,sub_addr,reg)
  File "/home/agrummer/hgc-engine-tools2/engine_comm.py", line 174, in read_roc_direct
    self.myiic.write_i2c_indirect(roc_full_addr0, [R0])
  File "/home/agrummer/hgc-engine-tools2/iic.py", line 165, in write_i2c_indirect
    status = self.read_lpgbt(i2cstatus_base+2)[0]
IndexError: list index out of range
CTL.INVERT_RX_DATA_ORDER: 0
```


# Retry config at -15
and again at -6 and -4
no luck

#
[agrummer@zcufnal (hgc-engine-tools2)]$ ./lpgbt_status.py --target A
Reading daq lpgbt
chipid : 2118439643 (0x7e44d2db)
000 : 00
001 : 00
002 : 00
003 : 00
004 : 00
005 : 00
006 : 00
007 : 00
033 : 00
053 : c0
054 : 00
055 : c0
056 : 00
0f9 : 00
0fa : 00
0fb : 06
150 : b2
152 : f2
155 : f2
168 : c0
169 : c0
16a : c0
16b : c0
16c : c0
16d : c0
16e : c0
1c6 : 00
1c7 : 00
1c8 : 00
1c9 : 00
1d9 : 13
1da : 01
1db : 00
1dc : 00
1dd : 01
1de : 01
1df : 00
1e8 : 05
1e9 : 00
1ea : 00
1eb : 06
[agrummer@zcufnal (hgc-engine-tools2)]$ ./lpgbt_status.py --target C
Reading trigger lpgbt C
Traceback (most recent call last):
  File "/home/agrummer/hgc-engine-tools2/./lpgbt_status.py", line 62, in <module>
    chipid = read_chip_ID(myengine,args.target)
  File "/home/agrummer/hgc-engine-tools2/./lpgbt_status.py", line 14, in read_chip_ID
    fusedatavalid = myengine.read_lpgbt(fuse_ro_base+0,1,target)[0] & (1 << 2)
IndexError: list index out of range



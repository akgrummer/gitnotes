0 I PLL_LCK DAC 0 REF_HV0 (21k)
1 I ERROR 1 REF_HV0 (100k)
2 O SOFT_RSTB 2 REF_HV1 (21k)

3 O I2C_RSTB 3 REF_HV1 (100k)
4 O HARD_RSTB
# 5 I PLL_LCK 2nd ROC
# 6 I ERROR 2nd ROC
7 O LED_ON_OFF
8 O LED_DISABLE1
9 O LED_DISABLE2
10 O LED_DISABLE3
11 O LED_DISABLE4
12 O LED_DISABLE5
13 O LED_DISABLE6
14 O LED_DISABLE7
15 O LED_DISABLE8
# 16 O LED_DISABLE1 2nd ROC
# 17 O LED_DISABLE2 2nd ROC
# 18 O ENHV0 (2nd Aldo)
# 19 O ENHV1 (2nd Aldo)
20 O ENHV0 (Aldo)
21 O ENHV1 (Aldo)
22 O EN_LDO (VDDD, VDDA)
23 O SOFTSTART (VDDA, VDDD)
24 O M50MV_VDDD
25 O P50MV_VDDD
26 O M50MV_VDDA
27 O P50MV_VDDA
28 I PG_LDO
29 I OCZ_LDO
# 30 O LED_DISABLE3 2nd ROC
# 31 O LED_DISABLE4 2nd ROC



8 VCC_GBTSCA (1k/1k)
9 MPPC_BIAS1 (324k/6.49k)
10 MPPC_BIAS2 (324k/6.49k)
11 VCC_IN (14k/1k)
12 LED_BIAS (14k/1k)
13 VPA (3k/1k)
14 PRE_VPA (3k/1k)
15 VDDA (1k/1k)
16 VDDD (1k/1k)
17 PRE_VDDA (1k/1k)
18 MPPC_BIAS_IN (324k/6.49k)
22 PROBE_DC_L1
23 PROBE_PA_L (inDACs)
24 PROBE_DC_R1
25 PROBE_PA_R (inDACs)
26 BOARD_ID_0 (LSB)
27 BOARD_ID_1 (MSB)
29 CURHV0 (ALDO)
30 CURHV1 (ALDO)



## DATA: GPIOs and ADCs:

- GPIO and ADC values are shown here for 4 of the boards on the 10deg cassette.
- Notes relavent to this data are provided below.

```bash
------ GPIO STATUS -------
tileboard                       A     B     D     E
PLL_LCK              (gpio 0):  1     1     1     1
ERROR                (gpio 1):  1     1     1     1
SOFT_RSTB            (gpio 2):  1     1     1     1
I2C_RSTB             (gpio 3):  1     1     1     1
HARD_RSTB            (gpio 4):  1     1     1     1
LED_ON_OFF           (gpio 7):  0     0     0     0
LED_DISABLE1         (gpio 8):  0     0     0     0
LED_DISABLE2         (gpio 9):  0     0     0     0
LED_DISABLE3         (gpio 10): 0     0     0     0
LED_DISABLE4         (gpio 11): 0     0     0     0
LED_DISABLE5         (gpio 12): 0     0     0     0
LED_DISABLE6         (gpio 13): 0     0     0     0
LED_DISABLE7         (gpio 14): 0     0     0     0
LED_DISABLE8         (gpio 15): 0     0     0     0
ENHV0_Aldo           (gpio 20): 0     0     0     0
ENHV1_Aldo           (gpio 21): 0     0     0     0
EN_LDO_VDDD_VDDA     (gpio 22): 1     1     1     1
SOFTSTART_VDDA_VDDD  (gpio 23): 1     1     1     1
M50MV_VDDD           (gpio 24): 0     0     0     0
P50MV_VDDD           (gpio 25): 0     0     0     0
M50MV_VDDA           (gpio 26): 0     0     0     0
P50MV_VDDA           (gpio 27): 0     0     0     0
PG_LDO               (gpio 28): 1     1     1     1
OCZ_LDO              (gpio 29): 1     1     1     1
```

```bash
------ ADC STATUS -------
tileboard                          A              B              D              E
Chip Serial Num.                   28158          28012          49976          49933
PT1000 - T2 method 1     (pin 0):  35.9 C         29.3 C         32.0 C         36.1 C
PT1000 - T2 method 2     (pin 0):  33.9 C         24.4 C         27.8 C         34.5 C
PT1000 - T4 method 1     (pin 1):  35.9 C         28.6 C         29.8 C         35.6 C
PT1000 - T4 method 2     (pin 1):  34.5 C         23.5 C         24.9 C         33.4 C
PT1000 - T1 method 1     (pin 2):  35.8 C         27.9 C         30.9 C         36.7 C
PT1000 - T1 method 2     (pin 2):  33.6 C         22.4 C         26.5 C         35.2 C
PT1000 - T6 method 1     (pin 3):  33.8 C         ---            28.1 C         34.6 C
PT1000 - T6 method 2     (pin 3):  30.9 C         ---            22.8 C         32.1 C
PT1000 - T3 method 1     (pin 4):  35.0 C         28.3 C         30.3 C         35.6 C
PT1000 - T3 method 2     (pin 4):  33.6 C         22.4 C         25.6 C         33.6 C
PT1000 - T8 method 1     (pin 5):  34.4 C         27.0 C         29.2 C         34.7 C
PT1000 - T8 method 2     (pin 5):  31.8 C         20.4 C         24.0 C         32.3 C
PT1000 - T7 method 1     (pin 6):  34.8 C         28.0 C         29.3 C         34.5 C
PT1000 - T7 method 2     (pin 6):  32.1 C         21.9 C         24.0 C         32.1 C
PT1000 - T5 method 1     (pin 7):  34.2 C         ---            27.8 C         34.8 C
PT1000 - T5 method 2     (pin 7):  31.6 C         ---            21.9 C         32.5 C
Int reference temp.      (pin 31)  27.3 C         26.7 C         26.5 C         25.1 C
-----
MPPC_BIAS_IN             (pin 18):  0.0000 V       0.0124 V       0.0000 V       0.0124 V
MPPC_BIAS1               (pin 9):   0.0000 V       0.0000 V       0.0000 V       0.0000 V
MPPC_BIAS2               (pin 10):  0.0000 V       0.0000 V       0.0000 V       0.0124 V
CURHV0                   (pin 29):  0.000  V       0.001  V       0.000  V       0.000  V
CURHV0 : current         (pin 29):  0.000  mA      0.036  mA      0.000  mA      0.007  mA
CURHV1                   (pin 30):  0.000  V       0.001  V       0.000  V       0.000  V
CURHV1 : current         (pin 30):  0.000  mA      0.036  mA      0.000  mA      0.000  mA
VCC_IN                   (pin 11): 10.111  V      10.149  V      10.121  V      10.171  V
LED_BIAS                 (pin 12):  9.140  V       8.723  V       9.121  V       9.092  V
VPA           [+2.5V]    (pin 13):  2.545  V       2.509  V       2.521  V       2.550  V
VCC_GBTSCA               (pin 8):   1.578  V       1.589  V       1.543  V       1.580  V
PRE_VPA       [~ +3.5V]  (pin 14):  3.100  V       3.070  V       3.132  V       3.128  V
VDDA          [+1.2V]    (pin 15):  1.198  V       1.221  V       1.218  V       1.203  V
VDDD          [+1.2V]    (pin 16):  1.176  V       1.242  V       1.221  V       1.213  V
PRE_VDDA      [+1.5V]    (pin 17):  1.517  V       1.495  V       1.452  V       1.472  V
TB_ID0 [+0.2V]           (pin 26):  0.000  V       0.000  V       0.000  V       0.001  V
TB_ID1 [+0.0V]           (pin 27):  0.292  V       0.308  V       0.303  V       0.301  V
PROBE_DC_L1              (pin 22):  0.781  V       0.157  V       0.232  V       0.421  V
PROBE_PA_L (inDACs)      (pin 23):  0.234  V       0.359  V       0.377  V       0.671  V
PROBE_DC_R1              (pin 24):  0.924  V       0.197  V       0.292  V       0.480  V
PROBE_PA_R (inDACs)      (pin 25):  0.317  V       0.306  V       0.421  V       0.527  V
```


## Notes:

- Board G is connected but I cannot reach the SCA.
- Board E connection to SCA is established - but ROC is corrupted on one half roc and missing on the second half roc.
- all boards have `ROCv3a` (meaning DAC control is over SCA)
- Board D does not have scintillator tiles and is labeled with: `TB3_D8_v2`
- The other boards have tiles (except special tiles) and have labels containing: `TB3v3` (actually board A only says `TB3`)

-----

### LED BIAS Voltage

- LED bias voltage is reading non-zero values
- This is not intentional - the GPIOs are all held low.

-----

### No CORR factors for the ADCs

- Have not applied correction values to any of the ADCs:
    - link: https://gitlab.cern.ch/pastika/hexactrl-script/-/tree/tileboard_update?ref_type=heads#L436-453
- Correction factor is based on ADC pins 22 (PROBE_DC_L1) and 24 (PROBE_DC_R1)

-----

### Temperature methods:

**Method 1:**
- using this (without CORR for now) temperature conversion from ADC value:
```python
A_T = 3.9083e-3
B_T = -5.7750e-7
R0 = 1000
T1 = CORR*(-R0*A_T + math.sqrt(math.pow(R0*A_T, 2) - 4*R0*B_T*(R0-(1800 / ((VPA*4095/float(ADC))-1))))) / (2*R0*B_T)
```
- Found in DESY script, TB3_SlowControl_calib.py: https://gitlab.cern.ch/pastika/hexactrl-script/-/tree/tileboard_update?ref_type=heads#L466
- from notes in DESY script: for temperature correction: V_supply = V_breakdown + VinputDAC + V_offset + OV - (25 - T)*0.036

**Method 2:**
- in swamp (using "PT1000" method for ADC temps and the `else` method for internal ref temp):
```python
if method == "PT1000":
    return voltage * 736.84 - 679.89
else:
    return (voltage - 0.716) / (-1.829) * 1000
```
- from this commit 577e93ae:
    - link: https://gitlab.cern.ch/hgcal-daq-sw/swamp/-/blob/577e93ae5b10cc729dca65f51c7fc70b6c077aa7/gbtsca_analog.py#L111-128

-----

### HV bias

- Trying to provide 25V to ALDO
- 25 V is supplied to the wingboard over the most recent PFH PCB connector.
- No impact to the `MPPC_BIAS_IN` is observed.
- I could try toggling GPIO: 20 "ENHV0 (Aldo)" as Fabian does here:
    - link: https://gitlab.cern.ch/kit-ipe/hgcal-serenity-z1.1-software/slow_control/-/blob/kit-serenity/sipm_bias.py?ref_type=heads#L136
- The MPPC_BIAS_IN values are changing between 0.0124 V and 0.000 V somewhat randomly. This is independent of what is provided to the wingboard.
    - more detailed data in this link: https://gist.github.com/akgrummer/c157bfaddb6081fad5a4a654241ddb92 (before LDO gpio was enabled)








# 2024 Dec 19:


- 25 V bias supplied to wingbaord (connect to all tileboards via the same PS channel)
- GPIO and ADC status reports are found below when (1) BIAS is OFF and (2) when it is ON.
    - MPPC_BIAS_IN measures the correct values
    - MPPC_BIAS1 and MPPC_BIAS2 measure non-zero values with BIAS is turned on
- GPIO and ADC measurements for the B type baord are now included
    - 2nd roc GPIOs seem good -> pll is locked
    - MPPC_BIAS3 and MPPC_BIAS4 read non-zero values regardless of whether BIAS is applied. These use the same ADC voltage corrections as MPPC_BIAS1 and MPPC_BIAS2.


## 25V BIAS OFF

```bash
------ GPIO STATUS -------
tileboard                       A    B    D    E
PLL_LCK              (gpio 0):  1    1    1    1
ERROR                (gpio 1):  1    1    1    1
SOFT_RSTB            (gpio 2):  1    1    1    1
I2C_RSTB             (gpio 3):  1    1    1    1
HARD_RSTB            (gpio 4):  1    1    1    1
PLL_LCK_2nd_ROC      (gpio 5):  -    1    -    -
ERROR_2nd_ROC        (gpio 6):  -    1    -    -
LED_ON_OFF           (gpio 7):  0    0    0    0
LED_DISABLE1         (gpio 8):  0    0    0    0
LED_DISABLE2         (gpio 9):  0    0    0    0
LED_DISABLE3         (gpio 10): 0    0    0    0
LED_DISABLE4         (gpio 11): 0    0    0    0
LED_DISABLE5         (gpio 12): 0    0    0    0
LED_DISABLE6         (gpio 13): 0    0    0    0
LED_DISABLE7         (gpio 14): 0    0    0    0
LED_DISABLE8         (gpio 15): 0    0    0    0
LED_DISABLE1_2nd_ROC (gpio 16): -    0    -    -
LED_DISABLE2_2nd_ROC (gpio 17): -    0    -    -
ENHV0_2nd_Aldo       (gpio 18): -    0    -    -
ENHV1_2nd_Aldo       (gpio 19): -    0    -    -
ENHV0_Aldo           (gpio 20): 0    0    0    0
ENHV1_Aldo           (gpio 21): 0    0    0    0
EN_LDO_VDDD_VDDA     (gpio 22): 1    1    1    1
SOFTSTART_VDDA_VDDD  (gpio 23): 1    1    1    1
M50MV_VDDD           (gpio 24): 0    0    0    0
P50MV_VDDD           (gpio 25): 0    0    0    0
M50MV_VDDA           (gpio 26): 0    0    0    0
P50MV_VDDA           (gpio 27): 0    0    0    0
PG_LDO               (gpio 28): 1    1    1    1
OCZ_LDO              (gpio 29): 1    1    1    1
LED_DISABLE3_2nd_ROC (gpio 30): -    0    -    -
LED_DISABLE4_2nd_ROC (gpio 31): -    0    -    -
```

```bash
------ ADC STATUS -------
tileboard                             A             B             D             E
Chip Serial Num.                      28158         28012         49976         49933
PT1000 - T2 method 1      (pin 0):    36.4 C        29.2 C        31.6 C        35.8 C
PT1000 - T2 method 2      (pin 0):    34.8 C        24.2 C        27.6 C        34.1 C
PT1000 - T4 method 1      (pin 1):    36.3 C        28.6 C        29.8 C        35.5 C
PT1000 - T4 method 2      (pin 1):    35.0 C        23.5 C        24.7 C        33.6 C
PT1000 - T1 method 1      (pin 2):    36.2 C        28.0 C        30.9 C        36.2 C
PT1000 - T1 method 2      (pin 2):    33.9 C        22.6 C        26.0 C        34.6 C
PT1000 - T6 method 1      (pin 3):    34.2 C        ---           28.3 C        34.5 C
PT1000 - T6 method 2      (pin 3):    31.8 C        ---           22.8 C        32.1 C
PT1000 - T3 method 1      (pin 4):    35.6 C        28.3 C        30.2 C        35.5 C
PT1000 - T3 method 2      (pin 4):    33.7 C        22.8 C        25.6 C        33.4 C
PT1000 - T8 method 1      (pin 5):    34.8 C        27.0 C        29.1 C        34.7 C
PT1000 - T8 method 2      (pin 5):    32.5 C        20.4 C        23.7 C        32.3 C
PT1000 - T7 method 1      (pin 6):    35.1 C        28.3 C        29.2 C        34.4 C
PT1000 - T7 method 2      (pin 6):    33.0 C        22.6 C        24.4 C        31.6 C
PT1000 - T5 method 1      (pin 7):    34.7 C        ---           27.5 C        34.8 C
PT1000 - T5 method 2      (pin 7):    32.3 C        ---           21.3 C        32.3 C
Int reference temp.       (pin 31)    27.1 C        26.7 C        26.7 C        25.2 C
-----
MPPC_BIAS_IN              (pin 18):    0.0000 V      0.0000 V      0.0000 V      0.0124 V
MPPC_BIAS1                (pin 9):     0.0000 V      0.0000 V      0.0000 V      0.0000 V
MPPC_BIAS2                (pin 10):    0.0000 V      0.0000 V      0.0000 V      0.0000 V
MPPC_BIAS3                (pin 20):    ---          27.7318 V      ---           ---
MPPC_BIAS4                (pin 19):    ---          18.4049 V      ---           ---
CURHV0 (ALDO 2)           (pin 28):    ---           0.000  V      ---           ---
CURHV0 (ALDO 2): current  (pin 29):    ---           0.000  mA     ---           ---
CURHV1 (ALDO 2)           (pin 27):    ---           0.309  V      ---           ---
CURHV1 (ALDO 2): current  (pin 30):    ---           9.146  mA     ---           ---
CURHV0 (ALDO)             (pin 29):    0.000  V      0.001  V      0.000  V      0.000  V
CURHV0 (ALDO): current    (pin 29):    0.000  mA     0.029  mA     0.000  mA     0.007  mA
CURHV1 (ALDO)             (pin 30):    0.000  V      0.001  V      0.000  V      0.000  V
CURHV1 (ALDO): current    (pin 30):    0.000  mA     0.036  mA     0.000  mA     0.007  mA
VCC_IN                    (pin 11):   10.127  V     10.152  V     10.121  V     10.174  V
LED_BIAS                  (pin 12):    9.313  V      9.307  V      9.288  V      9.256  V
VPA          [+2.5V]      (pin 13):    2.547  V      2.510  V      2.521  V      2.549  V
VCC_GBTSCA                (pin 8):     1.580  V      1.590  V      1.543  V      1.580  V
PRE_VPA      [~ +3.5V]    (pin 14):    3.105  V      3.070  V      3.132  V      3.126  V
VDDA         [+1.2V]      (pin 15):    1.200  V      1.220  V      1.217  V      1.204  V
VDDD         [+1.2V]      (pin 16):    1.176  V      1.243  V      1.221  V      1.213  V
PRE_VDDA     [+1.5V]      (pin 17):    1.519  V      1.495  V      1.452  V      1.472  V
TB_ID0 [+0.2V]            (pin 26):    0.000  V      0.000  V      0.000  V      0.001  V
TB_ID1 [+0.0V]            (pin 27):    0.292  V      0.308  V      0.303  V      0.301  V
PROBE_DC_L1               (pin 22):    0.795  V      0.156  V      0.222  V      0.422  V
PROBE_PA_L (inDACs)       (pin 23):    0.234  V      0.359  V      0.376  V      0.671  V
PROBE_DC_R1               (pin 24):    0.937  V      0.197  V      0.285  V      0.482  V
PROBE_PA_R (inDACs)       (pin 25):    0.317  V      0.306  V      0.421  V      0.526  V
PROBE_PA2_R (inDACs)      (pin --):    ---           0.321  V      ---           ---
PROBE_DC_R1 2nd HGCROC    (pin --):    ---           0.144  V      ---           ---
```



## 25V BIAS ON

```bash
------ GPIO STATUS -------
tileboard                       A    B    D    E
PLL_LCK              (gpio 0):  1    1    1    1
ERROR                (gpio 1):  1    1    1    1
SOFT_RSTB            (gpio 2):  1    1    1    1
I2C_RSTB             (gpio 3):  1    1    1    1
HARD_RSTB            (gpio 4):  1    1    1    1
PLL_LCK_2nd_ROC      (gpio 5):  -    1    -    -
ERROR_2nd_ROC        (gpio 6):  -    1    -    -
LED_ON_OFF           (gpio 7):  0    0    0    0
LED_DISABLE1         (gpio 8):  0    0    0    0
LED_DISABLE2         (gpio 9):  0    0    0    0
LED_DISABLE3         (gpio 10): 0    0    0    0
LED_DISABLE4         (gpio 11): 0    0    0    0
LED_DISABLE5         (gpio 12): 0    0    0    0
LED_DISABLE6         (gpio 13): 0    0    0    0
LED_DISABLE7         (gpio 14): 0    0    0    0
LED_DISABLE8         (gpio 15): 0    0    0    0
LED_DISABLE1_2nd_ROC (gpio 16): -    0    -    -
LED_DISABLE2_2nd_ROC (gpio 17): -    0    -    -
ENHV0_2nd_Aldo       (gpio 18): -    0    -    -
ENHV1_2nd_Aldo       (gpio 19): -    0    -    -
ENHV0_Aldo           (gpio 20): 0    0    0    0
ENHV1_Aldo           (gpio 21): 0    0    0    0
EN_LDO_VDDD_VDDA     (gpio 22): 1    1    1    1
SOFTSTART_VDDA_VDDD  (gpio 23): 1    1    1    1
M50MV_VDDD           (gpio 24): 0    0    0    0
P50MV_VDDD           (gpio 25): 0    0    0    0
M50MV_VDDA           (gpio 26): 0    0    0    0
P50MV_VDDA           (gpio 27): 0    0    0    0
PG_LDO               (gpio 28): 1    1    1    1
OCZ_LDO              (gpio 29): 1    1    1    1
LED_DISABLE3_2nd_ROC (gpio 30): -    0    -    -
LED_DISABLE4_2nd_ROC (gpio 31): -    0    -    -
```

```bash
------ ADC STATUS -------
tileboard                             A             B             D             E
Chip Serial Num.                      28158         28012         49976         49933
PT1000 - T2 method 1      (pin 0):    35.9 C        29.4 C        31.6 C        35.8 C
PT1000 - T2 method 2      (pin 0):    34.5 C        24.4 C        27.8 C        34.1 C
PT1000 - T4 method 1      (pin 1):    36.4 C        29.1 C        29.7 C        35.5 C
PT1000 - T4 method 2      (pin 1):    34.8 C        23.5 C        24.9 C        33.4 C
PT1000 - T1 method 1      (pin 2):    35.9 C        28.1 C        30.9 C        36.2 C
PT1000 - T1 method 2      (pin 2):    34.3 C        22.6 C        26.4 C        34.6 C
PT1000 - T6 method 1      (pin 3):    34.1 C        ---           28.3 C        34.4 C
PT1000 - T6 method 2      (pin 3):    31.6 C        ---           22.6 C        31.9 C
PT1000 - T3 method 1      (pin 4):    35.6 C        28.3 C        30.3 C        35.7 C
PT1000 - T3 method 2      (pin 4):    33.6 C        22.4 C        25.6 C        33.4 C
PT1000 - T8 method 1      (pin 5):    34.5 C        26.7 C        29.1 C        34.5 C
PT1000 - T8 method 2      (pin 5):    32.3 C        20.6 C        23.8 C        31.9 C
PT1000 - T7 method 1      (pin 6):    35.1 C        27.9 C        29.2 C        34.5 C
PT1000 - T7 method 2      (pin 6):    32.5 C        22.1 C        24.0 C        31.4 C
PT1000 - T5 method 1      (pin 7):    34.4 C        ---           27.5 C        34.6 C
PT1000 - T5 method 2      (pin 7):    31.9 C        ---           21.5 C        32.7 C
Int reference temp.       (pin 31)    27.3 C        26.9 C        26.5 C        25.6 C
-----
MPPC_BIAS_IN              (pin 18):   24.8342 V     24.8467 V     24.8467 V     24.8591 V
MPPC_BIAS1                (pin 9):    10.3093 V     10.5704 V      9.5880 V     10.8564 V
MPPC_BIAS2                (pin 10):   10.1725 V     10.4461 V     10.5455 V     10.7196 V
MPPC_BIAS3                (pin 20):    ---          27.8437 V      ---           ---
MPPC_BIAS4                (pin 19):    ---          18.6661 V      ---           ---
CURHV0 (ALDO 2)           (pin 28):    ---           0.000  V      ---           ---
CURHV0 (ALDO 2): current  (pin 29):    ---           0.007  mA     ---           ---
CURHV1 (ALDO 2)           (pin 27):    ---           0.309  V      ---           ---
CURHV1 (ALDO 2): current  (pin 30):    ---           9.146  mA     ---           ---
CURHV0 (ALDO)             (pin 29):    0.000  V      0.001  V      0.000  V      0.000  V
CURHV0 (ALDO): current    (pin 29):    0.000  mA     0.036  mA     0.000  mA     0.000  mA
CURHV1 (ALDO)             (pin 30):    0.000  V      0.001  V      0.000  V      0.000  V
CURHV1 (ALDO): current    (pin 30):    0.000  mA     0.036  mA     0.007  mA     0.000  mA
VCC_IN                    (pin 11):   10.111  V     10.155  V     10.124  V     10.171  V
LED_BIAS                  (pin 12):    9.310  V      9.310  V      9.291  V      9.256  V
VPA          [+2.5V]      (pin 13):    2.545  V      2.510  V      2.521  V      2.549  V
VCC_GBTSCA                (pin 8):     1.579  V      1.591  V      1.543  V      1.580  V
PRE_VPA      [~ +3.5V]    (pin 14):    3.103  V      3.071  V      3.134  V      3.128  V
VDDA         [+1.2V]      (pin 15):    1.198  V      1.220  V      1.218  V      1.204  V
VDDD         [+1.2V]      (pin 16):    1.175  V      1.245  V      1.221  V      1.213  V
PRE_VDDA     [+1.5V]      (pin 17):    1.516  V      1.495  V      1.451  V      1.472  V
TB_ID0 [+0.2V]            (pin 26):    0.000  V      0.000  V      0.000  V      0.001  V
TB_ID1 [+0.0V]            (pin 27):    0.291  V      0.309  V      0.303  V      0.301  V
PROBE_DC_L1               (pin 22):    0.790  V      0.157  V      0.225  V      0.426  V
PROBE_PA_L (inDACs)       (pin 23):    0.235  V      0.360  V      0.378  V      0.673  V
PROBE_DC_R1               (pin 24):    0.931  V      0.199  V      0.284  V      0.485  V
PROBE_PA_R (inDACs)       (pin 25):    0.318  V      0.307  V      0.422  V      0.528  V
PROBE_PA2_R (inDACs)      (pin --):    ---           0.321  V      ---           ---
PROBE_DC_R1 2nd HGCROC    (pin --):    ---           0.144  V      ---           ---
```

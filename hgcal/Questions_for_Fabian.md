I've applied an input bias from the power supplies of 40 V. I'm using your `sipm_bias.py` script to apply the bias to the sipms from the ALDO. The MPPC_BIAS1 value seems to update properly (for all tileboards). Could you let me know if you think MPPC_BIAS2 and the CURHV readings are expected?

```
(swamp_env) [labc2-fnal-gov Aug11 17:45:22 slow_control]$ DBscripts biasON
python sipm_bias.py bias_voltages/TenDegree.yaml all on
-------------------------------------------------------------------------------
Tileboard TB3_A5 (SCA Spare 0, chip 0)
-------------------------------------------------------------------------------
 - Switch bias voltage on: set GPIOs
 - Switch bias voltage on: set DACs
 - Dac A value is now 200
 - Dac B value is now 100
 - Please wait for voltage stabilization (5 seconds)
 - MPPC_BIAS_IN        39.6453 V
 - MPPC_BIAS1          39.6079 V
 - MPPC_BIAS2          8.8791 V
 - CURHV0               1.000  V, current  29.630 mA
 - CURHV1               0.000  V, current  0.000 mA
 - VCC_IN               10.054  V
 - LED_BIAS             0.013  V
 - VPA (+2.5V)          2.544  V
 - VCC_GBTSCA           1.576  V
 - PRE_VPA (~ +3.5V)    3.099  V
 - VDDA (+1.2V)         1.195  V
 - VDDD (+1.2V)         1.177  V
 - PRE_VDDA (+1.5V)     1.510  V
 - TB_ID0 (+0.2V)       0.000  V
 - TB_ID1 (+0.0V)       0.292  V
 - PROBE_DC_L1 =        0.394  V
 - PROBE_DC_L2 =        0.193  V
 - PROBE_DC_R1          0.445  V
 - PROBE_DC_R2          0.277  V
-------------------------------------------------------------------------------
Tileboard TB3_B12_1 (SCA Spare 4, chip 0)
-------------------------------------------------------------------------------
 - Switch bias voltage on: set GPIOs
 - Switch bias voltage on: set DACs
 - Dac A value is now 200
 - Dac B value is now 100
 - Please wait for voltage stabilization (5 seconds)
 - MPPC_BIAS_IN        39.6079 V
 - MPPC_BIAS1          39.5706 V
 - MPPC_BIAS2          8.8170 V
 - CURHV0               1.000  V, current  29.630 mA
 - CURHV1               0.001  V, current  0.036 mA
 - VCC_IN               10.067  V
 - LED_BIAS             0.006  V
 - VPA (+2.5V)          2.503  V
 - VCC_GBTSCA           1.584  V
 - PRE_VPA (~ +3.5V)    3.053  V
 - VDDA (+1.2V)         1.212  V
 - VDDD (+1.2V)         1.238  V
 - PRE_VDDA (+1.5V)     1.485  V
 - TB_ID0 (+0.2V)       0.000  V
 - TB_ID1 (+0.0V)       0.307  V
 - PROBE_DC_L1 =        0.518  V
 - PROBE_DC_L2 =        0.321  V
 - PROBE_DC_R1          0.482  V
 - PROBE_DC_R2          0.260  V
-------------------------------------------------------------------------------
Tileboard TB3_B12_2 (SCA Spare 4, chip 1)
-------------------------------------------------------------------------------
 - Switch bias voltage on: set GPIOs
 - Switch bias voltage on: set DACs
 - Dac A value is now 200
 - Dac B value is now 100
 - Please wait for voltage stabilization (5 seconds)
 - MPPC_BIAS_IN        39.5831 V
 - MPPC_BIAS1          39.5831 V
 - MPPC_BIAS2          9.7621 V
 - CURHV0               1.000  V, current  29.630 mA
 - CURHV1               0.001  V, current  0.036 mA
 - VCC_IN               10.064  V
 - LED_BIAS             0.006  V
 - VPA (+2.5V)          2.503  V
 - VCC_GBTSCA           1.584  V
 - PRE_VPA (~ +3.5V)    3.053  V
 - VDDA (+1.2V)         1.213  V
 - VDDD (+1.2V)         1.240  V
 - PRE_VDDA (+1.5V)     1.484  V
 - TB_ID0 (+0.2V)       0.000  V
 - TB_ID1 (+0.0V)       0.307  V
 - PROBE_DC_L1 =        0.518  V
 - PROBE_DC_L2 =        0.321  V
 - PROBE_DC_R1          0.481  V
 - PROBE_DC_R2          0.260  V
-------------------------------------------------------------------------------
Tileboard TB3_D8 (SCA Spare 1, chip 0)
-------------------------------------------------------------------------------
 - Switch bias voltage on: set GPIOs
 - Switch bias voltage on: set DACs
 - Dac A value is now 197
 - Dac B value is now 100
 - Please wait for voltage stabilization (5 seconds)
 - MPPC_BIAS_IN        39.6204 V
 - MPPC_BIAS1          39.6328 V
 - MPPC_BIAS2          8.6304 V
 - CURHV0               0.512  V, current  15.159 mA
 - CURHV1               0.000  V, current  0.000 mA
 - VCC_IN               10.095  V
 - LED_BIAS             0.009  V
 - VPA (+2.5V)          2.510  V
 - VCC_GBTSCA           1.570  V
 - PRE_VPA (~ +3.5V)    3.131  V
 - VDDA (+1.2V)         1.174  V
 - VDDD (+1.2V)         1.205  V
 - PRE_VDDA (+1.5V)     1.484  V
 - TB_ID0 (+0.2V)       0.000  V
 - TB_ID1 (+0.0V)       0.299  V
 - PROBE_DC_L1 =        0.458  V
 - PROBE_DC_L2 =        0.230  V
 - PROBE_DC_R1          0.455  V
 - PROBE_DC_R2          0.279  V
-------------------------------------------------------------------------------
Tileboard TB3_E8 (SCA Spare 2, chip 0)
-------------------------------------------------------------------------------
 - Switch bias voltage on: set GPIOs
 - Switch bias voltage on: set DACs
 - Dac A value is now 205
 - Dac B value is now 100
 - Please wait for voltage stabilization (5 seconds)
 - MPPC_BIAS_IN        39.7447 V
 - MPPC_BIAS1          39.6950 V
 - MPPC_BIAS2          8.8667 V
 - CURHV0               1.000  V, current  29.630 mA
 - CURHV1               0.000  V, current  0.000 mA
 - VCC_IN               10.133  V
 - LED_BIAS             0.025  V
 - VPA (+2.5V)          2.547  V
 - VCC_GBTSCA           1.578  V
 - PRE_VPA (~ +3.5V)    3.120  V
 - VDDA (+1.2V)         1.200  V
 - VDDD (+1.2V)         1.212  V
 - PRE_VDDA (+1.5V)     1.468  V
 - TB_ID0 (+0.2V)       0.001  V
 - TB_ID1 (+0.0V)       0.301  V
 - PROBE_DC_L1 =        0.636  V
 - PROBE_DC_L2 =        0.663  V
 - PROBE_DC_R1          0.678  V
 - PROBE_DC_R2          0.514  V
-------------------------------------------------------------------------------
Tileboard TB3_G8 (SCA Spare 3, chip 0)
-------------------------------------------------------------------------------
 - Switch bias voltage on: set GPIOs
 - Switch bias voltage on: set DACs
 - Dac A value is now 190
 - Dac B value is now 100
 - Please wait for voltage stabilization (5 seconds)
 - MPPC_BIAS_IN        39.8691 V
 - MPPC_BIAS1          39.8567 V
 - MPPC_BIAS2          8.7423 V
 - CURHV0               1.000  V, current  29.630 mA
 - CURHV1               0.000  V, current  0.000 mA
 - VCC_IN               10.171  V
 - LED_BIAS             0.025  V
 - VPA (+2.5V)          2.563  V
 - VCC_GBTSCA           1.585  V
 - PRE_VPA (~ +3.5V)    3.177  V
 - VDDA (+1.2V)         1.214  V
 - VDDD (+1.2V)         1.216  V
 - PRE_VDDA (+1.5V)     1.494  V
 - TB_ID0 (+0.2V)       0.000  V
 - TB_ID1 (+0.0V)       0.301  V
 - PROBE_DC_L1 =        0.511  V
 - PROBE_DC_L2 =        0.425  V
 - PROBE_DC_R1          0.579  V
 - PROBE_DC_R2          0.343  V
```


My "TenDegree.yaml" bias config file has this content:

```
TB3_A5:
  DACA: 200
  DACB: 100
  sca: 0
  chip: 0
  emp_channel: 88
  I2C_master: 0
  ROCv3b: false
  HV_en_gpio: [20, 21]
TB3_B12_1:
  DACA: 200
  DACB: 100
  sca: 4
  chip: 0
  emp_channel: 88
  I2C_master: 0
  ROCv3b: false
  HV_en_gpio: [20, 21]
TB3_B12_2:
  DACA: 200
  DACB: 100
  sca: 4
  chip: 1
  emp_channel: 88
  I2C_master: 0
  ROCv3b: false
  HV_en_gpio: [20, 21]
TB3_D8:
  DACA: 197
  DACB: 100
  sca: 1
  chip: 0
  emp_channel: 88
  I2C_master: 0
  ROCv3b: false
  HV_en_gpio: [20, 21]
TB3_E8:
  DACA: 205
  DACB: 100
  sca: 2
  chip: 0
  emp_channel: 88
  I2C_master: 0
  ROCv3b: false
  HV_en_gpio: [20, 21]
TB3_G8:
  DACA: 190
  DACB: 100
  sca: 3
  chip: 0
  emp_channel: 88
  I2C_master: 0
  ROCv3b: false
  HV_en_gpio: [20, 21]
```


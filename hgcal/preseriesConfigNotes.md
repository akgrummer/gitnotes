
for Partial module
bcr is being interpreted as cal_pulse_int_fcmd_count
so fc are not interpreted well
3 of 6 and 6 of 12 erX phase settings are 0xF
all snapshots are 0 on the partial

- should try Cristina's partial config is it here?:
https://gitlab.cern.ch/agrummer/cass-sw/-/blob/partials/configs/econd_init_cpp.yaml?ref_type=heads

FCtrl:
  Global:
    invert_command_rx: 0x0
    command_rx_inverted: 0x0
    locked: 0x1
    lock_count: 0x1
    bcr_fcmd_count: 0xE1
    ocr_fcmd_count: 0x0
    l1a_fcmd_count: 0x65
    nzs_fcmd_count: 0x6E
    cal_pulse_int_fcmd_count: 0x9D
    cal_pulse_ext_fcmd_count: 0x2
    ebr_fcmd_count: 0x0
    ecr_fcmd_count: 0x0
    link_reset_roc_t_fcmd_count: 0x0
    link_reset_roc_d_fcmd_count: 0x0
    link_reset_econ_t_fcmd_count: 0x0
    link_reset_econ_d_fcmd_count: 0x0
    fc_error_fcmd_count: 0xD
    tmr_err_cnt_fast_ctrl_decoder: 0x0




number of roc EBOs that have to agree
greater than the value (not greater than or equal to)
v_reconstruct_thresh

HD:
TPG should have HD format
sum by 9 channels instead of 4:
SelTC4: 0


preemphasis resistors

on pCM for partials

Guillaume Soudais from Saclay
based on wave form he can assess

input at Rafael or


HD wagon - preemphesis resistors were everywhere
creating problems - but not everywhere.
some sites of the wagon
link alignment issues Roc to econ for some wagon sites - removed premphasis


HD wagon for 3 HD full 4 rafaels
econt without rafael




# LD5



0101 0000000000000000
0001 00000000b9999807
0001 0000000066667f84
0001 0000000000000000
0001 0000000066667f84
0001 000000008ccccff0
0001 00000000ffffffff
0000 00000000ffffffff


# relay:
78 was good with uncovered light all bias

relay:
run, module covered from light
79: HD m3 301
80: HD m2 302
81: HD m1 303
82: LD3 e3 322
83: LD3 e2 323
84: LD3 e1 324
85: LD3 w1 312
86: LD3 w2 326
87: LD3 w3 327
88: LD4 e2 329
89: LD4 e1 330
90: LD4 w1 331
91: LD4 w2 311
92: LD4 w3 333
93: LD5 e2 335
94: LD5 e1 336
95: LD5 w1 337
96: LD5 w2 338

97: totally covered
98: two papers
99: poster covered at an angle



30000079

103: LD1 e3 322
104: LD1 e2 323
105: LD1 e1 324
106: LD1 w1 312
107: LD1 w2 326
108: LD1 w3 327
109: LD2 e3 329
110: LD2 e2 329
111: LD2 e1 330
112: LD2 w1 331
113: LD2 w2 311


## tiles

25 V from PS
Dboard - 14 mA current draw from CURHV reading
PS reading 8 mA
outputMeasurementCurrent.u104 = Opaque: Float: 0.008118 A

43.8 V from PS
no Dboard:
from PS:
outputMeasurementCurrent.u104 = Opaque: Float: 0.014954 A
4 modules at ~0.4mA


with D board included:
outputMeasurementCurrent.u104 = Opaque: Float: 0.016418 A

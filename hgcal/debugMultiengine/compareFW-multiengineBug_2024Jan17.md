# pre-refactored fw (with cosmic trig)
* I beleive this version was edited off of the February commit `4c92238` - could be double checked though
* uses two hgc-engine-tools sw git branches: `V3_aidan` and `engineSetup_FNAL_aidan_retrace`
* uses swamp sw branch: `fnal_cassettes`

configure with zcu_multitool.py to setup clocks successfully...

then input at command line is:

```bash
# from hgc-engine-tools dir:

./enableEngine.sh
./lpgbt_status.py --mode V3_ALL -t DAQ --dumpPUSM
./lpgbt_status.py --mode V3_ALL -t E --dumpPUSM
./lpgbt_status.py --mode V3_ALL -t W --dumpPUSM

# from SWAMP directory:

./enableSwamp.sh 
python lpgbt_control.py -t daq -rw read -reg PUSMSTATUS
python lpgbt_control.py -t trg_e -rw read -reg PUSMSTATUS
python lpgbt_control.py -t trg_w -rw read -reg PUSMSTATUS
```


Output:
```bash
[agrummer@zcufnal (hgc-engine-tools)]$ pwd
/home/agrummer/hgc-engine-tools
[agrummer@zcufnal (hgc-engine-tools)]$ ./enableEngine.sh
IC_SOURCE: 0
EC_SOURCE: 0
[agrummer@zcufnal (hgc-engine-tools)]$ ./lpgbt_status.py --mode V3_ALL -t DAQ --dumpPUSM
PUSMstatus(0x1d9): 0x13
[agrummer@zcufnal (hgc-engine-tools)]$ ./lpgbt_status.py --mode V3_ALL -t E --dumpPUSM
PUSMstatus(0x1d9): 0x13
[agrummer@zcufnal (hgc-engine-tools)]$ ./lpgbt_status.py --mode V3_ALL -t W --dumpPUSM
PUSMstatus(0x1d9): 0x13
[agrummer@zcufnal (hgc-engine-tools)]$ cd /home/agrummer/daq/slow_control/swamp
[agrummer@zcufnal (swamp)]$ ./enableSwamp.sh 
IC_SOURCE: 1
EC_SOURCE: 1
[agrummer@zcufnal (swamp)]$ python lpgbt_control.py -t daq -rw read -reg PUSMSTATUS
Namespace(lpgbt_target='daq', read_write='read', config=None, reg='PUSMSTATUS', val=None, protocol='sct', ic_emp_channel=13)
['TOP']
2024-01-17 13:15:48,140 - lpgbt - INFO - read with config = {'PUSMSTATUS': None} (sc_lpgbt.py:107)
2024-01-17 13:15:48,145 - lpgbt - INFO - sc_lpgbt.read done (sc_lpgbt.py:116)
PUSMSTATUS               :  0x13
[agrummer@zcufnal (swamp)]$ python lpgbt_control.py -t trg_e -rw read -reg PUSMSTATUS
Namespace(lpgbt_target='trg_e', read_write='read', config=None, reg='PUSMSTATUS', val=None, protocol='sct', ic_emp_channel=13)
['TOP']
2024-01-17 13:15:53,442 - lpgbt - INFO - read with config = {'PUSMSTATUS': None} (sc_lpgbt.py:107)
2024-01-17 13:15:53,446 - lpgbt - INFO - sc_lpgbt.read done (sc_lpgbt.py:116)
PUSMSTATUS               :  0x13
[agrummer@zcufnal (swamp)]$ python lpgbt_control.py -t trg_w -rw read -reg PUSMSTATUS
Namespace(lpgbt_target='trg_w', read_write='read', config=None, reg='PUSMSTATUS', val=None, protocol='sct', ic_emp_channel=13)
['TOP']
2024-01-17 13:15:58,718 - lpgbt - INFO - read with config = {'PUSMSTATUS': None} (sc_lpgbt.py:107)
2024-01-17 13:15:58,723 - lpgbt - INFO - sc_lpgbt.read done (sc_lpgbt.py:116)
PUSMSTATUS               :  0x13
```


# multi-engine FW
* fw name: eight-engine `eight-engine-feature_eight_engine-2023_12_15_21_19_40.701aaa75`
* uses sw hgc-engine tools branch: `danny_dev_backend_refactor_multiEngine`
* swamp sw branch: `fnal_cassettes_multiEngine`

following same command line instructions as above.

**Different PUSMSTATUS output for SWAMP**

only difference in swamp sw branches are the uhal node names:
see `sc_transactor_interface.py ` [here](https://gitlab.cern.ch/agrummer/swamp/-/compare/fnal_cassettes...fnal_cassettes_multiEngine?from_project_id=177229&straight=true)


Output:
```bash
[agrummer@zcufnal (hgc-engine-tools)]$ pwd
/home/agrummer/hgc-engine-tools
[agrummer@zcufnal (hgc-engine-tools)]$ ./enableEngine.sh
IC_SOURCE: 0
EC_SOURCE: 0
[agrummer@zcufnal (hgc-engine-tools)]$ ./lpgbt_status.py --mode V3_ALL -t DAQ --dumpPUSM
PUSMstatus(0x1d9): 0x13
[agrummer@zcufnal (hgc-engine-tools)]$ ./lpgbt_status.py --mode V3_ALL -t E --dumpPUSM
PUSMstatus(0x1d9): 0x13
[agrummer@zcufnal (hgc-engine-tools)]$ ./lpgbt_status.py --mode V3_ALL -t W --dumpPUSM
PUSMstatus(0x1d9): 0x13
[agrummer@zcufnal (hgc-engine-tools)]$ 
[agrummer@zcufnal (hgc-engine-tools)]$ 
[agrummer@zcufnal (hgc-engine-tools)]$ 
[agrummer@zcufnal (hgc-engine-tools)]$ cd /home/agrummer/daq/slow_control/swamp
[agrummer@zcufnal (swamp)]$ ./enableSwamp.sh 
IC_SOURCE: 1
EC_SOURCE: 1
[agrummer@zcufnal (swamp)]$ python lpgbt_control.py -t daq -rw read -reg PUSMSTATUS
Namespace(lpgbt_target='daq', read_write='read', config=None, reg='PUSMSTATUS', val=None, protocol='sct', ic_emp_channel=13)
['TOP']
2024-01-17 13:40:07,199 - lpgbt - INFO - read with config = {'PUSMSTATUS': None} (sc_lpgbt.py:107)
2024-01-17 13:40:07,203 - lpgbt - INFO - sc_lpgbt.read done (sc_lpgbt.py:116)
PUSMSTATUS               :  0x0
[agrummer@zcufnal (swamp)]$ python lpgbt_control.py -t trg_e -rw read -reg PUSMSTATUS
Namespace(lpgbt_target='trg_e', read_write='read', config=None, reg='PUSMSTATUS', val=None, protocol='sct', ic_emp_channel=13)
['TOP']
2024-01-17 13:40:19,866 - lpgbt - INFO - read with config = {'PUSMSTATUS': None} (sc_lpgbt.py:107)
2024-01-17 13:40:19,870 - lpgbt - INFO - sc_lpgbt.read done (sc_lpgbt.py:116)
PUSMSTATUS               :  0x0
[agrummer@zcufnal (swamp)]$ python lpgbt_control.py -t trg_w -rw read -reg PUSMSTATUS
Namespace(lpgbt_target='trg_w', read_write='read', config=None, reg='PUSMSTATUS', val=None, protocol='sct', ic_emp_channel=13)
['TOP']
2024-01-17 13:40:26,366 - lpgbt - INFO - read with config = {'PUSMSTATUS': None} (sc_lpgbt.py:107)
2024-01-17 13:40:26,370 - lpgbt - INFO - sc_lpgbt.read done (sc_lpgbt.py:116)
PUSMSTATUS               :  0x0
```

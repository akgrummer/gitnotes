on Hexaboard fw interposer-ROCv2:
link reset counter doesn't increase
./uhal_string.py -b Housekeeping-FastControl-fastcontrol-v2-decod-0 --node link_reset_count
also l1a count doesn't increase from 0
./uhal_string.py -b Housekeeping-FastControl-fastcontrol-v2-decod-0 --node l1a_count

error counter is continually increasing
./uhal_string.py -b Housekeeping-FastControl-fastcontrol-v2-decod-0 --node err_count

L1A counter ZCU fw version zcu102-siengine-v1p0-ROCv2:
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --node counters.internal_test
counters.internal_test: 4
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --node command.l1a_A
command.l1a_A: 0
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --node command.l1a_A --val 1
command.l1a_A: 0
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --node counters.internal_test
counters.internal_test: 5
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --node counters.l1a
counters.l1a: 0

Also true on ZCU fw version zcu102-siengine-v1p0
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --node counters.internal_test
counters.internal_test: 1
[agrummer@fnal-zcu102-a uhal101]$  ./uhal_string.py -b fastcontrol-axi-0 --node command.l1a_A
command.l1a_A: 0
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --node command.l1a_A --val 1
command.l1a_A: 0
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --node counters.internal_test
counters.internal_test: 2
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --ls
[agrummer@fnal-zcu102-a uhal101]$ ./uhal_string.py -b fastcontrol-axi-0 --node counters.l1a
counters.l1a: 0

counters on ZCU fw version zcu102-siengine-v1p0-ROCv2
./uhal_string.py -b fastcontrol-axi-0 --node counters.errors
./uhal_string.py -b fastcontrol-axi-0 --node counters.orbit_sync
./uhal_string.py -b fastcontrol-axi-0 --node counters.orbit_count_reset
./uhal_string.py -b fastcontrol-axi-0 --node counters.calibration_request
./uhal_string.py -b fastcontrol-axi-0 --node counters.calibration_l1a
./uhal_string.py -b fastcontrol-axi-0 --node counters.link_reset
./uhal_string.py -b fastcontrol-axi-0 --node counters.daq_sync
./uhal_string.py -b fastcontrol-axi-0 --node counters.roc_dump
./uhal_string.py -b fastcontrol-axi-0 --node counters.internal_test

Which clk on Hexaboard
./uhal_string.py -b Housekeeping-FastControl-FC-control --node clk_int_select
./uhal_string.py -b Housekeeping-FastControl-FC-control --node FC_int_select
./uhal_string.py -b Housekeeping-FastControl-FC-control --node ext_clk_active



fast commands seem to work on hexaboard with new firware now - after the debugging, something seemed to lock it
Current status:
	- zcu is using zcu102-siengine-v1p0 fw
	- using milos2/hgc-engine-tools
	- using interposer-ROCv2


./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node global.global_reset_counters --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node global.global_latch_counters --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.error_counter
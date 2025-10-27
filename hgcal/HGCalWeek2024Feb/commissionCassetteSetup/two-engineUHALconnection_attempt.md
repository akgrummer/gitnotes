```bash
[HGCAL_dev@hgczcu102-mbv3 (hgc-engine-tools)]$ sudo fw-loader load two-engine
[sudo] password for HGCAL_dev:
Previously loaded firmware: /opt/cms-hgcal-firmware/hgc-test-systems/unicorn
Using bitstream: /opt/cms-hgcal-firmware/hgc-test-systems/two-engine/two-engine.bit
Using device tree overlay: /opt/cms-hgcal-firmware/hgc-test-systems/two-engine/device-tree/pl.dtbo
Loading the bitstream took: 12.827s
Loaded the device tree overlay successfully using the zynqMP FPGA manager
[HGCAL_dev@hgczcu102-mbv3 (hgc-engine-tools)]$
[HGCAL_dev@hgczcu102-mbv3 (hgc-engine-tools)]$
[HGCAL_dev@hgczcu102-mbv3 (hgc-engine-tools)]$
[HGCAL_dev@hgczcu102-mbv3 (hgc-engine-tools)]$ python
Python 3.9.18 (main, Feb 19 2024, 08:26:16)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import uhal
>>> uhal.setLogLevelTo( uhal.LogLevel.NOTICE )
>>> uhal.ConnectionManager("file:///opt/cms-hgcal-firmware/hgc-test-systems/active/uHAL_xml/connections.xml").getDevice("TOP")
21-02-24 06:03:44.088963 [281473029271552] NOTICE - Node "contents" has type "NON_INCREMENTAL" but does not have a "size" attribute. This is not necessarily a problem, but if there is a limit to the size of the read/write operation from this port, then please consider adding this attribute for the sake of safety.
21-02-24 06:03:44.094024 [281473029271552] NOTICE - Node "" has type "NON_INCREMENTAL" but does not have a "size" attribute. This is not necessarily a problem, but if there is a limit to the size of the read/write operation from this port, then please consider adding this attribute for the sake of safety.
21-02-24 06:03:44.097159 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-0-DAQ-capture-DAQ-link-capture_global.xml.txt"
21-02-24 06:03:44.103009 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-0-DAQ-capture-DAQ-link-capture.xml.txt"
21-02-24 06:03:44.108715 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-0-LD-0.xml.txt"
21-02-24 06:03:44.113947 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-0-trig-capture-trig-link-capture_global.xml.txt"
21-02-24 06:03:44.120976 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-0-trig-capture-trig-link-capture.xml.txt"
21-02-24 06:03:44.127788 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-1-DAQ-capture-DAQ-link-capture_global.xml.txt"
21-02-24 06:03:44.131608 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-1-DAQ-capture-DAQ-link-capture.xml.txt"
21-02-24 06:03:44.137339 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-1-LD-0.xml.txt"
21-02-24 06:03:44.142573 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-1-trig-capture-trig-link-capture_global.xml.txt"
21-02-24 06:03:44.149519 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-engines-engine-1-trig-capture-trig-link-capture.xml.txt"
21-02-24 06:03:44.162474 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-transceivers-transceiver-left-0.xml.txt"
21-02-24 06:03:44.167844 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-transceivers-transceiver-right-0.xml.txt"
21-02-24 06:03:44.175511 [281473029271552] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-fw_block_addresses.xml.txt"
21-02-24 06:03:44.299014 [281473029271552] NOTICE - list of nodes Housekeeping-FastCommands-fastcontrol-axi-0
21-02-24 06:03:44.299111 [281473029271552] NOTICE - list of nodes Housekeeping-FastCommands-fastcontrol-recv-axi-0
21-02-24 06:03:44.299140 [281473029271552] NOTICE - list of nodes engines-engine-0-DAQ-capture-DAQ-link-capture
21-02-24 06:03:44.299167 [281473029271552] NOTICE - list of nodes engines-engine-0-DAQ-capture-DAQ-link-capture_FIFO
21-02-24 06:03:44.299194 [281473029271552] NOTICE - list of nodes engines-engine-0-LD-0
21-02-24 06:03:44.299219 [281473029271552] NOTICE - list of nodes engines-engine-0-trig-capture-trig-link-capture
21-02-24 06:03:44.299245 [281473029271552] NOTICE - list of nodes engines-engine-0-trig-capture-trig-link-capture_FIFO
21-02-24 06:03:44.299271 [281473029271552] NOTICE - list of nodes engines-engine-1-DAQ-capture-DAQ-link-capture
21-02-24 06:03:44.299294 [281473029271552] NOTICE - list of nodes engines-engine-1-DAQ-capture-DAQ-link-capture_FIFO
21-02-24 06:03:44.299318 [281473029271552] NOTICE - list of nodes engines-engine-1-LD-0
21-02-24 06:03:44.299352 [281473029271552] NOTICE - list of nodes engines-engine-1-trig-capture-trig-link-capture
21-02-24 06:03:44.299379 [281473029271552] NOTICE - list of nodes engines-engine-1-trig-capture-trig-link-capture_FIFO
21-02-24 06:03:44.299406 [281473029271552] NOTICE - list of nodes slow-control-Slow-Control-0_config
21-02-24 06:03:44.299432 [281473029271552] NOTICE - list of nodes slow-control-Slow-Control-0_data
21-02-24 06:03:44.299457 [281473029271552] NOTICE - list of nodes transceivers-transceiver-left-0
21-02-24 06:03:44.299482 [281473029271552] NOTICE - list of nodes transceivers-transceiver-right-0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: Is a directory
>>>
```

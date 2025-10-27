```bash
[HGCAL_dev@hgczcu102-mbv3 (hgc-engine-tools)]$ sudo fw-loader load unicorn
Previously loaded firmware: /opt/cms-hgcal-firmware/hgc-test-systems/two-engine
Using bitstream: /opt/cms-hgcal-firmware/hgc-test-systems/unicorn/unicorn.bit
Using device tree overlay: /opt/cms-hgcal-firmware/hgc-test-systems/unicorn/device-tree/pl.dtbo
Loading the bitstream took: 12.901s
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
21-02-24 05:56:54.079101 [281472906739712] NOTICE - Node "" has type "NON_INCREMENTAL" but does not have a "size" attribute. This is not necessarily a problem, but if there is a limit to the size of the read/write operation from this port, then please consider adding this attribute for the sake of safety.
21-02-24 05:56:54.084722 [281472906739712] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-ECON-D-ECOND-input-link-capture-AXI-0_global.xml.txt"
21-02-24 05:56:54.088964 [281472906739712] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-ECON-D-ECOND-input-link-capture-AXI-0.xml.txt"
21-02-24 05:56:54.094083 [281472906739712] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-ECON-D-ECOND-output-link-capture-AXI-0_global.xml.txt"
21-02-24 05:56:54.096800 [281472906739712] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-ECON-D-ECOND-output-link-capture-AXI-0.xml.txt"
21-02-24 05:56:54.107861 [281472906739712] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-ECON-T-ECONT-input-link-capture-AXI-0_global.xml.txt"
21-02-24 05:56:54.112703 [281472906739712] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-ECON-T-ECONT-input-link-capture-AXI-0.xml.txt"
21-02-24 05:56:54.121375 [281472906739712] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-ECON-T-ECONT-output-link-capture-AXI-0_global.xml.txt"
21-02-24 05:56:54.126561 [281472906739712] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-modules-ECON-T-ECONT-output-link-capture-AXI-0.xml.txt"
21-02-24 05:56:54.132542 [281472906739712] NOTICE - Node "contents" has type "NON_INCREMENTAL" but does not have a "size" attribute. This is not necessarily a problem, but if there is a limit to the size of the read/write operation from this port, then please consider adding this attribute for the sake of safety.
21-02-24 05:56:54.140584 [281472906739712] WARNING - Address overlaps observed - report file written at "/tmp/HGCAL_dev/uhal/OverlapReport-opt-cms-hgcal-firmware-hgc-test-systems-active-uHAL_xml-fw_block_addresses.xml.txt"
21-02-24 05:56:54.230623 [281472906739712] NOTICE - list of nodes ECON-D-ECOND-emulator-ECOND-support-0
21-02-24 05:56:54.230719 [281472906739712] NOTICE - list of nodes ECON-D-ECOND-input-IO-blocks-0
21-02-24 05:56:54.230747 [281472906739712] NOTICE - list of nodes ECON-D-ECOND-input-link-capture-AXI-0
21-02-24 05:56:54.230774 [281472906739712] NOTICE - list of nodes ECON-D-ECOND-input-link-capture-AXI-0_FIFO
21-02-24 05:56:54.230801 [281472906739712] NOTICE - list of nodes ECON-D-ECOND-output-IO-blocks-1
21-02-24 05:56:54.230827 [281472906739712] NOTICE - list of nodes ECON-D-ECOND-output-link-capture-AXI-0
21-02-24 05:56:54.230852 [281472906739712] NOTICE - list of nodes ECON-D-ECOND-output-link-capture-AXI-0_FIFO
21-02-24 05:56:54.230878 [281472906739712] NOTICE - list of nodes ECON-D-fast-commands-clk-FC-mux-0
21-02-24 05:56:54.230904 [281472906739712] NOTICE - list of nodes ECON-D-fast-commands-fastcontrol-recv-axi-0
21-02-24 05:56:54.230929 [281472906739712] NOTICE - list of nodes ECON-T-ECONT-emulator-ECONT-support-0
21-02-24 05:56:54.230955 [281472906739712] NOTICE - list of nodes ECON-T-ECONT-input-IO-blocks-0
21-02-24 05:56:54.230980 [281472906739712] NOTICE - list of nodes ECON-T-ECONT-input-link-capture-AXI-0
21-02-24 05:56:54.231005 [281472906739712] NOTICE - list of nodes ECON-T-ECONT-input-link-capture-AXI-0_FIFO
21-02-24 05:56:54.231031 [281472906739712] NOTICE - list of nodes ECON-T-ECONT-output-IO-blocks-1
21-02-24 05:56:54.231056 [281472906739712] NOTICE - list of nodes ECON-T-ECONT-output-link-capture-AXI-0
21-02-24 05:56:54.231082 [281472906739712] NOTICE - list of nodes ECON-T-ECONT-output-link-capture-AXI-0_FIFO
21-02-24 05:56:54.231107 [281472906739712] NOTICE - list of nodes ECON-T-fast-commands-clk-FC-mux-0
21-02-24 05:56:54.231132 [281472906739712] NOTICE - list of nodes ECON-T-fast-commands-fastcontrol-recv-axi-0
21-02-24 05:56:54.231157 [281472906739712] NOTICE - list of nodes Housekeeping-fast-commands-fastcontrol-axi-0
21-02-24 05:56:54.231183 [281472906739712] NOTICE - list of nodes I2C-I2C-interconnect-0
<uhal._core.HwInterface object at 0xffff7dfc62b0>
>>>
```

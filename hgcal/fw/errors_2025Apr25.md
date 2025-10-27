
1. gen xml step:

The following decoders have changed and must be updated:
 - ipbus_decode_tcds2_relay_ipbus_accessor.vhd
 - ipbus_decode_tcds2_interface_ipbus_accessor_hw_cfg.vhd
 - ipbus_decode_tcds2_interface_ipbus_accessor.vhd


2. implementation step:

[...]

impl | INFO: [Netlist 29-17] Analyzing 13290 Unisim elements for replacement
impl | INFO: [Netlist 29-28] Unisim Transformation completed in 0 CPU seconds
impl | INFO: [Project 1-479] Netlist was created with Vivado 2022.2
impl | INFO: [Project 1-570] Preparing netlist for logic optimization
impl | Parsing XDC File [/home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/xdma_0/ip_0/source/ip_pcie4_uscale_plus_impl_x1y2.xdc] for cell 'infra/dma/xdma/inst/pcie4_ip_i/inst'
impl | Finished Parsing XDC File [/home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/xdma_0/ip_0/source/ip_pcie4_uscale_plus_impl_x1y2.xdc] for cell 'infra/dma/xdma/inst/pcie4_ip_i/inst'
impl | CRITICAL WARNING: [Designutils 20-1280] Could not find module 'SlinkRocket_SERDES_15G66_GTY'. The XDC file /home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/SR_core_master/sources_1/ip/SlinkRocket_SERDES_15G66_GTY/synth/SlinkRocket_SERDES_15G66_GTY.xdc will not be read for any cell of this module.
impl | CRITICAL WARNING: [Designutils 20-1280] Could not find module 'SlinkRocket_SERDES_25G78125_GTY'. The XDC file /home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/SR_core_master/sources_1/ip/SlinkRocket_SERDES_25G78125_GTY/synth/SlinkRocket_SERDES_25G78125_GTY.xdc will not be read for any cell of this module.
impl | CRITICAL WARNING: [Designutils 20-1280] Could not find module 'SR_core_master'. The XDC file /home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/SR_core_master/constrs_1/imports/gitreps/slinkrocket/SLINK_sender/SR_sender.xdc will not be read for any cell of this module.
impl | CRITICAL WARNING: [Designutils 20-1280] Could not find module 'SR_core_master'. The XDC file /home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/SR_core_master/constrs_1/imports/gitreps/fpga_library/resync/resetn_resync.xdc will not be read for any cell of this module.
impl | CRITICAL WARNING: [Designutils 20-1280] Could not find module 'SR_core_master'. The XDC file /home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/SR_core_master/constrs_1/imports/gitreps/fpga_library/resync/resetp_resync.xdc will not be read for any cell of this module.
impl | CRITICAL WARNING: [Designutils 20-1280] Could not find module 'SR_core_master'. The XDC file /home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/SR_core_master/constrs_1/imports/gitreps/fpga_library/resync/resync_pulse.xdc will not be read for any cell of this module.
impl | CRITICAL WARNING: [Designutils 20-1280] Could not find module 'SR_core_master'. The XDC file /home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/SR_core_master/constrs_1/imports/gitreps/fpga_library/resync/resync_pulse_ena.xdc will not be read for any cell of this module.
impl | CRITICAL WARNING: [Designutils 20-1280] Could not find module 'SR_core_master'. The XDC file /home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/SR_core_master/constrs_1/imports/gitreps/fpga_library/resync/resync_sig_gen.xdc will not be read for any cell of this module.
impl | Parsing XDC File [/home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/xdma_0/ip_0/ip_0/synth/xdma_0_pcie4_ip_gt.xdc] for cell 'infra/dma/xdma/inst/pcie4_ip_i/inst/xdma_0_pcie4_ip_gt_top_i/diablo_gt.diablo_gt_phy_wrapper/gt_wizard.gtwizard_top_i/xdma_0_pcie4_ip_gt_i/inst'
impl | Finished Parsing XDC File [/home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/xdma_0/ip_0/ip_0/synth/xdma_0_pcie4_ip_gt.xdc] for cell 'infra/dma/xdma/inst/pcie4_ip_i/inst/xdma_0_pcie4_ip_gt_top_i/diablo_gt.diablo_gt_phy_wrapper/gt_wizard.gtwizard_top_i/xdma_0_pcie4_ip_gt_i/inst'
impl | CRITICAL WARNING: [Designutils 20-1280] Could not find module 'SR_FIFO_sender'. The XDC file /home/agrummer/fw/raghu_2025Apr11/hgc_work_area2/proj/hgcal_hybrid/hgcal_hybrid/hgcal_hybrid.gen/sources_1/ip/SR_core_master/sources_1/ip/SR_FIFO_sender/SR_FIFO_sender.xdc will not be read for any cell of this module.

[...]

impl | [Tue Apr 22 16:11:00 2025] impl_1 finished
impl | WARNING: [Vivado 12-13638] Failed runs(s) : 'impl_1'
impl | wait_on_runs: Time (s): cpu = 00:32:08 ; elapsed = 00:16:21 . Memory (MB): peak = 2249.945 ; gain = 0.000 ; free physical = 56664 ; free virtual = 93050
impl | impl_1
[16:11:00] hgcal_hybrid: Implementation completed successfully.


3. Package Step:

bitfile | Vivado% open_run impl_1
bitfile | open_run impl_1
bitfile | ERROR: [Common 17-69] Command failed: Run 'impl_1' failed. Unable to open
[16:40:10] Vivado error/critical warnings detected                                                                         utils.py:250
           ERROR: [Common 17-69] Command failed: Run 'impl_1' failed. Unable to open                                       utils.py:251
                                                                                                                           utils.py:252
Aborted!
bitfile | Vivado% quit
bitfile | quit
bitfile | INFO: [Common 17-206] Exiting Vivado at Tue Apr 22 16:40:10 2025...
bitfile | - Terminating Vivado (pid 131665) -----------------------------------------


# motherboards 2025 Apr 9

Received 2 motherboards on Apr 8
Econ D prod (2024/18)
2 Econ T prod (2024/18)
2 lpgbt v1
R607: open
R608: open
R609: 0 ohm
J2: empty?
2 additional screw holes
one screw hole further inset

motherbaord v1
3 lpgbt v1
2 Econ T (2021 V1)
R607: 0 ohm
R608: 0 ohm
R609: open
Efuse: empty?

New cutouts needed in kapton for
- 2 new screw stand offs
- new location for screw hole

there is an additional screw hole for motherboard to copper plate on the vtrx end

* VTRX doesn't seem to cover the screw hole stand off

using pentagon shaped screws

not flush with copper plate

connection between motherboard and wingboard v1.5.2 is still not tight when not using copper plate

vtrx screws are tricky to get it. Must be placed in after motherboard and wingboard are in place. Screw is easily trapped in the copper slot where one side is now completely covered by motherboard pcb.


```bash
python gpio_control.py -rw write -p emp -d vcu118 -c 84 -t daq -pins 14 -dir output -o up
python gpio_control.py -rw read -p emp -d vcu118 -c 84 -t daq -pins 14 -dir output
python lpgbt_control.py -t trg_w -rw read -f ../../swamp-cpp/test/config/lpgbt_status.yaml -p emp -c 84 -d vcu118


python econ_control.py -s w0 -b 0 -a 0x61 -rw read -p emp -c 84 -d vcu118 -f configs/econd_status.yaml
python econ_control.py -s w0 -b 1 -a 0x20 -rw read -p emp -c 84 -d vcu118 -f configs/econt_status.yaml
python econ_control.py -s w0 -b 2 -a 0x20 -rw read -p emp -c 84 -d vcu118 -f configs/econt_status.yaml




##  using lpgbt_test_write.py to test the motherboard error rate


from lpgbt manual: Both the up and downlinks use Forward Error Correction (FEC) to detect
https://lpgbt.web.cern.ch/lpgbt/v1/highSpeedLinks.html#downlink-frame




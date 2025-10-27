config outputs.yaml
lpgbt_control -F /root/config_generator/hwcfg_fnal_10deg_sil.yaml -L 3 -l daq -f  ./configs/daq_lpgbt/outputs.yaml -r 0 -c 1
2025-05-19 14:52:53.092 [info] provided configuration =
EPTX00CHNCNTR: 7
EPTX01CHNCNTR: 7
EPTX01_00CHNCNTR: 136
EPTX02CHNCNTR: 7
EPTX03CHNCNTR: 7
EPTX03_02CHNCNTR: 128
EPTX10CHNCNTR: 7
EPTX10ENABLE: 7
EPTX11CHNCNTR: 7
EPTX11_10CHNCNTR: 136
EPTX12CHNCNTR: 7
EPTX13CHNCNTR: 7
EPTX13_12CHNCNTR: 0
EPTX20CHNCNTR: 7
EPTX21CHNCNTR: 7
EPTX21_20CHNCNTR: 0
EPTX22CHNCNTR: 7
EPTX23CHNCNTR: 7
EPTX23_22CHNCNTR: 136
EPTX30CHNCNTR: 7
EPTX31CHNCNTR: 7
EPTX31_30CHNCNTR: 136
EPTX32CHNCNTR: 7
EPTX32ENABLE: 43
EPTX33CHNCNTR: 7
EPTX33_32CHNCNTR: 136
EPTXCONTROL: 13
EPTXDATARATE: 243
2025-05-19 14:52:53.093 [info] read back configuration =
EPTX00CHNCNTR: 7
EPTX01CHNCNTR: 7
EPTX02CHNCNTR: 0
EPTX03CHNCNTR: 0
EPTX10CHNCNTR: 7
EPTX11CHNCNTR: 0
EPTX12CHNCNTR: 0
EPTX13CHNCNTR: 0
EPTX20CHNCNTR: 7
EPTX21CHNCNTR: 7
EPTX22CHNCNTR: 0
EPTX23CHNCNTR: 0
EPTX30CHNCNTR: 7
EPTX31CHNCNTR: 7
EPTX32CHNCNTR: 0
EPTX33CHNCNTR: 0
EPTX01_00CHNCNTR: 0
EPTX03_02CHNCNTR: 0
EPTX11_10CHNCNTR: 0
EPTX13_12CHNCNTR: 0
EPTX21_20CHNCNTR: 7
EPTX23_22CHNCNTR: 7
EPTX31_30CHNCNTR: 0
EPTX33_32CHNCNTR: 0
EPTXDATARATE: 243
EPTXCONTROL: 13
EPTX10ENABLE: 7
EPTX32ENABLE: 43
2025-05-19 14:52:53.093 [info] ********Config Differences**************
2025-05-19 14:52:53.093 [info] Register                            | Expected     | Read Back
2025-05-19 14:52:53.093 [info] -----                               | -----        | -----
2025-05-19 14:52:53.093 [info] EPTX02CHNCNTR                       | 0x0          | 0x7
2025-05-19 14:52:53.093 [info] EPTX03CHNCNTR                       | 0x0          | 0x7
2025-05-19 14:52:53.093 [info] EPTX11CHNCNTR                       | 0x0          | 0x7
2025-05-19 14:52:53.093 [info] EPTX12CHNCNTR                       | 0x0          | 0x7
2025-05-19 14:52:53.093 [info] EPTX13CHNCNTR                       | 0x0          | 0x7
2025-05-19 14:52:53.093 [info] EPTX22CHNCNTR                       | 0x0          | 0x7
2025-05-19 14:52:53.093 [info] EPTX23CHNCNTR                       | 0x0          | 0x7
2025-05-19 14:52:53.093 [info] EPTX32CHNCNTR                       | 0x0          | 0x7
2025-05-19 14:52:53.093 [info] EPTX33CHNCNTR                       | 0x0          | 0x7
2025-05-19 14:52:53.093 [info] EPTX01_00CHNCNTR                    | 0x0          | 0x88
2025-05-19 14:52:53.093 [info] EPTX03_02CHNCNTR                    | 0x0          | 0x80
2025-05-19 14:52:53.093 [info] EPTX11_10CHNCNTR                    | 0x0          | 0x88
2025-05-19 14:52:53.093 [info] EPTX21_20CHNCNTR                    | 0x7          | 0x0
2025-05-19 14:52:53.093 [info] EPTX23_22CHNCNTR                    | 0x7          | 0x88
2025-05-19 14:52:53.093 [info] EPTX31_30CHNCNTR                    | 0x0          | 0x88
2025-05-19 14:52:53.093 [info] EPTX33_32CHNCNTR                    | 0x0          | 0x88
2025-05-19 14:52:53.093 [error] expected and read back configuration DON'T match
[2025-05-19 14:52:53.093] [error] expected and read back configuration DON'T match




config outputs2.yaml


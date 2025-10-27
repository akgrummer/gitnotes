STAGE1_VER=ras_tmux_ouput_reorder
HGCAL_FC_VER=task/adapt-tcds2-0-2
VIVADO_VER=2022.2
MODELSIM_VER=2020.2
APOLLO_CM_INFRA_VER=v2.2.0
IPBUS_VER=v1.14.1
LEGACY_TTC_VER=v2.1
TCDS2_VER=v0_2_0_rc3
TCLINK_VER=fixes
GBT_FPGA_VER=gbt_fpga_6_1_0
LPGBT_FPGA_VER=v.2.1
GBTSC_VER=gbt_sc_4_3
SLINK_VER=v03.12
SLINK_IP_VER=v03.12
SLINK_LOCAL_VER=emp_multi_quad
HGCAL_10G_RO_VER=DTH_beamtest_dev
IPBB_VIVADO_LOGLEVEL=warn
EMP_FWK_VER=hgcal_dev
MINIDAQ_VER=v1


ipbb init hgc_work_area2
cd hgc_work_area2

ipbb add git --depth 1 https://github.com/ipbus/ipbus-firmware -b ${IPBUS_VER}
ipbb add git --depth 1 https://gitlab.cern.ch/ttc/legacy_ttc.git -b ${LEGACY_TTC_VER}
ipbb add git --depth 1 https://:@gitlab.cern.ch:8443/cms-tcds/cms-tcds2-firmware.git -b ${TCDS2_VER}
ipbb add git --depth 1 https://@gitlab.cern.ch:8443/hgcal-tpg/emp-fwk.git -b ${EMP_FWK_VER}
ipbb add git --depth 1 https://gitlab.cern.ch/jhegeman/tclink.git -b ${TCLINK_VER}
ipbb add git --depth 1 https://gitlab.cern.ch/gbt-fpga/gbt-fpga.git -b ${GBT_FPGA_VER}
ipbb add git --depth 1 https://gitlab.cern.ch/gbt-fpga/lpgbt-fpga.git -b ${LPGBT_FPGA_VER}
ipbb add git --depth 1 https://gitlab.cern.ch/gbtsc-fpga-support/gbt-sc.git -b ${GBTSC_VER}
ipbb add git --depth 1 https://gitlab.cern.ch/dth_p1-v2/slinkrocket_ips.git -b ${SLINK_IP_VER}
ipbb add git --depth 1 https://@gitlab.cern.ch:8443/dth_p1-v2/slinkrocket.git -b ${SLINK_VER}
ipbb add git --depth 1 https://@gitlab.cern.ch:8443/rshukla/hgcal_fast_commands.git -b ${HGCAL_FC_VER}
ipbb add git --depth 1 https://@gitlab.cern.ch:8443/cms-hgcal-firmware/fast-control.git -b ROCv3
ipbb add git --depth 1 https://@gitlab.cern.ch:8443/cms-hgcal-firmware/components/throttle_l1a.git -b master
ipbb add git --depth 1 https://@gitlab.cern.ch:8443/hgcal-tpg/slink_local_readout.git -b ${SLINK_LOCAL_VER}
ipbb add git --depth 1 https://@gitlab.cern.ch:8443/hgcal-tpg/hgcal_lpgbt_data_framers.git
ipbb add git --depth 1 https://@gitlab.cern.ch:8443/cms-hgcal-firmware/components/hgc_minidaq.git -b ${MINIDAQ_VER}
ipbb add git --depth 1 https://@gitlab.cern.ch:8443/hgcal-tpg/stage1.git -b ${STAGE1_VER}
ipbb add git --depth 1 https://:@gitlab.cern.ch:8443/hgcal-tpg/stage1_daq_hybrid.git -b ras_dev



TARGET_PART=xcvu9p-flga2104-2L-e

pushd src/cms-tcds2-firmware
sed -i 's/args\[1\]/target_part/g' ./scripts/vivado_create_ips.sh
./scripts/vivado_create_ips.sh --target-part=${TARGET_PART} --user-ip-repo=../slinkrocket_ips '^(?!(.*(gthe3|gtye3|mmcme3|gth|linkrocket|loopback|axi|legacy|ibert|trigger|tcds2_interface_mgt_timing).*))'
popd
# ./scripts/vivado_create_ips.sh --target-part=xcvu9p-flga2104-2L-e --user-ip-repo=../slinkrocket_ips '^(?!(.*(gthe3|gtye3|mmcme3|gth|linkrocket|loopback|axi|legacy|ibert|trigger|tcds2_interface_mgt_timing).*))'

pushd src/tclink
sed -i 's/args\[1\]/target_part/g' ./scripts/vivado_create_ips.sh
./scripts/vivado_create_ips.sh --target-part=${TARGET_PART} '^(?!(.*(gthe3|gtye3|mmcme3|gth|dfe_5g|lpm_5g|vio_control).*))'
popd
# ./scripts/vivado_create_ips.sh --target-part=xcvu9p-flga2104-2L-e '^(?!(.*(gthe3|gtye3|mmcme3|gth|dfe_5g|lpm_5g|vio_control).*))'

# # ipbb proj create vivado hgcal_hybrid stage1_daq_hybrid:projects/ESR2_SerenityS1 top.dep
# ipbb proj create vivado hgcal_hybrid stage1_daq_hybrid:projects/vcu118_test top.dep
# cd proj/hgcal_hybrid
# ipbb ipbus gendecoders
# ipbb vivado  generate-project --single
# ipbb vivado synth -j8
# ipbb vivado impl -j8
# ipbb vivado package

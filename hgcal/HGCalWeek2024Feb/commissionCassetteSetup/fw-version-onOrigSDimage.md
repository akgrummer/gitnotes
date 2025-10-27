# Original fw installations:

```bash
[HGCAL_dev@hgczcu102-mbv3 (hgc-engine-tools)]$ for f in /opt/cms-hgcal-firmware/hgc-test-systems/*/; do fwver="$(basename "${f}")"; echo ">>> sudo yum list ${fwver}"; sudo yum list ${fwver}; done
>>> sudo yum list interposer
Loaded plugins: fastestmirror
Repository updates is listed more than once in the configuration
Repository updates-source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
 * base: mirror.init7.net
 * epel: linuxsoft.cern.ch
 * extras: mirror.init7.net
 * updates: mirror.init7.net
Installed Packages
interposer.noarch                             2021.11.17.23.32.51-995798ca                             @cern-repo-hgcwebsw
Available Packages
interposer.noarch                             2022.12.13.02.33.07-fce40512                             cern-repo-hgcwebsw
>>> sudo yum list two-engine
Loaded plugins: fastestmirror
Repository updates is listed more than once in the configuration
Repository updates-source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
 * base: mirror.init7.net
 * epel: linuxsoft.cern.ch
 * extras: mirror.init7.net
 * updates: mirror.init7.net
Installed Packages
two-engine.noarch                  feature_eight_engine-2024_01_19_21_02_49.5138cc23                   @cern-repo-hgcwebsw
>>> sudo yum list unicorn
Loaded plugins: fastestmirror
Repository updates is listed more than once in the configuration
Repository updates-source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
 * base: mirror.init7.net
 * epel: linuxsoft.cern.ch
 * extras: mirror.init7.net
 * updates: mirror.init7.net
Installed Packages
unicorn.noarch                  feature_update_submodules-2023_06_19_19_37_32.59595065                  installed
Available Packages
unicorn.noarch                  test_timing_improvement-2023_04_21_04_16_13.599b8f54                    cern-repo-hgcwebsw
>>> sudo yum list zcu102-ldv3-r1p0
Loaded plugins: fastestmirror
Repository updates is listed more than once in the configuration
Repository updates-source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
 * base: mirror.init7.net
 * epel: linuxsoft.cern.ch
 * extras: mirror.init7.net
 * updates: mirror.init7.net
Installed Packages
zcu102-ldv3-r1p0.noarch                          2022.04.13.03.56.46-3d0d774f                          @cern-repo-hgcwebsw
Available Packages
zcu102-ldv3-r1p0.noarch                          2022.07.22.00.33.40-8ad6bd5f                          cern-repo-hgcwebsw
>>> sudo yum list zcu102-ldv3-r1p0-ext-clk-trunk-v3
Loaded plugins: fastestmirror
Repository updates is listed more than once in the configuration
Repository updates-source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
 * base: mirror.init7.net
 * epel: linuxsoft.cern.ch
 * extras: mirror.init7.net
 * updates: mirror.init7.net
Installed Packages
zcu102-ldv3-r1p0-ext-clk-trunk-v3.noarch                 2022.08.12.15.15.58-761fefbf                  @cern-repo-hgcwebsw
Available Packages
zcu102-ldv3-r1p0-ext-clk-trunk-v3.noarch                 2022.08.30.11.06.38-761fefbf                  cern-repo-hgcwebsw
>>> sudo yum list zcu102-ldv3-r1p0-ext-clk-trunk-v3-transactor
Loaded plugins: fastestmirror
Repository updates is listed more than once in the configuration
Repository updates-source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
 * base: mirror.init7.net
 * epel: linuxsoft.cern.ch
 * extras: mirror.init7.net
 * updates: mirror.init7.net
Installed Packages
zcu102-ldv3-r1p0-ext-clk-trunk-v3-transactor.noarch            2022.08.31.19.45.05-90a9d978            @cern-repo-hgcwebsw
>>> sudo yum list zcu102-ldv3-r1p0-ROCv3
Loaded plugins: fastestmirror
Repository updates is listed more than once in the configuration
Repository updates-source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
 * base: mirror.init7.net
 * epel: linuxsoft.cern.ch
 * extras: mirror.init7.net
 * updates: mirror.init7.net
Installed Packages
zcu102-ldv3-r1p0-ROCv3.noarch       feature_ROCv3_ENGv3_econd1_10_1-2023_02_25_02_01_31.4c922380       @cern-repo-hgcwebsw
Available Packages
zcu102-ldv3-r1p0-ROCv3.noarch       2022.10.27.23.21.51-7667e226                                       cern-repo-hgcwebsw
>>> sudo yum list zcu102-ldv3-r1p0-ROCv3-ECOND
Loaded plugins: fastestmirror
Repository updates is listed more than once in the configuration
Repository updates-source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
 * base: mirror.init7.net
 * epel: linuxsoft.cern.ch
 * extras: mirror.init7.net
 * updates: mirror.init7.net
Installed Packages
zcu102-ldv3-r1p0-ROCv3-ECOND.noarch      feature_ROCv3_ENGv3_econd18-2023_02_22_03_11_15.b3b25e43      @cern-repo-hgcwebsw
Available Packages
zcu102-ldv3-r1p0-ROCv3-ECOND.noarch      2022.10.27.23.21.51-7667e226                                  cern-repo-hgcwebsw
>>> sudo yum list zcu102-siengine-v1p0
Loaded plugins: fastestmirror
Repository updates is listed more than once in the configuration
Repository updates-source is listed more than once in the configuration
Loading mirror speeds from cached hostfile
 * base: mirror.init7.net
 * epel: linuxsoft.cern.ch
 * extras: mirror.init7.net
 * updates: mirror.init7.net
Installed Packages
zcu102-siengine-v1p0.noarch                        2022.01.29.19.35.44-5bea77fa                        @cern-repo-hgcwebsw
Available Packages
zcu102-siengine-v1p0.noarch                        2022.04.30.17.34.55-a2f4d68c                        cern-repo-hgcwebsw
```

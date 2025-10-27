# Lab C computer Setup
- `sudo yum update`
- `sudo yum install python39` - possible in Centos8
- copied bashrc (kept default bashrc and pasted in new parts) and vimrc from ZCU
- making dir `cass-sw/` for future work 
- installed packages from  `hexactrl-sw`
	- https://gitlab.cern.ch/hgcal-daq-sw/hexactrl-sw#sw-installation-on-the-remote-pc-
	```
	sudo yum install epel-release
	sudo yum update
	sudo yum install pugixml pugixml-devel cmake zeromq zeromq-devel cppzmq-devel libyaml yaml-cpp yaml-cpp-devel boost boost-devel root
	```
	- couldn't find: `libyaml-devel`
	- using a python virtual environment
		- created with `python3 -m venv /path/to/new/virtual/environment`
		- activated with `source /path-to-env/bin/activate`
		- doing this in the bashrc now
			- `export VIRTUAL_ENV_DISABLE_PROMPT=1 #don't change prompt`
	- tkinter:  `sudo yum install python39-tkinter`
	- `pip install matplotlib`
	- `pip install boost_histogram`
## hexa setup:
- setup network passthrough:
- `/etc/sysconfig/network-scripts/ifcfg-eth0`
- on 91:
	Name        : interposer
	Arch        : noarch
	Version     : 2022.09.14.23.08.44
	Release     : 46b02124
	Size        : 16 M
	Repo        : installed



# ZCU setup
## global python3.9 install:
used (similar instructions to above):
https://www.liquidweb.com/kb/how-to-install-python-3-on-centos-7/
and got version Python-3.9.13 from python.org
this version should be compatible with the openssl version on hcalpro
note: need to use sudo for the make altinstall
python3.9 now exists in:
/usr/local/bin/python3.9

the other python versions exist in:
/usr/bin/

- install python3.9 on ZCU:
```bash
# https://www.liquidweb.com/kb/how-to-install-python-3-on-centos-7/
wget https://www.python.org/ftp/python/3.9.15/Python-3.9.15.tgz
tar -xzf Python-3.9.15.tgz
cd Python-3.9.15/
sudo ./configure --enable-optimizations
sudo make altinstall
```
	Messages:
```bash
Installing collected packages: setuptools, pip
  WARNING: The script pip3.9 is installed in '/usr/local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-22.0.4 setuptools-58.1.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```

- Working in a virtual environment for python3.9
https://docs.python.org/3/tutorial/venv.html

## Install  ipbus for python3.9
SSHFS didn't work:
- `sudo yum install fuse-sshfs`


```bash
   cd ipbus-software/
    git checkout asteen/UIO-hgcal-dev 
	# ONLY FOR PYTHON 2 - see instructions for python 3 below
    # compile uHal
    make -j2 Set=uhal
    make install -j2 Set=uhal
```
- *python3 compatible uhal installation*
   If compiling to python3 instead of python2, do not checkout the `asteen/UIO-hgcal-dev` branch, but stick to the default `hgcal-uio` branch from the `hgcal-daq-sw/ipbus-software.git` repository.  Additionally, the `pybind11` libraries need to be installed:
   repo also exists here: 
   origin	https://gitlab.cern.ch/asteen/ipbus-software.git
	pastika	https://gitlab.cern.ch/pastika/ipbus-software.git
```bash
	sudo pip3 install "pybind11[global]"
```
    The Makefiles need to be updated in a couple of spots to build the python3 bindings instead of defaulting to python2
	ACTUALLY I PUT the full path instead of just 3.9 - otherwise sudo couldn't find it...
    In `config/Makefile.macros`, line 8, change `python` to `python3`
```bash
	-PYTHON ?= python
	+PYTHON ?= python3.9
```
and in uhal/Makefile, lines 22:
```bash
	PACKAGES := $(filter-out python, $(PACKAGES))
	PACKAGES := $(filter-out python3.9, $(PACKAGES))
```
and line 57:
```bash
	-PYTHON ?= python
	+PYTHON ?= python3.9
```
Then, finally, compile:
```bash
	# compile uHal
	sudo make -j2 Set=uhal
	sudo make install -j2 Set=uhal
```

```bash
sudo env "PATH=$PATH" make -j2 Set=uhal
sudo env "PATH=$PATH" make install -j2 Set=uhal
```

## So to recap
	- installed python3.9 globally
	- installed uhal globally for python3.9
N.B. don't make the venv until after python3.9 is built
	- setup virtual evironement with:
		- `python3.9 -m venv --system-site-packages python39-venv`
		- so it can now use the global uhal
	- bashrc will always start the virtual environment now
	- Note - could probably install uhal for the user only, just without the `sudo`, seems like cleaner solution, but need to move on, this takes some time for the `make` step
	- `pip install numpy`
	- `pip install tabulate`
	- `pip install matplotlib`
	- `pip install smbus2`
	
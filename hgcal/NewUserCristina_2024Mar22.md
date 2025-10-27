#	modified:   gui_windows/clocks.py
#	deleted:    gui_windows/customButtonClass.py
#	new file:   setup-hgc/config_aidan_testSingleEngine.sh
#	new file:   setup-hgc/setup_trains.py
#	new file:   uhalNames.py
#	modified:   uhal_backend_v3.py



new user
add lpc user to labc, kerberos password works to log in


new user uses
export LD_LIBRARY_PATH=/opt/cactus/lib:${HOME}/lib
export HGC_FW_BASE=${HOME}/src
source /home/agrummer/python39-venv/bin/activate

add user
sudo useradd -m jane
Change groups of user in this file:
sudo vim /etc/group

Recursive cass-sw repo clone
then install swamp package

For swamp lpgbt library install don't use `user` option:
pip install --user -e lpgbt_control_lib/


## adding Gabi and Clara:
first to labc
sudo useradd -m gmachado
then again on zcu2
sudo useradd -m gmachado
copy .bashrc

sudo passwd gmachado
(temp hgcal password)

add new user to gitlab cass-sw repo

add users to hgcal and wheel:
sudo vim /etc/group

Gabi: gmachado
Clara: calvarez
all users on LabC:
agrummer  calvarez  cmantill  gmachado  mtinfena  opt  zgecse
all users on zcu2
agrummer  calvarez  cmantill  gmachado  HGCAL_dev  jmmans  pastika  zgecse

### instructions for new user:

log in with kerberos credentials to labc (need active kinit ticket)

ssh gmachado@labc1.fnal.gov

from labc computer:
ssh zcu2
if that doesn't work you may need to update your .ssh/config file, or try:
ssh gmachado@zcu2
ssh gmachado@192.168.1.201

change your zcu2 user password with:
`passwd`

generate an ssh key pair:
https://gitlab.cern.ch/help/user/ssh#generate-an-ssh-key-pair
copy the contents of the public key that was just generated (in ~/.ssh directory, ends with .pug)

when signed in to gitlab, navigate to Preferences >> SSH Keys
select "add new key"
paste the contents of the public key in the Key field and select add key

then from your home directory in zcu2
then git clone -b two-engine --recursive ssh://git@gitlab.cern.ch:7999/agrummer/cass-sw.git


# adding daquser

sudo useradd -m daquser
sudo passwd daquser
(hgcal dev password)
add users to hgcal and wheel:
sudo vim /etc/group

sudo cp daq user

creating venv notes here:
https://gist.github.com/akgrummer/c83306afdf0fabf225c8cf81312411d5







### instructions for new user:

sudo useradd -m rchudasa




brew services start grafana

start influx server with:
influxd

the command line interface installed with:
brew install influxdb-cli

influx config list
influx auth list
influx bucket list
only for cloud:
influx bucket-schema list -n MPOD_example -n current
source env.sh
echo ${INFLUXDB_TOKEN}
influx auth create  --org fnal  --all-access

influx config create --config-name config_2025Apr30 \
  --host-url http://localhost:8086 \
  --org fnal \
  --token ${INFLUXDB_TOKEN} \
  --active

influx query '
  import "influxdata/influxdb/schema"

  schema.measurements(bucket: "MPOD_example")
'
influx DB on : http://localhost:8086
grafana : http://localhost:3000


## notes for what I'd like it to do:

save data from all 19 channels
show data on grafana
extract data to excel

install on labc2 (both influxdb and grafana) and view url from mac (maybe over ssh local port forwarding)


## adding user to org
(grafana_venv) [labc2-fnal-gov Apr30 19:33:52 ~]$ influx org members list -n fnal
ID	Name	User Type	Status
(grafana_venv) [labc2-fnal-gov Apr30 19:36:58 ~]$ influx org members list
ID	Name	User Type	Status
(grafana_venv) [labc2-fnal-gov Apr30 19:37:34 ~]$ influx org list
ID			Name
67e67e63504154c6	fnal
(grafana_venv) [labc2-fnal-gov Apr30 19:37:56 ~]$ influx user list
ID			Name
0ece1bf6b5e6a000	hgcal_dev
(grafana_venv) [labc2-fnal-gov Apr30 19:38:15 ~]$ influx org members add -n fnal -m 0ece1bf6b5e6a000
user "0ece1bf6b5e6a000" has been added as a member of org "67e67e63504154c6"




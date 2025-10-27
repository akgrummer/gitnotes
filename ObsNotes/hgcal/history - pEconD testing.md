  630  ./uhal_string.py -s
  631  ./uhal_string.py --block ro --node passthrough --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.reg0.delay_mode --val 1
 ./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.reg0.delay_mode --val 1
 ./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.reg0.delay_mode --val 1
 ./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.reg0.delay_mode --val 1
 ./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.reg0.delay_mode --val 1
 ./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.reg0.delay_mode --val 1
  638  ./uhal_string.py -s
  639  ./uhal_string.py -b fcrec --node counters.link_reset_rocd
  640  ./uhal_string.py --clks
  642  ./uhal_string.py -s
  643  ./uhal_string.py -b fcrec --node counters.link_reset_econd
  644  ./uhal_string.py -s
  645  ./uhal_string.py -b in --links explicit_align --val 1
  646  ./uhal_string.py -s
  647  ./uhal_string.py -b in --links explicit_align --val 1
  648  ./uhal_string.py -s
  649  ./uhal_string.py --block in --links aquire_length --val 39 
  650  ./uhal_string.py --block in --links total_length --val 39 
  651  ./uhal_string.py --block in --links capture_mode_in --val 2
  656  ./uhal_string.py --block in --node global.continous_acquire --val 63
  # SEND L1A
  657  ./uhal_string.py -s
  658  ./uhal_string.py --b fcrec --node counters.l1a
  659  ./uhal_string.py -s
  660  ./uhal_string.py --fifo in
NEW: ./uhal_string.py --block in --links L1A_offset_or_BX --val 9
NEW: ./uhal_string.py --block in --links aquire_length --val 40
NEW: ./uhal_string.py --block in --links total_length --val 40
  SKIP 661  ./uhal_string.py --block in --links aquire_length --val 50
  SKIP 662  ./uhal_string.py --block in --links total_length --val 50
  ./uhal_string.py --b fcrec --node counters.l1a
  663  ./uhal_string.py -s
  664  ./uhal_string.py --fifo in -q
  665  ./uhal_string.py -s
  666  ./uhal_string.py --fifo in
  667  ./uhal_string.py -s
  668  ./uhal_string.py -b out --links align_pattern --val 2899102912
  669  ./uhal_string.py -b out --links align_pattern --myhex
  670  ./uhal_string.py -s
  671  ./uhal_string.py -b out --node global.explicit_align --val 1
  672  ./uhal_string.py -s
  673  ./uhal_string.py --block ro --node passthrough --val 0
  674  ./uhal_string.py --block in --links capture_mode_in --val 3
  675  ./uhal_string.py --block in --node global.continous_acquire --val 63
  676  ./uhal_string.py -s
  677  ./uhal_string.py -b fcrec --node counters.l1a


./uhal_string.py --block ro --node passthrough --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.reg0.delay_mode --val 1
./uhal_string.py -b fcrec --node counters.link_reset_rocd
./uhal_string.py --clks
./uhal_string.py -b fcrec --node counters.link_reset_econd
./uhal_string.py -b in --links explicit_align --val 1
./uhal_string.py -b in --links explicit_align --val 1
./uhal_string.py --block in --links aquire_length --val 39 
./uhal_string.py --block in --links total_length --val 39 
./uhal_string.py --block in --links capture_mode_in --val 2
./uhal_string.py --block in --node global.continous_acquire --val 63
echo "send l1a"
read -n 1 -s -r -p "Press any key to continue"
echo
./uhal_string.py --b fcrec --node counters.l1a
./uhal_string.py --fifo in
./uhal_string.py --block in --links L1A_offset_or_BX --val 9
echo "send l1a"
read -n 1 -s -r -p "Press any key to continue"
echo
./uhal_string.py --b fcrec --node counters.l1a
./uhal_string.py --fifo in -q
echo "send l1a"
read -n 1 -s -r -p "Press any key to continue"
echo
./uhal_string.py --fifo in
./uhal_string.py -b out --links align_pattern --val 2899102912
./uhal_string.py -b out --links align_pattern --myhex
./uhal_string.py -b out --node global.explicit_align --val 1
./uhal_string.py --block ro --node passthrough --val 0
./uhal_string.py --block in --links capture_mode_in --val 3
./uhal_string.py --block in --node global.continous_acquire --val 63
./uhal_string.py -b fcrec --node counters.l1a
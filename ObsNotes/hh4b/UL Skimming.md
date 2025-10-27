# to run locally (testing):
skim_ntuple.exe --input inputFiles/2016_NMSSM_XYH_bbbb_Datasets/BTagCSV_Data.txt --cfg=config/Resonant_NMSSM_bbbb/skim_2016Resonant_NMSSM_XYH_bbbb.cfg --is-data --maxDeltaR=0.25 --output=testSkimoutput.root --maxEvts=10000000


skim_ntuple.exe --input inputFiles/UL/UL2016_files.txt --cfg=config/Resonant_NMSSM_bbbb/skim_2016Resonant_NMSSM_XYH_bbbb.cfg --is-data --maxDeltaR=0.25 --output=testSkimoutput.root --maxEvts=10000
skim_ntuple.exe --input inputFiles/UL/UL2017_files.txt --cfg=config/Resonant_NMSSM_bbbb/skim_2017Resonant_NMSSM_XYH_bbbb.cfg --is-data --maxDeltaR=0.25 --output=testSkimoutput.root --maxEvts=10000
skim_ntuple.exe --input inputFiles/UL/UL2018_files.txt --cfg=config/Resonant_NMSSM_bbbb/skim_2018Resonant_NMSSM_XYH_bbbb.cfg --is-data --maxDeltaR=0.25 --output=testSkimoutput.root --maxEvts=10000

 # To count the number of entries in the tree:
 H1_b1_pt > 30 && H1_b2_pt > 30 && H2_b1_pt > 30 && H2_b2_pt > 30 && H1_b1_ptRegressed > 30 && H1_b2_ptRegressed > 30 && H2_b1_ptRegressed > 30 && H2_b2_ptRegressed > 30 && H1_b1_eta > -2.4 && H1_b1_eta < 2.4 && H1_b2_eta > -2.4 && H1_b2_eta < 2.4 && H2_b1_eta > -2.4 && H2_b1_eta < 2.4 && H2_b2_eta > -2.4 && H2_b2_eta < 2.4 && IsolatedElectron_pt<15 && IsolatedMuon_pt<10 && ( (HLT_DoubleJet90_Double30_TripleBTagCSV_p087_Fired==1 && HLT_DoubleJet90_Double30_TripleBTagCSV_p087_ObjectMatched>0) || (HLT_QuadJet45_TripleBTagCSV_p087_Fired==1 && HLT_QuadJet45_TripleBTagCSV_p087_ObjectMatched > 0) ) && (NbJets >= 4) && (H1_m >65) && (H1_m < 185)

## 2016
bbbbTree->Draw("H1_b1_pt", "H1_b1_pt > 30 && H1_b2_pt > 30 && H2_b1_pt > 30 && H2_b2_pt > 30 && H1_b1_ptRegressed > 30 && H1_b2_ptRegressed > 30 && H2_b1_ptRegressed > 30 && H2_b2_ptRegressed > 30 && H1_b1_eta > -2.4 && H1_b1_eta < 2.4 && H1_b2_eta > -2.4 && H1_b2_eta < 2.4 && H2_b1_eta > -2.4 && H2_b1_eta < 2.4 && H2_b2_eta > -2.4 && H2_b2_eta < 2.4 && IsolatedElectron_pt<15 && IsolatedMuon_pt<10 && ( (HLT_DoubleJet90_Double30_TripleBTagCSV_p087_Fired==1 && HLT_DoubleJet90_Double30_TripleBTagCSV_p087_ObjectMatched>0) || (HLT_QuadJet45_TripleBTagCSV_p087_Fired==1 && HLT_QuadJet45_TripleBTagCSV_p087_ObjectMatched > 0) ) && (NbJets >= 4) && (H1_m >65) && (H1_m < 185)")
## 2017
bbbbTree->Draw("H1_b1_pt", "H1_b1_pt > 40 && H1_b2_pt > 40 && H2_b1_pt > 40 && H2_b2_pt > 40 && H1_b1_ptRegressed > 40 && H1_b2_ptRegressed > 40 && H2_b1_ptRegressed > 40 && H2_b2_ptRegressed > 40 && H1_b1_eta > -2.5 && H1_b1_eta < 2.5 && H1_b2_eta > -2.5 && H1_b2_eta < 2.5 && H2_b1_eta > -2.5 && H2_b1_eta < 2.5 && H2_b2_eta > -2.5 && H2_b2_eta < 2.5 && IsolatedElectron_pt<15 && IsolatedMuon_pt<10 && ( (HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_Fired==1 && HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_ObjectMatched>0) || (HLT_HT300PT30_QuadJet_75_60_45_40_TripeCSV_p07_Fired==1 && HLT_HT300PT30_QuadJet_75_60_45_40_TripeCSV_p07_ObjectMatched > 0) ) && (NbJets >= 4) && (H1_m >65) && (H1_m < 185)")

## 2018
 bbbbTree->Draw("H1_b1_pt", "H1_b1_pt > 40 && H1_b2_pt > 40 && H2_b1_pt > 40 && H2_b2_pt > 40 && H1_b1_ptRegressed > 40 && H1_b2_ptRegressed > 40 && H2_b1_ptRegressed > 40 && H2_b2_ptRegressed > 30 && H1_b1_eta > -2.5 && H1_b1_eta < 2.5 && H1_b2_eta > -2.5 && H1_b2_eta < 2.5 && H2_b1_eta > -2.5 && H2_b1_eta < 2.5 && H2_b2_eta > -2.5 && H2_b2_eta < 2.5 && IsolatedElectron_pt<15 && IsolatedMuon_pt<10 && (HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_Fired==1 && HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_ObjectMatched>0)  && (NbJets >=4 ) && (H1_m >65) && (H1_m < 185)")


## 2016 3b
bbbbTree->Draw("H1_b1_pt", "H1_b1_pt > 30 && H1_b2_pt > 30 && H2_b1_pt > 30 && H2_b2_pt > 30 && H1_b1_ptRegressed > 30 && H1_b2_ptRegressed > 30 && H2_b1_ptRegressed > 30 && H2_b2_ptRegressed > 30 && H1_b1_eta > -2.4 && H1_b1_eta < 2.4 && H1_b2_eta > -2.4 && H1_b2_eta < 2.4 && H2_b1_eta > -2.4 && H2_b1_eta < 2.4 && H2_b2_eta > -2.4 && H2_b2_eta < 2.4 && IsolatedElectron_pt<15 && IsolatedMuon_pt<10 && ( (HLT_DoubleJet90_Double30_TripleBTagCSV_p087_Fired==1 && HLT_DoubleJet90_Double30_TripleBTagCSV_p087_ObjectMatched>0) || (HLT_QuadJet45_TripleBTagCSV_p087_Fired==1 && HLT_QuadJet45_TripleBTagCSV_p087_ObjectMatched > 0) ) && (NbJets == 3) && (H1_m >65) && (H1_m < 185)")
## 2017 3b
bbbbTree->Draw("H1_b1_pt", "H1_b1_pt > 40 && H1_b2_pt > 40 && H2_b1_pt > 40 && H2_b2_pt > 40 && H1_b1_ptRegressed > 40 && H1_b2_ptRegressed > 40 && H2_b1_ptRegressed > 40 && H2_b2_ptRegressed > 40 && H1_b1_eta > -2.5 && H1_b1_eta < 2.5 && H1_b2_eta > -2.5 && H1_b2_eta < 2.5 && H2_b1_eta > -2.5 && H2_b1_eta < 2.5 && H2_b2_eta > -2.5 && H2_b2_eta < 2.5 && IsolatedElectron_pt<15 && IsolatedMuon_pt<10 && ( (HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_Fired==1 && HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_ObjectMatched>0) || (HLT_HT300PT30_QuadJet_75_60_45_40_TripeCSV_p07_Fired==1 && HLT_HT300PT30_QuadJet_75_60_45_40_TripeCSV_p07_ObjectMatched > 0) ) && (NbJets == 3) && (H1_m >65) && (H1_m < 185)")

## 2018 3b
 bbbbTree->Draw("H1_b1_pt", "H1_b1_pt > 40 && H1_b2_pt > 40 && H2_b1_pt > 40 && H2_b2_pt > 40 && H1_b1_ptRegressed > 40 && H1_b2_ptRegressed > 40 && H2_b1_ptRegressed > 40 && H2_b2_ptRegressed > 30 && H1_b1_eta > -2.5 && H1_b1_eta < 2.5 && H1_b2_eta > -2.5 && H1_b2_eta < 2.5 && H2_b1_eta > -2.5 && H2_b1_eta < 2.5 && H2_b2_eta > -2.5 && H2_b2_eta < 2.5 && IsolatedElectron_pt<15 && IsolatedMuon_pt<10 && (HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_Fired==1 && HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_ObjectMatched>0)  && (NbJets ==3 ) && (H1_m >65) && (H1_m < 185)")

# check the status of the job submissions:
python scripts/getTaskStatus.py --dir jobs_UL2016_data_2022Feb15/SKIM_UL2016_files/ --resubCmd
resubmit the jobs with:
scripts/t3submit jobs_UL2016_data_2022Feb15/SKIM_UL2016_files//job_134.sh

first jobs submissions Feb 15:
	note 2016 needs to be separated to pre and post VFP - so these files aren't useful:
		python scripts/getTaskStatus.py --dir jobs_UL2016_data_2022Feb15/SKIM_UL2016_files/ --resubCmd
	python scripts/getTaskStatus.py --dir jobs_UL2017_data_2022Feb15/SKIM_UL2017_files/ --resubCmd
	python scripts/getTaskStatus.py --dir jobs_UL2018_data_2022Feb15/SKIM_UL2018_files/ --resubCmd

python scripts/getTaskStatus.py --dir jobs_Nominal2016_data_2022Feb17/SKIM_BTagCSV_Data/ --resubCmd
python scripts/getTaskStatus.py --dir jobs_Nominal2017_data_2022Feb17/SKIM_BTagCSV_Data/ --resubCmd
python scripts/getTaskStatus.py --dir jobs_Nominal2018_data_2022Feb17/SKIM_JetHT_Data/ --resubCmd
python scripts/getTaskStatus.py --dir jobs_UL2016_preVFP_data_2022Feb17/SKIM_UL2016_files_preVFP/ --resubCmd
	4 jobs
		scripts/t3submit jobs_UL2016_preVFP_data_2022Feb17/SKIM_UL2016_files_preVFP//job_102.sh
		scripts/t3submit jobs_UL2016_preVFP_data_2022Feb17/SKIM_UL2016_files_preVFP//job_103.sh
		scripts/t3submit jobs_UL2016_preVFP_data_2022Feb17/SKIM_UL2016_files_preVFP//job_107.sh
		scripts/t3submit jobs_UL2016_preVFP_data_2022Feb17/SKIM_UL2016_files_preVFP//job_157.sh
python scripts/getTaskStatus.py --dir jobs_UL2016_postVFP_data_2022Feb17_2/SKIM_UL2016_files_postVFP/ --resubCmd
	1 job
		jobs_UL2016_postVFP_data_2022Feb17_2/SKIM_UL2016_files_postVFP//job_74.sh
bad 2017
	python scripts/getTaskStatus.py --dir jobs_UL2017_data_2022Feb17/SKIM_UL2017_files/ --resubCmd
	14 jobs
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_16.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_17.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_30.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_33.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_35.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_36.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_39.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_49.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_50.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_51.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_71.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_78.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_123.sh
		scripts/t3submit jobs_UL2017_data_2022Feb17/SKIM_UL2017_files//job_135.sh	
python scripts/getTaskStatus.py --dir jobs_UL2017_data_2022Feb20/SKIM_UL2017_files/ --resubCmd
python scripts/getTaskStatus.py --dir jobs_UL2018_data_2022Feb17/SKIM_UL2018_files/ --resubCmd
	14 jobs
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_32.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_53.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_54.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_83.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_84.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_85.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_86.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_88.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_89.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_93.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_94.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_95.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_96.sh
		scripts/t3submit jobs_UL2018_data_2022Feb17/SKIM_UL2018_files//job_108.sh
	

hadd -f Nominal2016data_rerun_2022Feb17.root `xrdfsls -u /store/user/agrummer/bbbb_ntuples/Nominal2016_data_2022Feb17/SKIM_BTagCSV_Data/output`
hadd -f Nominal2017data_rerun_2022Feb17.root `xrdfsls -u /store/user/agrummer/bbbb_ntuples/Nominal2017_data_2022Feb17/SKIM_BTagCSV_Data/output`
hadd -f Nominal2018data_rerun_2022Feb17.root `xrdfsls -u /store/user/agrummer/bbbb_ntuples/Nominal2018_data_2022Feb17/SKIM_JetHT_Data/output`

hadd -f UL2016data_preVFP_2022Feb17.root `xrdfsls -u /store/user/agrummer/bbbb_ntuples/UL2016_preVFP_data_2022Feb17/SKIM_UL2016_files_preVFP/output`
hadd -f UL2016data_postVFP_2022Feb17.root `xrdfsls -u /store/user/agrummer/bbbb_ntuples/UL2016_postVFP_data_2022Feb17_2/SKIM_UL2016_files_postVFP/output`
hadd -f UL2017data_2022Feb17.root `xrdfsls -u /store/user/agrummer/bbbb_ntuples/UL2017_data_2022Feb17/SKIM_UL2017_files/output`
hadd -f UL2018data_2022Feb17.root `xrdfsls -u /store/user/agrummer/bbbb_ntuples/UL2018_data_2022Feb17/SKIM_UL2018_files/output`

python scripts/submitSkimOnTier3.py --input=inputFiles/UL/UL2017_files.txt --tag=UL2017_data_2022Feb20  --cfg=config/Resonant_NMSSM_bbbb/skim_2017Resonant_NMSSM_XYH_bbbb_UL.cfg --is-data --njobs=200 --maxDeltaR=0.25



Files from Fabio
/uscms/home/fravera/nobackup/DiHiggs_v2/CMSSW_10_2_5/src/bbbbAnalysis

-rw-r--r--  1 fravera us_cms 3483498838 Feb 21 09:24 ULsample_2016.root
-rw-r--r--  1 fravera us_cms 1143899475 Feb 21 09:25 ULsample_2017.root
-rw-r--r--  1 fravera us_cms 2129067504 Feb 21 09:28 ULsample_2018.root
-rw-r--r--  1 fravera us_cms 3036177215 Feb 21 09:48 Nominalsample_2016.root
-rw-r--r--  1 fravera us_cms 1371042596 Feb 21 09:51 Nominalsample_2017.root
-rw-r--r--  1 fravera us_cms 2494877674 Feb 21 09:55 Nominalsample_2018.root

Plot these mX and mY distributions  for each year.
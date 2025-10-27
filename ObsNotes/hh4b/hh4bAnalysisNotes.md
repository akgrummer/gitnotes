### skimming
- skimming code is in `src/OfflineProducerHelper.cc`
- TLorentz vectors are on line ~1568
### build (train) the reweighting BDT model
- Build Background commands
		- from:
			`/uscms/home/agrummer/nobackup/DiHiggs_v2/CMSSW_10_2_5/src/bbbbAnalysis`
		- run:
			`python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg`
			`python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg`
			`python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg`
- added an `addSelection` to the config files and use a 'pandas query' to use the selection -> in the `BuildBackgroundModel.py` script
- test making plots:
	`python mlskim_NMSSM_XYH_bbbb/makeplots.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg`
- for Left and Right side training:
	- named the weight: 
		- BDTweights_MassWindow_2022May2_RightSide
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --CRside Right`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --CRside Right`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --CRside Right`
	- named the weight: 
		- BDTweights_MassWindow_2022May2_LeftSide
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --CRside Left`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --CRside Left`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --CRside Left`
- for Inner and Outer CR half training
	- named the weight: 
		- BDTweights_MassWindow_2022May2_OutHalf
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --CRside Out`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --CRside Out`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --CRside Out`
	- named the weight: 
		- BDTweights_MassWindow_2022May2_InHalf
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --CRside In`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --CRside In`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --CRside In`
- for Excluding Left Outer Half and Right Outer half
	- named the weight: 
		- BDTweights_MassWindow_2022May2_OutHalf
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --CRside ExcRightOut`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --CRside ExcRightOut`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --CRside ExcRightOut`
	- named the weight: 
		- BDTweights_MassWindow_2022May2_InHalf
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --CRside ExcLeftOut`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --CRside ExcLeftOut`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --CRside ExcLeftOut`
- for Inner and Outer QUARTER  of inner half of CR training
	- named the weight: 
		- BDTweights_MassWindow_2022Jun14_OutQtr
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --CRside OutQtr`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --CRside OutQtr`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --CRside OutQtr`
	- named the weight: 
		- BDTweights_MassWindow_2022May2_InQtr
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --CRside InQtr`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --CRside InQtr`
		- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --CRside InQtr`
- BJetScores
		- weight name: BDTweights_MassWindow_2022Jun21_Nom - should be a repeat of seed2020 run
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg`
		- weight name: BDTweights_MassWindow_2022Jun21_Nom_bJetScoreLoose - require all four b-jets pass the low bjet threshold
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --bJetScore`
		-  Out half, bJets loose 
			- weight name: BDTweights_MassWindow_2022Jun23_OutHalf_bJetScoreLoose - require all four b-jets pass the low bjet threshold
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --bJetScore --CRside Out`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --bJetScore --CRside Out`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --bJetScore --CRside Out`
		-  In half, bJets loose 
			- weight name: BDTweights_MassWindow_2022Jun23_InHalf_bJetScoreLoose - require all four b-jets pass the low bjet threshold
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --bJetScore --CRside In`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --bJetScore --CRside In`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --bJetScore --CRside In`
- No mass window, BJetScores
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --bJetScore`
- mass group 0 training and mX =300 slice and again with a lower bound of 280 on mX:
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --bJetScore`
- mass group 0 training and mX =300 slice depth 4, leafs 50:
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --bJetScore`
- mass group 0 training and mX =300 slice depth 2, leafs 50:
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --bJetScore`
- Validation region Training
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --bJetScore`
- Up and Down Shape training
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2016_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2017_Full_kinFit.cfg --bJetScore`
			- `python mlskim_NMSSM_XYH_bbbb/BuildBackgroundModel.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg --bJetScore`

### apply the BDT reweighting model to the nTuples (makes a new branch)
- apply background
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir `
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BackgroundModels/Reweight_fullSubmission_2017_v27_PtRegressedAndHigherLevel_kinFit_nTree_500_aidan_2021Dec8/`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BackgroundModels/Reweight_fullSubmission_2018_v27_PtRegressedAndHigherLevel_kinFit_nTree_500_aidan_2021Dec8/`
- apply background for mass window study
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir MassWindowTraining_2022Feb/fullSubmission_2016_v27_MassWindow_mx600my400_2022Feb7`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir MassWindowTraining_2022Feb/fullSubmission_2017_v27_MassWindow_mx600my400_2022Feb7`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir MassWindowTraining_2022Feb/fullSubmission_2018_v27_MassWindow_mx600my400_2022Feb7`
- apply background for mass window study WITH ptX
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2016_v27_MassWindow_mx600my400_2022Feb7_ptX`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2017_v27_MassWindow_mx600my400_2022Feb7_ptX`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2018_v27_MassWindow_mx600my400_2022Feb7_ptX`
- apply background for mass window study  - only mX, mY
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2016_v27_MassWindow_mx600my400_2022Mar2_only_mXmY`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2017_v27_MassWindow_mx600my400_2022Mar2_only_mXmY`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2018_v27_MassWindow_mx600my400_2022Mar2_only_mXmY`
- apply background for mass window study  - without mX, mY
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2016_v27_MassWindow_mx600my400_2022Mar2_without_mXmY`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2017_v27_MassWindow_mx600my400_2022Mar2_without_mXmY`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2018_v27_MassWindow_mx600my400_2022Mar2_without_mXmY`
- use apply for ttbar closure test:
	- example from  fabio
		- `python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BackgroundModels/Reweight_fullSubmission_2017_v25_PtRegressedAndHigherLevel_kinFit/ --signals /store/user/fravera/bbbb_ntuples/fullSubmission_2017_v25`
	- `python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel_ttbarClosure.py --dir BackgroundModels/Reweight_fullSubmission_2016_v27_PtRegressedAndHigherLevel_kinFit_nTree_500_aidan_2021Dec8/ --signals /store/user/agrummer/bbbb_ntuples/fullSubmission_2016_v27`
	- `python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel_ttbarClosure.py --dir BackgroundModels/Reweight_fullSubmission_2017_v27_PtRegressedAndHigherLevel_kinFit_nTree_500_aidan_2021Dec8/ --signals /store/user/agrummer/bbbb_ntuples/fullSubmission_2017_v27`
	- `python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel_ttbarClosure.py --dir BackgroundModels/Reweight_fullSubmission_2018_v27_PtRegressedAndHigherLevel_kinFit_nTree_500_aidan_2021Dec8/ --signals /store/user/agrummer/bbbb_ntuples/fullSubmission_2018_v27`
- Checking systematics of BDT by changing the seed to 1020:
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2016_v27_BDTweights_MassWindow_2022Apr11_seed1020`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2017_v27_BDTweights_MassWindow_2022Apr11_seed1020`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2018_v27_BDTweights_MassWindow_2022Apr11_seed1020`
- also repeating the seed at 2020:
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2016_v27_BDTweights_MassWindow_2022Apr11_seed2020`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2017_v27_BDTweights_MassWindow_2022Apr11_seed2020`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/MassWindowTraining_2022Feb/fullSubmission_2018_v27_BDTweights_MassWindow_2022Apr11_seed2020`
- BDT Left and right sides:
	- Right Side
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022May2_RightSide`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022May2_RightSide`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022May2_RightSide`
	- Left side:
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022May2_LeftSide`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022May2_LeftSide`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022May2_LeftSide`
- BDT Outer and Inner Half:
	- Out Half
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022May2_OutHalf`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022May2_OutHalf`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022May2_OutHalf`
	- Inner half
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022May2_InHalf`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022May2_InHalf`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022May2_InHalf`
- BDT Excluding Right outer half and left outer half of CR
	- ExcRightOut
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022May24_ExcRightOut`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022May24_ExcRightOut`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022May24_ExcRightOut`
	- ExcLeftOut
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022May24_ExcLeftOut`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022May24_ExcLeftOut`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022May24_ExcLeftOut`
- BDT Outer and Inner Quarter (of inner half CR):
	- Out Quarter
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022Jun14_OutQtr`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022Jun14_OutQtr`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022Jun14_OutQtr`
	- Inner Quarter
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022Jun14_InQtr`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022Jun14_InQtr`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022Jun14_InQtr`
- BDT trained with a BJet Threshold
	- bjet loose requirements
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022Jun21_Nom_bJetScoreLoose`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022Jun21_Nom_bJetScoreLoose`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022Jun21_Nom_bJetScoreLoose`
	- repeat nom:
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022Jun21_Nom`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022Jun21_Nom`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022Jun21_Nom`
	- Out Half bjet loose requirements
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022Jun23_OutHalf_bJetScoreLoose`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022Jun23_OutHalf_bJetScoreLoose`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022Jun23_OutHalf_bJetScoreLoose`
	- In Half bjet loose requirements
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_MassWindow_2022Jun23_InHalf_bJetScoreLoose`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_MassWindow_2022Jun23_InHalf_bJetScoreLoose`
		`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_MassWindow_2022Jun23_InHalf_bJetScoreLoose`
- Full BDT, bLooseJets
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Jul7_bJetScoreLoose`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Jul7_bJetScoreLoose`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Jul7_bJetScoreLoose`
- Full BDT, bLooseJets
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Jul14_bJetScore1p5`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Jul14_bJetScore1p5`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Jul14_bJetScore1p5`
- Mass group 0 BDT (messed up the build a couple times. `MassGroup0_bJetLoose_2` is the correct name for the weights)
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Aug4_MassGroup0_bJetLoose_2`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Aug4_MassGroup0_bJetLoose_2`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Aug4_MassGroup0_bJetLoose_2`
- Slice around Mx = 300 (did too large of a slice first time (212<mX<450) correct name is with `_2` (212<mX<400))
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Sep14_Mx300_bJetLoose_2`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Sep14_Mx300_bJetLoose_2`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Sep14_Mx300_bJetLoose_2`
- Slice around Mx = 300 (with a lower bound of 280)
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Sep14_Mx300_bJetLoose_mx280cut`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Sep14_Mx300_bJetLoose_mx280cut`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Sep14_Mx300_bJetLoose_mx280cut`
- Slice around Mx = 300 , depth 4, leafs 50
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Sep14_Mx300_bJetLoose_depth4_leafs50`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Sep14_Mx300_bJetLoose_depth4_leafs50`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Sep14_Mx300_bJetLoose_depth4_leafs50`
- Slice around Mx = 300 , depth 2, leafs 50
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Sep14_Mx300_bJetLoose_depth2_leafs50`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Sep14_Mx300_bJetLoose_depth2_leafs50`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Sep14_Mx300_bJetLoose_depth2_leafs50`
- Validation Region Training
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Oct25_ValRegTrain_bJetLoose`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Oct25_ValRegTrain_bJetLoose`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Oct25_ValRegTrain_bJetLoose`
- Shapes UP and DOWN
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Nov14_bJetScoreLoose_shapeUp`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Nov14_bJetScoreLoose_shapeUp`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Nov14_bJetScoreLoose_shapeUp`
	
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2016_v27_BDTweights_2022Nov14_bJetScoreLoose_shapeDown`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2017_v27_BDTweights_2022Nov14_bJetScoreLoose_shapeDown`
	`python mlskim_NMSSM_XYH_bbbb/ApplyBackgroundModel.py --dir BDToutput/fullSubmission_2018_v27_BDTweights_2022Nov14_bJetScoreLoose_shapeDown`
### submitting BDT on the grid:
	python scripts/submitBDTOnTier3.py --tag 2022Apr19
	python scripts/submitBDTOnTier3.py --tag 2022Apr20
- reorganize the data on eos...
	- save only the data that is used for building the BDT:
		- mlskim_NMSSM_XHY_bbbb/SkimMassWindow_2022Apr25.py
		- for each year:(added a year variable in the config files)
			- `python mlskim_NMSSM_XYH_bbbb/SkimMassWindow_2022Apr25.py --config mlskim_NMSSM_XYH_bbbb/config/outputskim_2018_Full_kinFit.cfg`
	- hadd the full skimmed files to a single file:
	- /store/user/agrummer/bbbb_ntuples/fullSubmission_2016_v27_BDTsyst/fullSubmission_2016_v27
fullSubmission_2016_v27_merged.root
example hadd from lpc webpage:
- hadd myTarget.root `xrdfsls -u /store/user/username/rootFiles | grep '\.root'`
- hadd testMerge_2016BDT_seed2020.root `xrdfsls -u /store/user/agrummer/bbbb_ntuples/fullSubmission_2016_v27_BDTsyst/seeds/seed2020/SKIM_BTagCSV_Data/output/ | grep '\.root'`
- xrdcp testMerge_2016BDT_seed2020.root $EOS/store/user/agrummer/bbbb_ntuples/fullSubmission_2016_v27_BDTsyst/seeds/seed2020/SKIM_BTagCSV_Data/

- submit the apply BDT step:
	- copy the BDT weights to lpc and then include them in the tar for the apply step
	
	- The training was performed with: `python scripts/submitBDTOnTier3.py --tag 2022Apr26_all`
	- The apply NOT is performed with: `python scripts/submitApplyBDTOnTier3.py --tag 2022Apr26_all --year 2017`
	- The apply is performed with: `python scripts/runApplyBDTlocal.py --tag 2022Apr26_all --year 2016`
	`grep -nr "Err" BDTgridSubmit/runLocalOutput/2017/seed2024/`
	agrummer@cmslpc102

### fill the histograms and create outPlotter.root
- Code: fill_histograms.exe
- run with `fill_histograms.exe configfile`
	edited cfg file to have fewer signal points
	- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2016Resonant_NMSSM_XYH_bbbb_Full.cfg`
	- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2017Resonant_NMSSM_XYH_bbbb_Full.cfg`
	- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2018Resonant_NMSSM_XYH_bbbb_Full.cfg`
- Config files:
    - ( *called from bottom of plotter_ config file* ) config file (one for each year) with weight branch name:
        - config/Resonant_NMSSM_bbbb/selectionCfg_2016Resonant_NMSSM_XYH_bbbb_all.cfg
                - config files contain syst. weights and variable binning
                *do sig_..._3bScaled weights need to be changed?*
                *same question for kinfit_up and kinfit_down*
        - Config file( one for each year ):
	        -  `config/Resonant_NMSSM_bbbb/plotter_2017Resonant_NMSSM_XYH_bbbb_Full_quicktest_2021Dec8.cfg`
            - changed selection_ config to "rebinned" versions
        - **how do I check if the luminosity is right? - fabio used correct lumis in the Full files; but probably a 1% effect**
        *added several points:*
        signals = `sig_NMSSM_bbbb_MX_700_MY_300, sig_NMSSM_bbbb_MX_500_MY_200, sig_NMSSM_bbbb_MX_900_MY_400, sig_NMSSM_bbbb_MX_1400_MY_600, sig_NMSSM_bbbb_MX_1800_MY_800, sig_NMSSM_bbbb_MX_300_MY_125, sig_NMSSM_bbbb_MX_300_MY_150, sig_NMSSM_bbbb_MX_600_MY_400, sig_NMSSM_bbbb_MX_700_MY_500, sig_NMSSM_bbbb_MX_800_MY_600, sig_NMSSM_bbbb_MX_600_MY_400, sig_NMSSM_bbbb_MX_900_MY_250, sig_NMSSM_bbbb_MX_1000_MY_300, sig_NMSSM_bbbb_MX_1200_MY_200` 
        new outputdir:
        `./2016DataPlots_NMSSM_XYH_bbbb_dataDrivenStudies_aidan_2021Dec15`
- for FULL FILL use `scripts/submitAllFillOnTier3_RunII.sh` (change the tag inside), which uses scripts/submitFillOnTier3.py for each year
	- the outputFolder in `plotter config` is not used when submitting to condor
	- then you have to merge the outputs:
		- mergeHistograms.py and use the same tag as in `submitAllFillOnTier3_RunII`
			- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_v34_aidan_2021Dec21`
			- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_v34_aidan_2021Dec21`
			- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_v34_aidan_2021Dec21`
			- For rebinned submission:
				-  `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_v34_aidan_rebinnned_2021Dec23`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_v34_aidan_rebinnned_2021Dec23`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_v34_aidan_rebinnned_2021Dec23`
			- for full BDT with b-jets selections
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_2022Jul7_fullBDT_bJetScoreLoose`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_2022Jul7_fullBDT_bJetScoreLoose`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_2022Jul7_fullBDT_bJetScoreLoose`
			- for full BDT with b-jets selections
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_2022Jul14_fullBDT_bJetScore1p5`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_2022Jul14_fullBDT_bJetScore1p5`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_2022Jul14_fullBDT_bJetScore1p5`
			- for full BDT b-jets loose selections, low mass cut
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_2022Aug1_fullBDT_bJetLoose_CutLowMx`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_2022Aug1_fullBDT_bJetLoose_CutLowMx`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_2022Aug1_fullBDT_bJetLoose_CutLowMx`
			- for mass group 0
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_2022Aug4_MassGroup0_bJetLoose`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_2022Aug4_MassGroup0_bJetLoose`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_2022Aug4_MassGroup0_bJetLoose`
			- for mX = 300 slice
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_2022Sep14_Mx300_bJetLoose_3`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_2022Sep14_Mx300_bJetLoose_3`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_2022Sep14_Mx300_bJetLoose_3`
				moved to `_2` because of training on wrong slice, 
				moved to `_3` because filled with wrong bdt and on wrong slice
			- for mX = 300 slice, lower bound of mx=280
					edit plotter config and selection config (for BDT weights input and mass window selection)
					edit and run submitallFillonTier3 takes some time to run on grid
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_2022Sep14_Mx300_bJetLoose_mx280cut`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_2022Sep14_Mx300_bJetLoose_mx280cut`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_2022Sep14_Mx300_bJetLoose_mx280cut`
			- for mX = 300 slice, depth (2, 4), leafs (50)
					edit plotter config --> really: selection config (for BDT weights input and mass window selection)
					! edit ! and run `source scripts/submitAllFillOnTier3_RunII.sh`; takes some time to run on grid
				- this is where you left off Monday night, 2022 Sep 26. - rerunning fill for depth 4, leafs 50. the next study (depth2) is running limits
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_2022Sep14_Mx300_bJetLoose_depth4_leafs50_3`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_2022Sep14_Mx300_bJetLoose_depth4_leafs50_3`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_2022Sep14_Mx300_bJetLoose_depth4_leafs50_3`
				
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_2022Sep14_Mx300_bJetLoose_depth2_leafs50`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_2022Sep14_Mx300_bJetLoose_depth2_leafs50`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_2022Sep14_Mx300_bJetLoose_depth2_leafs50`
					- edit and use `source renameFullSubmissions.sh` to rename the output folder names before unrolling
						- have to edit the tag in the script first
			- for Validation Region Training
							- edit plotter config --> really: selection config (for BDT weights input and mass window selection)
				- ! edit ! and run `source scripts/submitAllFillOnTier3_RunII.sh`; takes some time to run on grid
					- `python scripts/submitFillOnTier3.py --tag fullSubmission_2016_v27_BDTweights_2022Oct25_ValRegTrain_bJetLoose --cfg config/Resonant_NMSSM_bbbb/plotter_2016Resonant_NMSSM_XYH_bbbb_Full.cfg`
					- `python scripts/submitFillOnTier3.py --tag fullSubmission_2017_v27_BDTweights_2022Oct25_ValRegTrain_bJetLoose --cfg config/Resonant_NMSSM_bbbb/plotter_2017Resonant_NMSSM_XYH_bbbb_Full.cfg`
					- `python scripts/submitFillOnTier3.py --tag fullSubmission_2018_v27_BDTweights_2022Oct25_ValRegTrain_bJetLoose --cfg config/Resonant_NMSSM_bbbb/plotter_2018Resonant_NMSSM_XYH_bbbb_Full.cfg`

				- stopped here on Oct25
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_2022Oct25_ValRegTrain_bJetLoose`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_2022Oct25_ValRegTrain_bJetLoose`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_2022Oct25_ValRegTrain_bJetLoose`
					- edit and use `source renameFullSubmissions.sh` to rename the output folder names before unrolling
						- have to edit the tag in the script first
			- For Shapes UP and DOWN
				- Ran the Fill 2 times:
					- once for all signals with a couple variables (MX, MY, MH, 2d hists)
					- Once for a few signals and all analysis variables
				- edit plotter config --> really: selection config (for BDT weights input and mass window selection)
				
				- ! edit ! and run `source scripts/submitAllFillOnTier3_RunII.sh`; takes some time to run on grid
					- python scripts/submitFillOnTier3.py --tag fullSubmission_2016_BDTweights_2022Nov14_bJetScoreLoose_shapes2  --cfg config/Resonant_NMSSM_bbbb/plotter_2016Resonant_NMSSM_XYH_bbbb_Full.cfg
					- python scripts/submitFillOnTier3.py --tag fullSubmission_2016_BDTweights_2022Nov14_bJetScoreLoose_shapes2  --cfg config/Resonant_NMSSM_bbbb/plotter_2017Resonant_NMSSM_XYH_bbbb_Full.cfg
					- python scripts/submitFillOnTier3.py --tag fullSubmission_2016_BDTweights_2022Nov14_bJetScoreLoose_shapes2 --cfg config/Resonant_NMSSM_bbbb/plotter_2018Resonant_NMSSM_XYH_bbbb_Full.cfg
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_BDTweights_2022Nov14_bJetScoreLoose_shapes2`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_BDTweights_2022Nov14_bJetScoreLoose_shapes2`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_BDTweights_2022Nov14_bJetScoreLoose_shapes2`
					- the 2 is because the first run got corrupted somewhere.
					- also trying to run with all analysis vars with additional tag `_allVars`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_BDTweights_2022Nov14_bJetScoreLoose_shapes_allVars_selectSigs`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_BDTweights_2022Nov14_bJetScoreLoose_shapes_allVars_selectSigs`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_BDTweights_2022Nov14_bJetScoreLoose_shapes_allVars_selectSigs`
					- edit and use `source renameFullSubmissions.sh` to rename the output folder names before unrolling
						- have to edit the tag in the script first
			- for preapproval plots - bjet eta vs phi and nJets distributions
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_BDTweights_2023Feb13_preapprovalVars2`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_BDTweights_2023Feb13_preapprovalVars2`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_BDTweights_2023Feb13_preapprovalVars2`
				- The 2 in the tag is for updated binning (phi was out of range) and now looking at NbJets from the root file instead of nJets.
				- edit and use `source renameFullSubmissions.sh` to rename the output folder names before unrolling
				 				- have to edit the tag in the script first
			- for arc chair question - gen matched mH plots (edited selecitons config to add gen matching to selection bjets and the selected signals to plot)
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_BDTweights_2023Feb21_genMatched`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_BDTweights_2023Feb21_genMatched`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_BDTweights_2023Feb21_genMatched`
				- edit and use `source renameFullSubmissions.sh` to rename the output folder names before unrolling
				 				- have to edit the tag in the script first
			- for arc chair question - rebinning of mX and mY plots for better visualization
					- `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_BDTweights_2023Feb21_visualBinning3`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_BDTweights_2023Feb21_visualBinning3`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_BDTweights_2023Feb21_visualBinning3`
				- edit and use `source renameFullSubmissions.sh` to rename the output folder names before unrolling
				- the 2 is because I messed up the binning syntax and but brackets around the list
				- the 3 is for another binning - the bins were still very small for the low mY
				 				- have to edit the tag in the script first
			- for arc chair question - analysis binning, correct the 1D plots to match the 2d hist binnning
							 - `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_BDTweights_2023Feb22_analysisBinning`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_BDTweights_2023Feb22_analysisBinning`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_BDTweights_2023Feb22_analysisBinning`
				- edit and use `source renameFullSubmissions.sh` to rename the output folder names before unrolling
				- the 2 is because I messed up the binning syntax and but brackets around the list
				- the 3 is for another binning - the bins were still very small for the low mY
				 				- have to edit the tag in the script first
			- for arc chair question - check the mx and my relationship by cutting on mx at 500  and making two sets of plots
							 - `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_BDTweights_2023Feb22_Mxlt500_3`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_BDTweights_2023Feb22_Mxlt500_3`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_BDTweights_2023Feb22_Mxlt500_3`
	
							 - `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_BDTweights_2023Feb22_Mxgt500`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_BDTweights_2023Feb22_Mxgt500`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_BDTweights_2023Feb22_Mxgt500`
	
							 - `python ./scripts/mergeHistograms.py --tag fullSubmission_2016_BDTweights_2023Feb22_Mxgt800`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2017_BDTweights_2023Feb22_Mxgt800`
				- `python ./scripts/mergeHistograms.py --tag fullSubmission_2018_BDTweights_2023Feb22_Mxgt800`
				- edit and use `source renameFullSubmissions.sh` to rename the output folder names before unrolling
				- the 2 is because I messed up the binning syntax and but brackets around the list
				- the 3 is for another binning - the bins were still very small for the low mY
				 				- have to edit the tag in the script first
			- for arc chair question -  how much does the trig threshold impact the analysis
				- `fullSubmission_2016_BDTweights_2023Feb27_TrigCut`
        - run the job from dir above scripts
- Can also use the `fill_histograms.exe` for variable plotting
	- if you changed the BDT trainging, change to the branch in the selection_ config file, variable `data_BTagCSV_dataDriven_kinFit`
	- running a selected mass window test;
		- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2016Resonant_NMSSM_XYH_bbbb_Full_quicktest_2022Feb.cfg`
		- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2017Resonant_NMSSM_XYH_bbbb_Full_quicktest_2022Feb.cfg`
		- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2018Resonant_NMSSM_XYH_bbbb_Full_quicktest_2022Feb.cfg`
- **added a mass Test Mass Window in the selction config:**
	- `config/Resonant_NMSSM_bbbb/selectionCfg_2016Resonant_NMSSM_XYH_bbbb_all.cfg`
	- TestMassWindow is called in the "selectionbjets" selection
		- tried calling the cut as its own selection in the plotter config ( but didn't work as expected, so I abandoned this idea for the one above):
				- `config/Resonant_NMSSM_bbbb/plotter_2018Resonant_NMSSM_XYH_bbbb_Full_quicktest_2022Feb.cfg`
				- adding  TestMassWindow here added directories inside of the output root file
	- Changed the BDT to the mass window training BDT 
	- (with original training variables!) in all selection BDT config files (line 1590)
	- the BDT weight name is: `MassWindow_mx600my400_2022Feb7` 
		- added ptX to the training, BDT weight name `MassWindow_mx600my400_2022Feb7_ptX`
	- plot with `plotVars_2022Feb.py`  (change idir and odir)
	- BDT with only mX mY, and without mX mY:
	- the BDT weight name is: `MassWindow_mx600my400_2022Mar2_only_mXmY` 
	- the BDT weight name is: `MassWindow_mx600my400_2022Mar2_without_mXmY` 
	- running a selected mass window test;
		- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2016Resonant_NMSSM_XYH_bbbb_Full_quicktest_2022Feb.cfg`
		- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2017Resonant_NMSSM_XYH_bbbb_Full_quicktest_2022Feb.cfg`
		- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2018Resonant_NMSSM_XYH_bbbb_Full_quicktest_2022Feb.cfg`
	- TTBAR closure test:
	- edit all 3 config files to add ttbar*_3bScaled histogram settings
	- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2016Resonant_NMSSM_XYH_bbbb_Full_ttbarClosure.cfg`
	- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2017Resonant_NMSSM_XYH_bbbb_Full_ttbarClosure.cfg`
	- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2018Resonant_NMSSM_XYH_bbbb_Full_ttbarClosure.cfg`
	- copied the ttbar output.root files ({YEAR}DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data_{VR}) into {YEAR}DataPlots_2022Apr6_fullBDT_MassWindow_{VR}
	- BDT systematics test:
		- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2016Resonant_NMSSM_XYH_bbbb_systBDT_2022Apr.cfg`
		- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2017Resonant_NMSSM_XYH_bbbb_systBDT_2022Apr.cfg`
		- `fill_histograms.exe config/Resonant_NMSSM_bbbb/plotter_2018Resonant_NMSSM_XYH_bbbb_systBDT_2022Apr.cfg`
**the code crashed on the first try... complaining that the output folder already existed when it did not. Code worked on 2nd try**

### TTBAR BKG shape
- 2016
        `root -l -q './scripts/BkgShape_ttbar.cc("VarPlots/rootHists/2016DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data/outPlotter.root", "selectionbJets_ValidationRegionBlinded")'`
        `root -l -q './scripts/BkgShape_ttbar.cc("VarPlots/rootHists/2016DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data/outPlotter.root", "selectionbJets_ControlRegionBlinded")'`
        `root -l -q './scripts/BkgShape_ttbar.cc("VarPlots/rootHists/2016DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data/outPlotter.root", "selectionbJets_SignalRegion")'`
- 2017
        `root -l -q './scripts/BkgShape_ttbar.cc("VarPlots/rootHists/2017DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data/outPlotter.root", "selectionbJets_ValidationRegionBlinded")'`
        `root -l -q './scripts/BkgShape_ttbar.cc("VarPlots/rootHists/2017DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data/outPlotter.root", "selectionbJets_ControlRegionBlinded")'`
        `root -l -q './scripts/BkgShape_ttbar.cc("VarPlots/rootHists/2017DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data/outPlotter.root", "selectionbJets_SignalRegion")'`
- 2018
        `root -l -q './scripts/BkgShape_ttbar.cc("VarPlots/rootHists/2018DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data/outPlotter.root", "selectionbJets_ValidationRegionBlinded")'`
        `root -l -q './scripts/BkgShape_ttbar.cc("VarPlots/rootHists/2018DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data/outPlotter.root", "selectionbJets_ControlRegionBlinded")'`
        `root -l -q './scripts/BkgShape_ttbar.cc("VarPlots/rootHists/2018DataPlots_2022Mar17_fullBDT_TTBAR_MassWindow_data/outPlotter.root", "selectionbJets_SignalRegion")'`
### unroll the 2d plots
### modify the plots to look at the bkg model (instead of signal)
- code: scripts/modifyPlotForControlTest.C+
- now using code: scripts/modifyAllPlotForControlTest.C+
- - run with:
    `root -l './scripts/modifyAllPlotForControlTest.C("v34_aidan_2021Dec21")'`
    `root -l './scripts/modifyAllPlotForControlTest.C("v34_aidan_2022Jan26")'`
    `root -l './scripts/modifyAllPlotForControlTest.C("v34_aidan_rebinnned_2021Dec23")'`
    `root -l './scripts/modifyAllPlotForValidationTest.C("v34_aidan_2021Dec21")'`
    `root -l './scripts/modifyAllPlotForControlTest.C("v34_aidan_rebinnned_2021Dec23")'`
	- to run validation Region:
		    `root -l './scripts/modifyAllPlotForValidationTest.C("v34_aidan_2021Dec21")'`
		    `root -l './scripts/modifyAllPlotForValidationTest.C("v34_aidan_rebinnned_2021Dec23")'`
		    `root -l './scripts/modifyAllPlotForValidationTest.C("v34_aidan_2022Jan26_VR_mx600_my400")'`
	- for single points:
		    `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Feb8_BDTmasscut")'`
		    `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Feb8_BDTmasscut_ptX")'`
		    `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Feb8_BDTmasscut_VR")'`
		    `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Feb8_BDTmasscut_ptX_VR")'`
	  for BDT train on a smaller mass window with only mX and mY, and without mX and mY
        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Mar2_only_mXmY")'`
        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Mar2_without_mXmY")'`
        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Mar2_only_mXmY_VR")'`
        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Mar2_without_mXmY_VR")'`
	  for Full BDT, with TTBAR, and data - now edited to swap out TTBAR directory as well (only for Validation region)
        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Mar17_fullBDT_TTBAR_MassWindow_data")'`
        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Mar17_fullBDT_TTBAR_MassWindow_data_VR")'`
	  for Full BDT, with TTBAR, and data - now edited to swap out TTBAR directory as well (only for Validation region)
        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Apr6_fullBDT_MassWindow", "2022Apr6/")'`
        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Apr6_fullBDT_MassWindow_VR", "2022Apr6/")'`
        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Apr7_fullBDT_MassWindow_2xErr", "2022Apr7/")'`
        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Apr7_fullBDT_MassWindow_2xErr_VR", "2022Apr7/")'`
        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Apr7_fullBDT_MassWindow_5xErr", "2022Apr7/")'`
        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Apr7_fullBDT_MassWindow_5xErr_VR", "2022Apr7/")'`
        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Apr7_fullBDT_MassWindow_10xErr", "2022Apr7/")'`
        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Apr7_fullBDT_MassWindow_10xErr_VR", "2022Apr7/")'`
	- for BDT systematics tests 
		- nominal BDT training
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_NomBDTtoFullVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_NomBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_NomBDTtoInVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_NomBDTtoInVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_NomBDTtoOutVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_NomBDTtoOutVR_VR", "BDTsyst_2022Apr/")'`
		- Quarters of CR for BDT trainin
			---
	        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_OutQtrBDTtoOutQtr_OutVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_OutQtrBDTtoOutQtr_OutVR_VR", "BDTsyst_2022Apr/")'`
			---
	        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_OutQtrBDTtoInQtr_InVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_OutQtrBDTtoInQtr_InVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_InQtrBDTtoOutQtr_OutVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_InQtrBDTtoOutQtr_OutVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_InQtrBDTtoInQtr_InVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_InQtrBDTtoInQtr_InVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_InQtrBDTtoFullVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_InQtrBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_OutQtrBDTtoFullVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_OutQtrBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			--- --- ---
			--- --- ---
		- Halfs of CR for BDT training
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_OutBDTtoOutCR_OutVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_OutBDTtoOutCR_OutVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_OutBDTtoInCR_InVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_OutBDTtoInCR_InVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_InBDTtoOutCR_OutVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_InBDTtoOutCR_OutVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_InBDTtoInCR_InVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_InBDTtoInCR_InVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_OutBDTtoFullVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_OutBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			---
			`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun16_InBDTtoFullVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun16_InBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
		- bTagScore
	        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun21_Nom_FullCRtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun21_Nom_FullCRtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun23_Nom_bJetScoreLoose_OutBDTtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun23_Nom_bJetScoreLoose_OutBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jun23_Nom_bJetScoreLoose_InBDTtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jun23_Nom_bJetScoreLoose_InBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf_VR", "BDTsyst_2022Apr/")'`
	- for full submission:
		`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jul7_fullBDT_bJetScoreLoose", "fullSubmission_2022July//")'`
		`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jul7_fullBDT_bJetScoreLoose_VR", "fullSubmission_2022July//")'`
		
		`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jul14_fullBDT_bJetScore1p5", "fullSubmission_2022July/")'`
		`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jul14_fullBDT_bJetScore1p5_VR", "fullSubmission_2022July/")'`
		
		`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Aug1_fullBDT_bJetLoose_CutLowMx", "fullSubmission_2022July/")'`
		`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Aug1_fullBDT_bJetLoose_CutLowMx_VR", "fullSubmission_2022July/")'`
		!! ONLY modifying mass group 0 now
		`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Aug30_fullBDT_bJetLoose_CutLowMx280", "fullSubmission_2022July/")'`
		`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Aug30_fullBDT_bJetLoose_CutLowMx280_VR", "fullSubmission_2022July/")'`
		!! ONLY modifying mass group 0 now
		`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Sep14_Mx300_bJetLoose_3", "fullSubmission_2022July/")'`
		`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Sep14_Mx300_bJetLoose_3_VR", "fullSubmission_2022July/")'`
		!! ONLY modifying mass group 0 now
		`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Sep14_Mx300_bJetLoose_mx280cut", "fullSubmission_2022July/")'`
		`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Sep14_Mx300_bJetLoose_mx280cut_VR", "fullSubmission_2022July/")'`
		!! ONLY modifying mass group 0 now
		`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Sep14_Mx300_bJetLoose_depth4_leafs50_3", "fullSubmission_2022July/")'`
		`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Sep14_Mx300_bJetLoose_depth4_leafs50_3_VR", "fullSubmission_2022July/")'`
		!! ONLY modifying mass group 0 now
		`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Sep14_Mx300_bJetLoose_depth2_leafs50", "fullSubmission_2022July/")'`
		`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Sep14_Mx300_bJetLoose_depth2_leafs50_VR", "fullSubmission_2022July/")'`
		!! ONLY modifying mass group 0 now
		`root -l -q './scripts/modifyAllPlotForControlTest.C("2022Jul7_fullBDT_bJetScoreLoose_mx300unrollForPlotting", "fullSubmission_2022July/")'`
		`root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Jul7_fullBDT_bJetScoreLoose_mx300unrollForPlotting_VR", "fullSubmission_2022July/")'`
	- Validation Region training:
		- all mass groups
		- `root -l -q './scripts/modifyAllPlotForControlTest.C("2022Oct25_ValRegTrain_bJetLoose", "fullSubmission_2022July/")'`
		- `root -l -q './scripts/modifyAllPlotForValidationTest.C("2022Oct25_ValRegTrain_bJetLoose_VR", "fullSubmission_2022July/")'`

- removed the 'up' 'down' behavior for the CR test <span style="color:green">don't remove anymore (when running with the up and down - previous step)</span>
- need to edit the folder name
- Result of this code (in the root file): 
	- *replacing* 
		data_BTagCSV/selectionbJets_**SignalRegion**/data_BTagCSV_selectionbJets_SignalRegion_HH_kinFit_m_H2_m_Rebinned_Unrolled
		*with*
	   data_BTagCSV/selectionbJets_**ControlRegionBlinded**/data_BTagCSV_selectionbJets_ControlRegionBlinded_HH_kinFit_m_H2_m_Rebinned_Unrolled 
	- *and also replacing* 
	    data_BTagCSV_dataDriven_kinFit/selectionbJets_**SignalRegion**/data_BTagCSV_dataDriven_kinFit_selectionbJets_SignalRegion_HH_kinFit_m_H2_m_Rebinned_Unrolled
	    *with*
	    data_BTagCSV_dataDriven_kinFit/selectionbJets_**ControlRegionBlinded**/data_BTagCSV_dataDriven_kinFit_selectionbJets_ControlRegionBlinded_HH_kinFit_m_H2_m_Rebinned_Unrolled 
- code: `scripts/UnrollAllSubdirControlTest.sh`
- and `scripts/Unroll2DplotsSubRangeControlTest.cc` 
Note - do Validation unroll first, then copy the output massGroup* files to a directory with VR in the name, then run the CR unroll
- run code with:
	- `source ./scripts/UnrollAllSubdirControlTest.sh 2016`
	- `source ./scripts/UnrollAllSubdirControlTest.sh 2017`
	- `source ./scripts/UnrollAllSubdirControlTest.sh 2018`
- For Validation set:
	- copied the outPlotter.root files from the CR directories into the VR directories
		- The VR outPlotter is now in `DataPlots_fullSubmission_2016_v34_aidan_2022Jan26_VR_mx600_my400`
		- CR directies like: `DataPlots_fullSubmission_2016_v34_aidan_2022Jan26`, `jobsFill_fullSubmission_2016_v34_aidan_rebinnned_2021Dec23`
		- VR directoiries like: `DataPlots_fullSubmission_2016_v34_aidan_2022Jan26_VR`, `DataPlots_fullSubmission_2016_v34_aidan_rebinnned_2021Dec23_VR`
		- The outPlotter.root file for the normal binning is copied from the dirs: `DataPlots_fullSubmission_2016_v34_aidan_2021Dec21` 
			- outPlotter.root is the same for CR and VR (normal binning)
	- run code with: `source ./scripts/UnrollAllSubdirValidationTest.sh 2016`
	- run code with: `source ./scripts/UnrollAllSubdirValidationTest.sh 2017`
	- run code with: `source ./scripts/UnrollAllSubdirValidationTest.sh 2018`
- now run like:
 - Control Region: 
 - `source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr6/2016 2022Apr6_fullBDT_MassWindow`
 - `source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr6/2017 2022Apr6_fullBDT_MassWindow`
 - `source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr6/2018 2022Apr6_fullBDT_MassWindow`
 - Validation
 - `source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr6/2016 2022Apr6_fullBDT_MassWindow`
 - `source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr6/2017 2022Apr6_fullBDT_MassWindow`
 - `source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr6/2018 2022Apr6_fullBDT_MassWindow`
 - for 2x, 5x and 10x Errors:
		`cp -r 2022Apr6/2016DataPlots_2022Apr6_fullBDT_MassWindow 2022Apr7/2016DataPlots_2022Apr7_fullBDT_MassWindow_2xErr`
		`cp -r 2022Apr6/2017DataPlots_2022Apr6_fullBDT_MassWindow 2022Apr7/2017DataPlots_2022Apr7_fullBDT_MassWindow_2xErr`
		`cp -r 2022Apr6/2018DataPlots_2022Apr6_fullBDT_MassWindow 2022Apr7/2018DataPlots_2022Apr7_fullBDT_MassWindow_2xErr`

		`source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr7/2016 2022Apr7_fullBDT_MassWindow_2xErr`
		`source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr7/2017 2022Apr7_fullBDT_MassWindow_2xErr`
		`source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr7/2018 2022Apr7_fullBDT_MassWindow_2xErr`
		
		`mkdir 2016DataPlots_2022Apr7_fullBDT_MassWindow_2xErr_VR`
		`mkdir 2017DataPlots_2022Apr7_fullBDT_MassWindow_2xErr_VR`
		`mkdir 2018DataPlots_2022Apr7_fullBDT_MassWindow_2xErr_VR`
		
		`mv 2016DataPlots_2022Apr7_fullBDT_MassWindow_2xErr/*massGroup* 2016DataPlots_2022Apr7_fullBDT_MassWindow_2xErr_VR`
		`mv 2017DataPlots_2022Apr7_fullBDT_MassWindow_2xErr/*massGroup* 2017DataPlots_2022Apr7_fullBDT_MassWindow_2xErr_VR`
		`mv 2018DataPlots_2022Apr7_fullBDT_MassWindow_2xErr/*massGroup* 2018DataPlots_2022Apr7_fullBDT_MassWindow_2xErr_VR`
		
		`source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr7/2016 2022Apr7_fullBDT_MassWindow_2xErr`
		`source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr7/2017 2022Apr7_fullBDT_MassWindow_2xErr`
		`source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr7/2018 2022Apr7_fullBDT_MassWindow_2xErr`
		
		##################################################
		`cp -r 2022Apr6/2016DataPlots_2022Apr6_fullBDT_MassWindow 2022Apr7/2016DataPlots_2022Apr7_fullBDT_MassWindow_5xErr`
		`cp -r 2022Apr6/2017DataPlots_2022Apr6_fullBDT_MassWindow 2022Apr7/2017DataPlots_2022Apr7_fullBDT_MassWindow_5xErr`
		`cp -r 2022Apr6/2018DataPlots_2022Apr6_fullBDT_MassWindow 2022Apr7/2018DataPlots_2022Apr7_fullBDT_MassWindow_5xErr`
		
		`source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr7/2016 2022Apr7_fullBDT_MassWindow_5xErr`
		`source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr7/2017 2022Apr7_fullBDT_MassWindow_5xErr`
		`source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr7/2018 2022Apr7_fullBDT_MassWindow_5xErr`
		
		`mkdir 2016DataPlots_2022Apr7_fullBDT_MassWindow_5xErr_VR`
		`mkdir 2017DataPlots_2022Apr7_fullBDT_MassWindow_5xErr_VR`
		`mkdir 2018DataPlots_2022Apr7_fullBDT_MassWindow_5xErr_VR`
		
		`mv 2016DataPlots_2022Apr7_fullBDT_MassWindow_5xErr/*massGroup* 2016DataPlots_2022Apr7_fullBDT_MassWindow_5xErr_VR`
		`mv 2017DataPlots_2022Apr7_fullBDT_MassWindow_5xErr/*massGroup* 2017DataPlots_2022Apr7_fullBDT_MassWindow_5xErr_VR`
		`mv 2018DataPlots_2022Apr7_fullBDT_MassWindow_5xErr/*massGroup* 2018DataPlots_2022Apr7_fullBDT_MassWindow_5xErr_VR`
		
		`source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr7/2016 2022Apr7_fullBDT_MassWindow_5xErr`
		`source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr7/2017 2022Apr7_fullBDT_MassWindow_5xErr`
		`source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr7/2018 2022Apr7_fullBDT_MassWindow_5xErr`
		
		##################################################
		`cp -r 2022Apr6/2016DataPlots_2022Apr6_fullBDT_MassWindow 2022Apr7/2016DataPlots_2022Apr7_fullBDT_MassWindow_10xErr`
		`cp -r 2022Apr6/2017DataPlots_2022Apr6_fullBDT_MassWindow 2022Apr7/2017DataPlots_2022Apr7_fullBDT_MassWindow_10xErr`
		`cp -r 2022Apr6/2018DataPlots_2022Apr6_fullBDT_MassWindow 2022Apr7/2018DataPlots_2022Apr7_fullBDT_MassWindow_10xErr`
		
		`source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr7/2016 2022Apr7_fullBDT_MassWindow_10xErr`
		`source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr7/2017 2022Apr7_fullBDT_MassWindow_10xErr`
		`source ./scripts/UnrollAllSubdirValidationTest.sh 2022Apr7/2018 2022Apr7_fullBDT_MassWindow_10xErr`
		
		`mkdir 2016DataPlots_2022Apr7_fullBDT_MassWindow_10xErr_VR`
		`mkdir 2017DataPlots_2022Apr7_fullBDT_MassWindow_10xErr_VR`
		`mkdir 2018DataPlots_2022Apr7_fullBDT_MassWindow_10xErr_VR`
		
		`mv 2016DataPlots_2022Apr7_fullBDT_MassWindow_10xErr/*massGroup* 2016DataPlots_2022Apr7_fullBDT_MassWindow_10xErr_VR`
		`mv 2017DataPlots_2022Apr7_fullBDT_MassWindow_10xErr/*massGroup* 2017DataPlots_2022Apr7_fullBDT_MassWindow_10xErr_VR`
		`mv 2018DataPlots_2022Apr7_fullBDT_MassWindow_10xErr/*massGroup* 2018DataPlots_2022Apr7_fullBDT_MassWindow_10xErr_VR`
		
		`source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr7/2016 2022Apr7_fullBDT_MassWindow_10xErr`
		`source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr7/2017 2022Apr7_fullBDT_MassWindow_10xErr`
		`source ./scripts/UnrollAllSubdirControlTest.sh 2022Apr7/2018 2022Apr7_fullBDT_MassWindow_10xErr`
- BDT systematics
	- **had to comment out the \_down and \_up parts for the code to work (didn't keep functionality in the fill step for only BDT somehow ...?)**
		- line 404 to 417
	- seeds 1020 and 2020 
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2016 2022Apr11_seed1020`
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2017 2022Apr11_seed1020`
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2018 2022Apr11_seed1020`
		- `mv 2016DataPlots_2022Apr11_seed1020/outPlotter_massGroup* 2016DataPlots_2022Apr11_seed1020_VR`
		- `mv 2017DataPlots_2022Apr11_seed1020/outPlotter_massGroup* 2017DataPlots_2022Apr11_seed1020_VR`
		- `mv 2018DataPlots_2022Apr11_seed1020/outPlotter_massGroup* 2018DataPlots_2022Apr11_seed1020_VR`
		 
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2016 2022Apr11_seed1020`
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2017 2022Apr11_seed1020`
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2018 2022Apr11_seed1020`
		
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2016 2022Apr11_seed2020`
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2017 2022Apr11_seed2020`
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2018 2022Apr11_seed2020`
		- `mv 2016DataPlots_2022Apr11_seed2020/outPlotter_massGroup* 2016DataPlots_2022Apr11_seed2020_VR`
		- `mv 2017DataPlots_2022Apr11_seed2020/outPlotter_massGroup* 2017DataPlots_2022Apr11_seed2020_VR`
		- `mv 2018DataPlots_2022Apr11_seed2020/outPlotter_massGroup* 2018DataPlots_2022Apr11_seed2020_VR`
		
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2016 2022Apr11_seed2020`
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2017 2022Apr11_seed2020`
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2018 2022Apr11_seed2020`
	- for left and right side study:
		- `mkdir VarPlots/rootHists/BDTsyst_2022Apr/2016DataPlots_2022May5_RightSide_VR`
		- `mkdir VarPlots/rootHists/BDTsyst_2022Apr/2017DataPlots_2022May5_RightSide_VR`
		- `mkdir VarPlots/rootHists/BDTsyst_2022Apr/2018DataPlots_2022May5_RightSide_VR`
		- `mkdir VarPlots/rootHists/BDTsyst_2022Apr/2018DataPlots_2022May5_LeftSide_VR`
		- `mkdir VarPlots/rootHists/BDTsyst_2022Apr/2017DataPlots_2022May5_LeftSide_VR`
		- `mkdir VarPlots/rootHists/BDTsyst_2022Apr/2016DataPlots_2022May5_LeftSide_VR`
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2016 2022May5_RightSide`
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2017 2022May5_RightSide`
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2018 2022May5_RightSide`
		- `mv 2016DataPlots_2022May5_RightSide/outPlotter_massGroup* 2016DataPlots_2022May5_RightSide_VR`
		- `mv 2016DataPlots_2022May5_RightSide/outPlotter_massGroup* 2016DataPlots_2022May5_RightSide_VR`
		- `mv 2016DataPlots_2022May5_RightSide/outPlotter_massGroup* 2016DataPlots_2022May5_RightSide_VR`
		
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2016 2022May5_LeftSide`
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2017 2022May5_LeftSide`
		- `source ./scripts/UnrollAllSubdirValidationTest.sh BDTsyst_2022Apr/2018 2022May5_LeftSide`
		- `mv 2016DataPlots_2022May5_LeftSide/outPlotter_massGroup* 2016DataPlots_2022May5_LeftSide_VR`
		- `mv 2016DataPlots_2022May5_LeftSide/outPlotter_massGroup* 2016DataPlots_2022May5_LeftSide_VR`
		- `mv 2016DataPlots_2022May5_LeftSide/outPlotter_massGroup* 2016DataPlots_2022May5_LeftSide_VR`
		
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2016 2022May5_RightSide`
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2017 2022May5_RightSide`
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2018 2022May5_RightSide`
		
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2016 2022May5_LeftSide`
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2017 2022May5_LeftSide`
		- `source ./scripts/UnrollAllSubdirControlTest.sh BDTsyst_2022Apr/2018 2022May5_LeftSide`
- for inner and outer halfs of the CR:
	- now using script: `unrollCRandVR.sh`
		do not run them simultaneously!  - recompiling the code ...
		`source ./unrollCRandVR.sh 2022May19_OutBDTtoOutCR`
		`source ./unrollCRandVR.sh 2022May19_OutBDTtoInCR`
		`source ./unrollCRandVR.sh 2022May19_InBDTtoOutCR`
		`source ./unrollCRandVR.sh 2022May19_InBDTtoInCR`
		`source ./unrollCRandVR.sh 2022May24_ExcRightOutBDT`
		`source ./unrollCRandVR.sh 2022May24_ExcLeftOutBDT`
		`source ./unrollCRandVR.sh 2022Apr11_seed2020_InVR`
		`source ./unrollCRandVR.sh 2022Apr11_seed2020_OutVR`
		
		`source ./unrollCRandVR.sh 2022Jun16_NomBDTtoFullVR`
		`source ./unrollCRandVR.sh 2022Jun16_NomBDTtoInVR`
		`source ./unrollCRandVR.sh 2022Jun16_NomBDTtoOutVR`
		
		`source ./unrollCRandVR.sh 2022Jun16_OutQtrBDTtoOutQtr_OutVR`
		`source ./unrollCRandVR.sh 2022Jun16_OutQtrBDTtoInQtr_InVR`
		`source ./unrollCRandVR.sh 2022Jun16_InQtrBDTtoOutQtr_OutVR`
		`source ./unrollCRandVR.sh 2022Jun16_InQtrBDTtoInQtr_InVR`
		`source ./unrollCRandVR.sh 2022Jun16_InQtrBDTtoFullVR`
		`source ./unrollCRandVR.sh 2022Jun16_OutQtrBDTtoFullVR`
 
		`source ./unrollCRandVR.sh 2022Jun16_OutBDTtoOutCR_OutVR`
		`source ./unrollCRandVR.sh 2022Jun16_OutBDTtoInCR_InVR`
		`source ./unrollCRandVR.sh 2022Jun16_InBDTtoOutCR_OutVR`
		`source ./unrollCRandVR.sh 2022Jun16_InBDTtoInCR_InVR`
		`source ./unrollCRandVR.sh 2022Jun16_OutBDTtoFullVR`
		`source ./unrollCRandVR.sh 2022Jun16_InBDTtoFullVR`
- unroll BDT with btag score requirements set to loose
		`source ./unrollCRandVR.sh 2022Jun21_Nom_FullCRtoFullVR`
		`source ./unrollCRandVR.sh 2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR`
		`source ./unrollCRandVR.sh 2022Jun23_Nom_bJetScoreLoose_OutBDTtoFullVR`
		`source ./unrollCRandVR.sh 2022Jun23_Nom_bJetScoreLoose_InBDTtoFullVR`
	- use inner and outer half for Up and Down variations
		`source ./unrollCRandVR.sh 2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf`
- unroll full submissions BDT
	- there was a Mass Window Cut in `scripts/Unroll2DplotsSubRangeControlTest.cc` and `scripts/Unroll2DplotsSubRangeValidationTest.cc`
	make sure to rename the full submission output first (with `renameFullSubmissions.sh`)
	should make this better. Each unrolling takes 10 min. 5 mass groups of unrolled plots fro each year and for CR and VR. 5x3x2=30x10min=300min=5 hrs
	`source ./unrollCRandVR.sh 2022Jul7_fullBDT_bJetScoreLoose`
	`source ./unrollCRandVR_byYear.sh 2022Jul7_fullBDT_bJetScoreLoose 2016`
	`source ./unrollCRandVR_byYear.sh 2022Jul7_fullBDT_bJetScoreLoose 2017`
	`source ./unrollCRandVR_byYear.sh 2022Jul7_fullBDT_bJetScoreLoose 2018`
	
	`source ./unrollCRandVR_byYear.sh 2022Jul14_fullBDT_bJetScore1p5 2016`
	`source ./unrollCRandVR_byYear.sh 2022Jul14_fullBDT_bJetScore1p5 2017`
	`source ./unrollCRandVR_byYear.sh 2022Jul14_fullBDT_bJetScore1p5 2018`
	
	`source ./unrollCRandVR_byYear.sh 2022Aug1_fullBDT_bJetLoose_CutLowMx 2016`
	`source ./unrollCRandVR_byYear.sh 2022Aug1_fullBDT_bJetLoose_CutLowMx 2017`
	`source ./unrollCRandVR_byYear.sh 2022Aug1_fullBDT_bJetLoose_CutLowMx 2018`
	
	`source ./unrollCRandVR_byYear.sh 2022Aug4_MassGroup0_bJetLoose 2016`
	`source ./unrollCRandVR_byYear.sh 2022Aug4_MassGroup0_bJetLoose 2017`
	`source ./unrollCRandVR_byYear.sh 2022Aug4_MassGroup0_bJetLoose 2018`
	
	`source ./unrollCRandVR_byYear.sh 2022Aug30_fullBDT_bJetLoose_CutLowMx280 2016`
	`source ./unrollCRandVR_byYear.sh 2022Aug30_fullBDT_bJetLoose_CutLowMx280 2017`
	`source ./unrollCRandVR_byYear.sh 2022Aug30_fullBDT_bJetLoose_CutLowMx280 2018`
	
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_3 2016`
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_3 2017`
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_3 2018`
	
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_mx280cut 2016`
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_mx280cut 2017`
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_mx280cut 2018`
	
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_depth4_leafs50_3 2016`
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_depth4_leafs50_3 2017`
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_depth4_leafs50_3 2018`
	
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_depth2_leafs50 2016`
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_depth2_leafs50 2017`
	`source ./unrollCRandVR_byYear.sh 2022Sep14_Mx300_bJetLoose_depth2_leafs50 2018`

	copied the full outplotter.root files for this special unrolling (only for plotting)
	`source ./unrollCRandVR_byYear.sh 2022Jul7_fullBDT_bJetScoreLoose_mx300unrollForPlotting 2016`
	`source ./unrollCRandVR_byYear.sh 2022Jul7_fullBDT_bJetScoreLoose_mx300unrollForPlotting 2017`
	`source ./unrollCRandVR_byYear.sh 2022Jul7_fullBDT_bJetScoreLoose_mx300unrollForPlotting 2018`
- Validation region training:
	- Removed mX slices in validation and control source code (line 61)
	- and included all mass groups (line 311 in these files)
		- `scripts/Unroll2DplotsSubRangeValidationTest.cc`
		- `scripts/Unroll2DplotsSubRangeControlTest.cc`
	- `source ./unrollCRandVR_byYear.sh 2022Oct25_ValRegTrain_bJetLoose 2016`
	- `source ./unrollCRandVR_byYear.sh 2022Oct25_ValRegTrain_bJetLoose 2017`
	- `source ./unrollCRandVR_byYear.sh 2022Oct25_ValRegTrain_bJetLoose 2018`
- Shapes Up and Down:
	- Removed mX slices in validation and control source code (line 61)
	- and included all mass groups (line 311 in these files)
		- `scripts/Unroll2DplotsSubRangeValidationTest.cc`
		- `scripts/Unroll2DplotsSubRangeControlTest.cc`
	- Note: this script unrolls the plots for a VR test also, but this is note used later
	- `source ./unrollCRandVR_byYear.sh 2022Nov14_bJetScoreLoose_shapes2 2016`
	- `source ./unrollCRandVR_byYear.sh 2022Nov14_bJetScoreLoose_shapes2 2017`
	- `source ./unrollCRandVR_byYear.sh 2022Nov14_bJetScoreLoose_shapes2 2018`
	- This was not actually done:
		- `source ./unrollCRandVR_byYear.sh 2022Nov14_bJetScoreLoose_shapes_allVars_selectSigs 2016`
		- `source ./unrollCRandVR_byYear.sh 2022Nov14_bJetScoreLoose_shapes_allVars_selectSigs 2017`
		- `source ./unrollCRandVR_byYear.sh 2022Nov14_bJetScoreLoose_shapes_allVars_selectSigs 2018`
	- Instead use now (includes validation region, the byYear script was better used for control and validation region study):
	- `source ./scripts/UnrollAllSubdir.sh`
Notes:
	- the mass cuts in these scripts on mY are to avoid the triangular regions in the mX vs mY plane 
	Result:
	- <span style="color:green">creates files outplotter_massGroup*.root</span>

### for the up and down variations:
- use scripts/calculateBGKshape.C (need to use the right tag)
- takes the up and down histograms and recomputes them so that "up" is always above the average when "down" is below and vice versa.
    - run with:
        `root -l './scripts/calculateAllBKGshape.C("v34_aidan_2021Dec21")'`
        `root -l './scripts/calculateAllBKGshape.C("v34_aidan_2022Jan26")'`
	for rebinned data run it like:
        `root -l './scripts/calculateAllBKGshape.C("v34_aidan_rebinnned_2021Dec23")'`
	for VR data run it like:
        `root -l './scripts/calculateAllBKGshape.C("v34_aidan_2022Jan26_VR")'`
	for VR rebinned data run it like:
        `root -l './scripts/calculateAllBKGshape.C("v34_aidan_rebinnned_2021Dec23_VR")'`
	- for VR - mass point mX=600, mY=400
	       `root -l './scripts/calculateAllBKGshape.C("v34_aidan_2022Jan26_VR_mx600_my400")'`
	  for BDT training on a smaller mass window, and BDT trained on mass window with ptX var included: 
        `root -l -q './scripts/calculateAllBKGshape.C("2022Feb8_BDTmasscut")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Feb8_BDTmasscut_ptX")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Feb8_BDTmasscut_VR")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Feb8_BDTmasscut_ptX_VR")'`
		2022Feb7_BDTmasscut_ptX
	  for BDT train on a smaller mass window with only mX and mY, and without mX and mY
        `root -l -q './scripts/calculateAllBKGshape.C("2022Mar2_only_mXmY")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Mar2_only_mXmY_VR")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Mar2_without_mXmY")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Mar2_without_mXmY_VR")'`
	  for Full BDT, with TTBAR, and data
        `root -l -q './scripts/calculateAllBKGshape.C("2022Mar17_fullBDT_TTBAR_MassWindow_data")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Mar17_fullBDT_TTBAR_MassWindow_data_VR")'`
		 - for Apr 6 (copied outPlotter.root from the TTBAR full, data)
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr6_fullBDT_MassWindow", "2022Apr6/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr6_fullBDT_MassWindow_VR", "2022Apr6/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr6_fullBDT_MassWindow_2xErr", "2022Apr6/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr6_fullBDT_MassWindow_2xErr_VR", "2022Apr6/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr6_fullBDT_MassWindow_5xErr", "2022Apr6/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr6_fullBDT_MassWindow_5xErr_VR", "2022Apr6/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr6_fullBDT_MassWindow_10xErr", "2022Apr6/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr6_fullBDT_MassWindow_10xErr_VR", "2022Apr6/")'`
		 - for Apr 7 - changed the 3b bkg errors only
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr7_fullBDT_MassWindow_2xErr", "2022Apr7/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr7_fullBDT_MassWindow_2xErr_VR", "2022Apr7/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr7_fullBDT_MassWindow_5xErr", "2022Apr7/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr7_fullBDT_MassWindow_5xErr_VR", "2022Apr7/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr7_fullBDT_MassWindow_10xErr", "2022Apr7/")'`
        `root -l -q './scripts/calculateAllBKGshape.C("2022Apr7_fullBDT_MassWindow_10xErr_VR", "2022Apr7/")'`
		- For BDT systematics
		`2022May19_OutBDTtoOutCR`
		`2022May19_OutBDTtoInCR`
		`2022May19_InBDTtoOutCR`
		`2022May19_InBDTtoInCR`
		`2022May24_ExcRightOutBDT`
		`2022May24_ExcLeftOutBDT`
		`2022Apr11_seed2020_InVR`
		`2022Apr11_seed2020_OutVR`
		
		- nominal
			`root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_NomBDTtoFullVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_NomBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
			`root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_NomBDTtoInVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_NomBDTtoInVR_VR", "BDTsyst_2022Apr/")'`
			
			`root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_NomBDTtoOutVR", "BDTsyst_2022Apr/")'`
			`root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_NomBDTtoOutVR_VR", "BDTsyst_2022Apr/")'`
		- Quarters of BDT 
			`2022Jun16_OutQtrBDTtoOutQtr_OutVR`
			`2022Jun16_OutQtrBDTtoInQtr_InVR`
			`2022Jun16_InQtrBDTtoOutQtr_OutVR`
			`2022Jun16_InQtrBDTtoInQtr_InVR`
			`2022Jun16_InQtrBDTtoFullVR`
			`2022Jun16_OutQtrBDTtoFullVR`
			--
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutQtrBDTtoOutQtr_OutVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutQtrBDTtoOutQtr_OutVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutQtrBDTtoInQtr_InVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutQtrBDTtoInQtr_InVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InQtrBDTtoOutQtr_OutVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InQtrBDTtoOutQtr_Out_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InQtrBDTtoInQtr_InVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InQtrBDTtoInQtr_InVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InQtrBDTtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InQtrBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutQtrBDTtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutQtrBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			--
		- halfs of BDT
			`2022Jun16_OutBDTtoOutCR_OutVR`
			`2022Jun16_OutBDTtoInCR_InVR`
			`2022Jun16_InBDTtoOutCR_OutVR`
			`2022Jun16_InBDTtoInCR_InVR`
			`2022Jun16_OutBDTtoFullVR`
			`2022Jun16_InBDTtoFullVR`
			--
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutBDTtoOutCR_OutVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutBDTtoOutCR_OutVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutBDTtoInCR_InVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutBDTtoInCR_InVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InBDTtoOutCR_OutVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InBDTtoOutCR_OutVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InBDTtoInCR_InVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InBDTtoInCR_InVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutBDTtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_OutBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InBDTtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun16_InBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
		- bTagScore
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun21_Nom_FullCRtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun21_Nom_FullCRtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun23_Nom_bJetScoreLoose_OutBDTtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun23_Nom_bJetScoreLoose_OutBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun23_Nom_bJetScoreLoose_InBDTtoFullVR", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jun23_Nom_bJetScoreLoose_InBDTtoFullVR_VR", "BDTsyst_2022Apr/")'`
			
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf", "BDTsyst_2022Apr/")'`
	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf_VR", "BDTsyst_2022Apr/")'`
	- Full BDT submission with bJet selections:
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jul7_fullBDT_bJetScoreLoose", "fullSubmission_2022July/")'`
 	         `root -l -q './scripts/calculateAllBKGshape.C("2022Jul7_fullBDT_bJetScoreLoose_VR", "fullSubmission_2022July/")'`
			 ---
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jul14_fullBDT_bJetScore1p5", "fullSubmission_2022July/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jul14_fullBDT_bJetScore1p5_VR", "fullSubmission_2022July/")'`
			 ---
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Aug1_fullBDT_bJetLoose_CutLowMx", "fullSubmission_2022July/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Aug1_fullBDT_bJetLoose_CutLowMx_VR", "fullSubmission_2022July/")'`
			 ---
			 !! ONLY looking at Mass Group 0 now
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Aug30_fullBDT_bJetLoose_CutLowMx280", "fullSubmission_2022July/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Aug30_fullBDT_bJetLoose_CutLowMx280_VR", "fullSubmission_2022July/")'`
			 !! ONLY looking at Mass Group 0 now
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Sep14_Mx300_bJetLoose_3", "fullSubmission_2022July/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Sep14_Mx300_bJetLoose_3_VR", "fullSubmission_2022July/")'`
			 !! ONLY looking at Mass Group 0 now
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Sep14_Mx300_bJetLoose_mx280cut", "fullSubmission_2022July/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Sep14_Mx300_bJetLoose_mx280cut_VR", "fullSubmission_2022July/")'`
			 !! ONLY looking at Mass Group 0 now
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Sep14_Mx300_bJetLoose_depth4_leafs50_3", "fullSubmission_2022July/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Sep14_Mx300_bJetLoose_depth4_leafs50_3_VR", "fullSubmission_2022July/")'`
			 !! ONLY looking at Mass Group 0 now
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Sep14_Mx300_bJetLoose_depth2_leafs50", "fullSubmission_2022July/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Sep14_Mx300_bJetLoose_depth2_leafs50_VR", "fullSubmission_2022July/")'`
			 !! ONLY looking at Mass Group 0 now
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jul7_fullBDT_bJetScoreLoose_mx300unrollForPlotting", "fullSubmission_2022July/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Jul7_fullBDT_bJetScoreLoose_mx300unrollForPlotting_VR", "fullSubmission_2022July/")'`
	- Validation region training
		- all mass groups
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Oct25_ValRegTrain_bJetLoose", "fullSubmission_2022July/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Oct25_ValRegTrain_bJetLoose_VR", "fullSubmission_2022July/")'`
	- Shapes UP and DOWN
		- all mass groups
 	        `root -l -q './scripts/calculateAllBKGshape.C("2022Nov14_bJetScoreLoose_shapes2", "fullSubmission_2022Nov/")'`
 	        `root -l -q './scripts/calculateAllBKGshape.C("2023Feb28", "fullSubmission_2022Nov/")'`
### Make plots
	- `plotVars_2022Feb.py`
	- `plotUnrolledVars_2022July.py`
- renamed the main functions from Fabios files to match the file names here, other functions may be available though:
		`root -l -b scripts/privateScript/StackPlots.C`
		`root -l -b privateTools/RatioPlot.C`
```
.L scripts/MeasureBackgroundSystematic.C++
doMeasureNorm("2022Nov14_bJetScoreLoose_shapes2", 2016)
```
## run the limits with Combine:
- code: nobackup/DiHiggs_v2/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/limits/prepareModels/SubmitFullRunIILimits.py
    `python prepareModels/SubmitFullRunIILimits.py --tag <tag_name> --year RunII --group auto --unblind`
    - replace `directory` in the config files (one config for each year): limits/prepareModels/config/LimitsConfig_2016.cfg
        - *option folder has fravera name...? this is the output folder for when you run the script locally (ie without condor)*
	- edit `listOfSamples.txt` for which mass points to run
	- replace the `<tag_name>`
		- initial tests 
	        `python prepareModels/SubmitFullRunIILimits.py --tag aidan_2021Dec15 --year RunII --group auto --unblind`
		- run the control region (but probably the mass window was not correct with I ran it) 
	        `python prepareModels/SubmitFullRunIILimits.py --tag aidan_all_2021Dec23 --year RunII --group auto --unblind`
		- run the control region (with the correct mass region)
	        `python prepareModels/SubmitFullRunIILimits.py --tag CR_2022Jan26 --year RunII --group auto --unblind`
		-  run the control region with new bins:
	        `python prepareModels/SubmitFullRunIILimits.py --tag CR_binwidthX2_2022Jan26 --year RunII --group auto --unblind`
		- run the validation region 
	        `python prepareModels/SubmitFullRunIILimits.py --tag VR_2022Jan26 --year RunII --group auto --unblind`
		-  run the validation region with new bins:
	        `python prepareModels/SubmitFullRunIILimits.py --tag VR_binwidthX2_2022Jan26 --year RunII --group auto --unblind`
		-  run the validation region mx=600, mY=400
	        `python prepareModels/SubmitFullRunIILimits.py --tag VR_2022Jan26_mx600_my400 --year RunII --group auto --unblind`
		-  run the validation region mx=600, mY=400 corrected the input directory!
	        `python prepareModels/SubmitFullRunIILimits.py --tag VR_2022Jan26_mx600_my400a --year RunII --group auto --unblind`
		-  run CR BDT trained in a mass window
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Feb8_BDTmasscut_CR --year RunII --group auto --unblind`
		-  run CR BDT trained in a mass window and ptX in BDT
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Feb8_BDTmasscut_ptX_CRa --year RunII --group auto --unblind`
		-  run VR BDT trained in a mass window
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Feb8_BDTmasscut_VR --year RunII --group auto --unblind`
		-  run VR BDT trained in a mass window and ptX in BDT
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Feb8_BDTmasscut_ptX_VR --year RunII --group auto --unblind`
		- BDT, VR and CR, only mX mY and without mX mY
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar2_only_mXmY --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar2_without_mXmY --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar2_only_mXmY_VR --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar2_without_mXmY_VR --year RunII --group auto --unblind`
		- Full BDT, VR and CR, ttbar shape, mass window, and VR with n = 2, and n=5
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar17_fullBDT_TTBAR_MassWindow_data --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar17_fullBDT_TTBAR_MassWindow_data_VR --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar17_fullBDT_TTBAR_MassWindow_data_VR_n2 --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar17_fullBDT_TTBAR_MassWindow_data_VR_n5 --year RunII --group auto --unblind`
		- FullBDT, VR, background adjusted for ttbar
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar17_fullBDT_TTBARasBKG_MassWindow_data_VR --year RunII --group auto --unblind`
		- FullBDT, VR, ttbar shape unc. - corrected the input (modify all validation step)
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar18_fullBDT_MassWindow_ttbarShape_VR --year RunII --group auto --unblind`
		- FullBDT, VR, ttbar as bkg - corrected the input (modify all validation step)
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar18_fullBDT_MassWindow_TTBARasBKG_VR --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar18_fullBDT_MassWindow_TTBARasBKG_VR_2 --year RunII --group auto --unblind`
		- FullBDT, no ttbar 
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar18_fullBDT_MassWindow_noTTBAR --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar18_fullBDT_MassWindow_noTTBAR_VR --year RunII --group auto --unblind`
		- FullBDT, no ttbar - reordered bins
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar24_binsReordered --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar24_binsReordered_VR --year RunII --group auto --unblind`
		- FullBDT, no ttbar - reordered bins, with systematics
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar25_binsReordered2 --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Mar25_binsReordered_VR --year RunII --group auto --unblind`
		- FullBDT, bJets selections
			- added freeze BKG normalization option in SubmitFullRunIILimits - should appear in the output root file graphs as a folder...
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022July7_fullBDT_bJetScoreLoose --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022July7_fullBDT_bJetScoreLoose_VR --year RunII --group auto --unblind`
			
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022July11_fullBDT_bJetScoreLoose --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022July11_fullBDT_bJetScoreLoose_VR --year RunII --group auto --unblind`

			- run from the limits directory - using the goTo_Limits2 alias setup after logging in to LPC
			- !!! need to edit (1) `directory` in the LimitConfig files for CR or VR (`folder` doesn't matter), (2) sample list to run all mass points, and (3) the tag in the command, controlling the output folder name
			- it is setup to run statOnly, syst, and freezeBKGnorm options in one go - this is a little annoying to handle in the (next) plotting step - the plotting step could be edited.
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022July13_fullBDT_bJetScoreLoose --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022July13_fullBDT_bJetScoreLoose_VR --year RunII --group auto --unblind`
			
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022July15_fullBDT_bJetScore1p5 --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022July15_fullBDT_bJetScore1p5_VR --year RunII --group auto --unblind`
			
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Aug1_fullBDT_bJetLoose_CutLowMx --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Aug1_fullBDT_bJetLoose_CutLowMx_VR --year RunII --group auto --unblind`
		 
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Aug30_fullBDT_bJetLoose_CutLowMx280 --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Aug30_fullBDT_bJetLoose_CutLowMx280_VR --year RunII --group auto --unblind`
		
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Aug30_fullBDT_bJetLoose_CutLowMx280_rmax20 --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Aug30_fullBDT_bJetLoose_CutLowMx280_rmax20_VR --year RunII --group auto --unblind`
		
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_2_rmax30 --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_2_VR_rmax30_2 --year RunII --group auto --unblind`
			-- first VR (`_2`) was submitted with the CR directory in the config file, there is a no `_rmax` tag that was run, but I canceled the jobs
		
			- run from the limits directory - using the goTo_Limits2 alias setup after logging in to LPC
			- !!! need to edit (1) `directory` in the LimitConfig files for CR or VR (`folder` doesn't matter), (2) sample list to run all mass points, and (3) the tag in the command, controlling the output folder name
			- it is setup to run statOnly, syst, and freezeBKGnorm options in one go - this is a little annoying to handle in the (next) plotting step - the plotting step could be edited.
			
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_3_rmax30_unrollcut --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_3_VR_rmax30_unrollcut  --year RunII --group auto --unblind`
			
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_3_rmax20 --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_3_VR_rmax20 --year RunII --group auto --unblind`
		
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_3_rmax5 --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_3_VR_rmax5 --year RunII --group auto --unblind`
			
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_mx280cut_rmax30_unrollcut --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_mx280cut_VR_rmax30_unrollcut  --year RunII --group auto --unblind`
			
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_depth4_leafs50_3_rmax30_unrollcut --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_depth4_leafs50_3_VR_rmax30_unrollcut  --year RunII --group auto --unblind`
			
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_depth2_leafs50_rmax30_unrollcut --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Mx300_bJetLoose_depth2_leafs50_VR_rmax30_unrollcut  --year RunII --group auto --unblind`
		- add scaling of the signal
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Oct19_Mx300_bJetLoose_3_VR_rmax30_unrollcut_addScaleSig  --year RunII --group auto --unblind`
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Oct19_Mx300_bJetLoose_3_VR_rmax30_unrollcut_noScaleSig  --year RunII --group auto --unblind`
			myScaleSig_2 for correctly adding signal process name in makeDatacardsandWorkspaces.py
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Oct19_Mx300_bJetLoose_3_VR_rmax30_unrollcut_myScaleSig_2  --year RunII --group auto --unblind`
			
	        `python prepareModels/SubmitFullRunIILimits.py --tag 2022Sep14_Oct19_Mx300_bJetLoose_3_VR_rmax30_unrollcut_myScaleSig_0p1  --year RunII --group auto --unblind`
		
			- run from the limits directory - using the goTo_Limits2 alias setup after logging in to LPC
			- !!! need to edit (1) `directory` in the LimitConfig files for CR or VR (`folder` doesn't matter), (2) sample list to run all mass points, and (3) the tag in the command, controlling the output folder name
			- it is setup to run statOnly, syst, and freezeBKGnorm options in one go - this is a little annoying to handle in the (next) plotting step - the plotting step could be edited.
		- Validation Region BDT Training
			- run from the limits directory - using the goTo_Limits2 alias setup after logging in to LPC
			- !!! need to edit (1) `directory` in the LimitConfig files for CR or VR (`folder` doesn't matter), (2) sample list to run all mass points, and (3) the tag in the command, controlling the output folder name
			- it is setup to run statOnly, syst, and freezeBKGnorm options in one go - this is a little annoying to handle in the (next) plotting step - the plotting step could be edited.
			- Only care about the validation region limits in this test
			- 2 for fixing the scale signal
		    - `python prepareModels/SubmitFullRunIILimits.py --tag 2022Oct25_ValRegTrain_bJetLoose_VR_2  --year RunII --group auto --unblind`
		- Shapes UP and DOWN -- blinded
			- run from the limits directory - using the goTo_Limits2 alias setup after logging in to LPC
			- !!! need to edit (1) `directory` in the LimitConfig (`folder` doesn't matter), (2) sample list to run all mass points, and (3) the tag in the command, controlling the output folder name
				- /uscms/home/agrummer/nobackup/DiHiggs_v2/CMSSW_10_2_5/src/bbbbAnalysis/limits/prepareModels/listOfSamples.txt
			- now running statOnly and syst
				 - possible to also run freezeBKGnorm (commented out in `prepareModels/SubmitFullRunIILimits.py` line 75) - for testing
					- it is setup to run statOnly, syst, and freezeBKGnorm options in one go - this is a little annoying to handle in the (next) plotting step - the plotting step could be edited.
			- 2 for only filling histograms for limit variables: MX, MY, MH, 2D plots
			- added shape back in to config file
			- use correct background norm uncertainties in `prepareModels/SubmitFullRunIILimits.py`
				- taken from background normalization plots, ratio mean
			- now running impacts
			- `python prepareModels/SubmitFullRunIILimits.py --tag 2022Nov22_bJetScoreLoose_shapes2  --year RunII --group auto --impacts`
			- to check jobs use : 
				- `python scripts/getTaskStatus.py -h`
				- `python scripts/getTaskStatus.py --dir CondorJobs/jobsLimits_2022Nov22_bJetScoreLoose_shapes2/ --long`
	- Q - Answered
		**There is a 	`LimitsConfig_2017_all.cfg` and  `LimitsConfig_2018_all.cfg` and I don't know what they do....** - Answer from Fabio - these were for testing
    - list of samples to run: 
        - /uscms/home/agrummer/nobackup/DiHiggs_v2/CMSSW_10_2_5/src/bbbbAnalysis/limits/prepareModels/listOfSamples.txt
### Run Impacts on LXPLUS:
voms-proxy-init --rfc --voms cms -hours 72
cd DiHiggs_v2/CMSSW_10_2_13/
cmsenv
cd src/HiggsAnalysis/CombinedLimit/
source submitAllImpacts2016.sh 
rm -r Impacts2016/Impacts_sig_NMSSM_bbbb_MX_700_MY_300
source submitAllImpacts2016.sh 
condor_q
have to run the impacts on lxplus a total of 4 times - for each sig injection (0 and central limit value) for the combine runs and the plotting
get injection values from: PlotLimitVsMy_orig.py print out (saved in a file, commands in produceAllResults)

seems to fail to get kerberos info forwarded properly -- why??
solved by using kinit

use rsync from hhAnalysisNote folder on mac to copy the impacts down
use pdftk to make a pdf of just the first page
`pdftk impacts400.pdf cat 1 output impacts400_1.pdf`

!!!!! changed the range of r to -30,30 for 2017 mx=1600,300!

### Self Bias Tests
- 
	- PrepareModels/runAllSelfBiasTest.sh
	- the problem here was that the previous process didn't complete before the next one wanted the outputfile. Increased the wait time from 1 sec to 5 seconds.

- Error message Dec 14:
	ERROR: store_cred of Kerberos credential failed - The credmon did not process credentials within the timeout period
	Submitting job(s)Have POIs: ['r']
	condor job script will be condor_Impacts_sig_NMSSM_bbbb_MX_400_MY_80_InitialFit.sh
	condor_submit condor_Impacts_sig_NMSSM_bbbb_MX_400_MY_80_InitialFit.sub
	None
	searching jobs
	Submitting job(s)Have POIs: ['r']
	Not found
	condor job script will be condor_Impacts_sig_NMSSM_bbbb_MX_400_MY_80_InitialFit.sh
	Not found
	condor_submit condor_Impacts_sig_NMSSM_bbbb_MX_400_MY_80_InitialFit.sub
	Not found
- other errors are `permission denied`, maybe related to kerberos ticket:
	- ls: cannot access submitAllImpacts2016.sh: Permission denied
	 - ls: cannot access Impacts2017: Permission denied
	- ls: cannot access Impacts2018: Permission denied
	- ls: cannot access copyPreApprovalInfo.sh: Permission denied
	- ls: cannot access submitAllImpacts2017.sh: Permission denied
	- ls: cannot access submitAllImpacts2018.sh: Permission denied
	- ls: cannot access runImpacts.py: Permission denied
	- ls: cannot access sess.vim: Permission denied

#### Run Combine locally on LPC:
- python prepareModels/prepareHistos.py --config prepareModels/config/LimitsConfig_$1.cfg --signal $n
	`python prepareModels/prepareHistos.py --config prepareModels/config/LimitsConfig_2016.cfg --signal sig_NMSSM_bbbb_MX_600_MY_400 --group 1`
	`python prepareModels/prepareHistos.py --config prepareModels/config/LimitsConfig_2017.cfg --signal sig_NMSSM_bbbb_MX_600_MY_400 --group 1`
	`python prepareModels/prepareHistos.py --config prepareModels/config/LimitsConfig_2018.cfg --signal sig_NMSSM_bbbb_MX_600_MY_400 --group 1`
	
- python prepareModels/makeDatacardsAndWorkspaces.py --config prepareModels/config/LimitsConfig_$1.cfg  --no-comb --signal  sig_NMSSM_bbbb_MX_600_MY_400 --bkgNorm 
	! may need to change the background normalization:
				bkgNormPerMassGroupDictionaty = {
		  "2016" : { "0" : "1.010", "1" :  "1.010", "2" :  "1.010", "3" :  "1.010", "4" :  "1.031", "none" : "1.010"},
		  "2017" : { "0" : "1.010", "1" :  "1.010", "2" :  "1.010", "3" :  "1.010", "4" :  "1.010", "none" : "1.010"},
		  "2018" : { "0" : "1.010", "1" :  "1.010", "2" :  "1.010", "3" :  "1.015", "4" :  "1.024", "none" : "1.013"},
		}
	`python prepareModels/makeDatacardsAndWorkspaces.py --config prepareModels/config/LimitsConfig_2016.cfg  --no-comb --signal sig_NMSSM_bbbb_MX_600_MY_400 --bkgNorm 1.010`
	`python prepareModels/makeDatacardsAndWorkspaces.py --config prepareModels/config/LimitsConfig_2017.cfg  --no-comb --signal sig_NMSSM_bbbb_MX_600_MY_400 --bkgNorm 1.010`
	`python prepareModels/makeDatacardsAndWorkspaces.py --config prepareModels/config/LimitsConfig_2018.cfg  --no-comb --signal sig_NMSSM_bbbb_MX_600_MY_400 --bkgNorm 1.010`
	
- combine "workspaceName" -M AsymptoticLimits --rMax 30 [ --run blind ] --X-rtd  MINIMIZER_analytic --X-rtd  FAST_VERTICAL_MORPH [--freezeParameters allConstrainedNuisances] 
- freeze parameters is for statOnly
- combine ...root -M AsymptoticLimits --rMax 30 --X-rtd  MINIMIZER_analytic --X-rtd  FAST_VERTICAL_MORPH
	`combine binsReordered_2022Mar28/Limits_kinFit_2016/sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.root -M AsymptoticLimits --rMax 30 --X-rtd  MINIMIZER_analytic --X-rtd  FAST_VERTICAL_MORPH >> binsReordered_2022Mar28/limits.txt`
	`combine binsReordered_2022Mar28/Limits_kinFit_2017/sig_NMSSM_bbbb_MX_600_MY_400/datacard2017_selectionbJets_SignalRegion.root -M AsymptoticLimits --rMax 30 --X-rtd  MINIMIZER_analytic --X-rtd  FAST_VERTICAL_MORPH >> binsReordered_2022Mar28/limits.txt`
	`combine binsReordered_2022Mar28/Limits_kinFit_2018/sig_NMSSM_bbbb_MX_600_MY_400/datacard2018_selectionbJets_SignalRegion.root -M AsymptoticLimits --rMax 30 --X-rtd  MINIMIZER_analytic --X-rtd  FAST_VERTICAL_MORPH >> binsReordered_2022Mar28/limits.txt`
- combine all years
	`mkdir -p binsReordered_2022Mar28/Limits_kinFit_RunII/sig_NMSSM_bbbb_MX_600_MY_400/`
	
	`combineCards.py c2016=binsReordered_2022Mar28/Limits_kinFit_2016/sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.txt c2017=binsReordered_2022Mar28/Limits_kinFit_2017/sig_NMSSM_bbbb_MX_600_MY_400/datacard2017_selectionbJets_SignalRegion.txt c2018=binsReordered_2022Mar28/Limits_kinFit_2018/sig_NMSSM_bbbb_MX_600_MY_400/datacard2018_selectionbJets_SignalRegion.txt > binsReordered_2022Mar28/Limits_kinFit_RunII/sig_NMSSM_bbbb_MX_600_MY_400/datacardRunII_selectionbJets_SignalRegion.txt`
	
	`text2workspace.py binsReordered_2022Mar28/Limits_kinFit_RunII/sig_NMSSM_bbbb_MX_600_MY_400/datacardRunII_selectionbJets_SignalRegion.txt`

	`combine binsReordered_2022Mar28/Limits_kinFit_RunII/sig_NMSSM_bbbb_MX_600_MY_400/datacardRunII_selectionbJets_SignalRegion.root -M AsymptoticLimits --rMax 30 --X-rtd  MINIMIZER_analytic --X-rtd  FAST_VERTICAL_MORPH >> binsReordered_2022Mar28/limits.txt`
	combineCards.py c2016={datacard2016} c2017={datacard2017} c2018={datacard2016}  {datacardRunII}
	- Goodness of Fit:
		- `combine -M GoodnessOfFit -n 2016 localCombineRuns/CombineGoF_2022Oct20/2016/sig_NMSSM_bbbb_MX_300_MY_150/datacard2016_selectionbJets_SignalRegion.txt --algo=KS >> KS_2016_sig_NMSSM_bbbb_MX_300_MY_150_VR.txt -t 1000 -s 12345`
		- `combine -M GoodnessOfFit -n 2017 localCombineRuns/CombineGoF_2022Oct20/2017/sig_NMSSM_bbbb_MX_300_MY_150/datacard2017_selectionbJets_SignalRegion.txt --algo=KS >> KS_2017_sig_NMSSM_bbbb_MX_300_MY_150_VR.txt -t 1000 -s 12345`
		- `combine -M GoodnessOfFit -n 2018 localCombineRuns/CombineGoF_2022Oct20/2018/sig_NMSSM_bbbb_MX_300_MY_150/datacard2018_selectionbJets_SignalRegion.txt --algo=KS >> KS_2018_sig_NMSSM_bbbb_MX_300_MY_150_VR.txt -t 1000 -s 12345`

	 - Goodness of Fit for loose Bjets - running all mass groups and years-  submitting 15 times in screen:
		 - run from folder localCombineRuns/CombineGoF_2022Oct24_Group2/{year}
		- `combine -M GoodnessOfFit -n 2016Group3 sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.txt --algo=KS >> KS_2016_sig_NMSSM_bbbb_MX_600_MY_400_Group3_VR.txt -t 1000 -s 12345 --fixedSignalStrength=0 &`
		- `combine -M GoodnessOfFit -n 2017Group3 sig_NMSSM_bbbb_MX_600_MY_400/datacard2017_selectionbJets_SignalRegion.txt --algo=KS >> KS_2017_sig_NMSSM_bbbb_MX_600_MY_400_Group3_VR.txt -t 1000 -s 12345 --fixedSignalStrength=0 &`
		- `combine -M GoodnessOfFit -n 2018Group3 sig_NMSSM_bbbb_MX_600_MY_400/datacard2018_selectionbJets_SignalRegion.txt --algo=KS >> KS_2018_sig_NMSSM_bbbb_MX_600_MY_400_Group3_VR.txt -t 1000 -s 12345 --fixedSignalStrength=0 &`
			- for data fit (no toys)
				- `combine -M GoodnessOfFit -n 2016Group1data sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.txt --algo=KS >> KS_2016_sig_NMSSM_bbbb_MX_600_MY_400_Group1_VR_data.txt`
				- `combine -M GoodnessOfFit -n 2017Group1data sig_NMSSM_bbbb_MX_600_MY_400/datacard2017_selectionbJets_SignalRegion.txt --algo=KS >> KS_2017_sig_NMSSM_bbbb_MX_600_MY_400_Group1_VR_data.txt`
				- `combine -M GoodnessOfFit -n 2018Group1data sig_NMSSM_bbbb_MX_600_MY_400/datacard2018_selectionbJets_SignalRegion.txt --algo=KS >> KS_2018_sig_NMSSM_bbbb_MX_600_MY_400_Group1_VR_data.txt`
			- for `saturated` model:
				- `combine -M GoodnessOfFit -n 2016Group0satTF localCombineRuns/CombineGoF_2022Oct24_Group0/2016/sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.txt --algo=saturated >> satTF_2016_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt -t 1000 -s 12345 --fixedSignalStrength=0 --toysFreq &`
				- `combine -M GoodnessOfFit -n 2016Group0satTF2 localCombineRuns/CombineGoF_2022Oct24_Group0/2016/sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.txt --algo=saturated -t 1000 --toysFreq -s 12345 --freezeParameters r --setParameters r=0 >> satTF2_2016_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt &`
			- for AD test:
				- `combine -M GoodnessOfFit -n 2016Group0 sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.txt --algo=AD >> AD_2016_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt -t 1000 -s 12345 --fixedSignalStrength=0 &`
				- `combine -M GoodnessOfFit -n 2017Group0 sig_NMSSM_bbbb_MX_600_MY_400/datacard2017_selectionbJets_SignalRegion.txt --algo=AD >> AD_2017_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt -t 1000 -s 12345 --fixedSignalStrength=0 &`
				- `combine -M GoodnessOfFit -n 2018Group0 sig_NMSSM_bbbb_MX_600_MY_400/datacard2018_selectionbJets_SignalRegion.txt --algo=AD >> AD_2018_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt -t 1000 -s 12345 --fixedSignalStrength=0 &`
				
				- `combine -M GoodnessOfFit -n 2016Group0ADdata sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.txt --algo=AD >> ADdata_2016_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt&`
				- `combine -M GoodnessOfFit -n 2017Group0ADdata sig_NMSSM_bbbb_MX_600_MY_400/datacard2017_selectionbJets_SignalRegion.txt --algo=AD >> ADdata_2017_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt -t 1000 -s 12345 --fixedSignalStrength=0 &`
				- `combine -M GoodnessOfFit -n 2018Group0 sig_NMSSM_bbbb_MX_600_MY_400/datacard2018_selectionbJets_SignalRegion.txt --algo=AD >> AD_2018_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt -t 1000 -s 12345 --fixedSignalStrength=0 &`

	
		- Fit diagnostics
			- Using datacard, old options
				- warning message:
					- "Missing background ModelConfig 'ModelConfig_bonly' in workspace 'w' in file roostats-wXQC1e.root"
					- "Will make one from the signal ModelConfig 'ModelConfig' setting signal strenth 'r' to zero"
					- "ERROR: (function: runSpecific) [WARNING]: Unable to determine uncertainties on all fit parameters in s+b fit. Have a look at https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/nonstandard/#fit-parameter-uncertainties for more information."
				 - `combine -M FitDiagnostics -n  datacard.txt`
				- `combine -M FitDiagnostics -n 2016Group0FD 2016/sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.txt --saveShapes >> FD_2016_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt &`
				- `combine -M FitDiagnostics -n 2017Group0FD 2017/sig_NMSSM_bbbb_MX_600_MY_400/datacard2017_selectionbJets_SignalRegion.txt --saveShapes >> FD_2017_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt &`
				- `combine -M FitDiagnostics -n 2018Group0FD 2018/sig_NMSSM_bbbb_MX_600_MY_400/datacard2018_selectionbJets_SignalRegion.txt --saveShapes >> FD_2018_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt &`
			- Use workspace instead of datacard text file
				- `combine -M FitDiagnostics -n 2016Group0FDshapesRootBounds 2016/sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.root --autoBoundsPOIs r --X-rtd MINIMIZER_analytic --saveShapes --saveWithUncertainties --X-rtd MINIMIZER_analytic >> FDshapesRootBounds_2016_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt &`
				- `combine -M FitDiagnostics -n 2017Group0FDshapesRootBounds 2017/sig_NMSSM_bbbb_MX_600_MY_400/datacard2017_selectionbJets_SignalRegion.root --autoBoundsPOIs r --X-rtd MINIMIZER_analytic --saveShapes --saveWithUncertainties --X-rtd MINIMIZER_analytic >> FDshapesRootBounds_2017_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt &`
				- `combine -M FitDiagnostics -n 2018Group0FDshapesRootBounds 2018/sig_NMSSM_bbbb_MX_600_MY_400/datacard2018_selectionbJets_SignalRegion.root --autoBoundsPOIs r --X-rtd MINIMIZER_analytic --saveShapes --saveWithUncertainties --X-rtd MINIMIZER_analytic >> FDshapesRootBounds_2018_sig_NMSSM_bbbb_MX_600_MY_400_Group0_VR.txt &`

text2workspace.py datacardRunII

### Run limits in parallel  on LPC (for mass window 600, 400. ie group 0):
-  2022Mar29_binsReordered_vrRange
	-  `. runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_5bins`
	-  `. runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_20bins`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_VR`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_5bins_VR`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_20bins_VR`
	 
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_lt1p3ratio`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_vrRange_lt1p3ratio`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_5bins_lt1p3ratio`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_20bins_lt1p3ratio`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_lt1p3ratio_VR`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_5bins_lt1p3ratio_VR`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_20bins_lt1p3ratio_VR`
	- #
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_lt1p2ratio`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_vrRange_lt1p2ratio`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_5bins_lt1p2ratio`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_20bins_lt1p2ratio`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_lt1p2ratio_VR`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_5bins_lt1p2ratio_VR`
	- ` . runLimits_parallel_2022Mar28.sh 2022Mar29_binsReordered_20bins_lt1p2ratio_VR`
-  reordered on 4b data
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_5bins
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_20bins
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_VR
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_5bins_VR
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_20bins_VR
	- 
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_lt1p3ratio
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_vrRange_lt1p3ratio
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_5bins_lt1p3ratio
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_20bins_lt1p3ratio
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_lt1p3ratio_VR
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_5bins_lt1p3ratio_VR
	- . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_20bins_lt1p3ratio_VR
	- 
	-   . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_lt1p2ratio
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_vrRange_lt1p2ratio
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_5bins_lt1p2ratio
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_20bins_lt1p2ratio
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_lt1p2ratio_VR
	-  . runLimits_parallel_2022Mar28.sh 2022Mar29_DATAbinsReordered_5bins_lt1p2ratio_VR
- sigma cuts (instead of ratio cuts) 
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_lt3sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_vrRange_lt3sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_5bins_lt3sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_20bins_lt3sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_lt3sigma_VR`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_5bins_lt3sigma_VR`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_20bins_lt3sigma_VR`
	
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_lt2sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_vrRange_lt2sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_5bins_lt2sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_20bins_lt2sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_lt2sigma_VR`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_5bins_lt2sigma_VR`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_20bins_lt2sigma_VR`
	
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_lt1p5sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_vrRange_lt1p5sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_5bins_lt1p5sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_20bins_lt1p5sigma`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_lt1p5sigma_VR`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_5bins_lt1p5sigma_VR`
	`. runLimits_parallel_2022Mar28.sh 2022Apr1_binsReordered_sigma_20bins_lt1p5sigma_VR`
#### 2022Apr6
- `. runLimits_parallel_2022Mar28.sh 2022Apr6 2022Apr6_fullBDT_MassWindow`
- `. runLimits_parallel_2022Mar28.sh 2022Apr6 2022Apr6_fullBDT_MassWindow_VR`
- `. runLimits_parallel_2022Mar28.sh 2022Apr6 2022Apr6_fullBDT_MassWindow`
- `. runLimits_parallel_2022Mar28.sh 2022Apr6 2022Apr6_fullBDT_MassWindow_VR`
- `. runLimits_parallel_2022Mar28.sh 2022Apr7 2022Apr7_fullBDT_MassWindow_2xErr`
- `. runLimits_parallel_2022Mar28.sh 2022Apr7 2022Apr7_fullBDT_MassWindow_2xErr_VR`
- `. runLimits_parallel_2022Mar28.sh 2022Apr7 2022Apr7_fullBDT_MassWindow_5xErr`
- `. runLimits_parallel_2022Mar28.sh 2022Apr7 2022Apr7_fullBDT_MassWindow_5xErr_VR`
- `. runLimits_parallel_2022Mar28.sh 2022Apr7 2022Apr7_fullBDT_MassWindow_10xErr`
- `. runLimits_parallel_2022Mar28.sh 2022Apr7 2022Apr7_fullBDT_MassWindow_10xErr_VR`
#### BDT syst
---
	- Nominal BDT 
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_NomBDTtoFullVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_NomBDTtoFullVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_NomBDTtoInVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_NomBDTtoInVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_NomBDTtoOutVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_NomBDTtoOutVR_VR`
		---
	- Quarter of CR for BDT training
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutQtrBDTtoOutQtr_OutVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutQtrBDTtoOutQtr_OutVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutQtrBDTtoInQtr_InVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutQtrBDTtoInQtr_InVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InQtrBDTtoOutQtr_OutVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InQtrBDTtoOutQtr_OutVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InQtrBDTtoInQtr_InVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InQtrBDTtoInQtr_InVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InQtrBDTtoFullVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InQtrBDTtoFullVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutQtrBDTtoFullVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutQtrBDTtoFullVR_VR`
		--- --- ---
		--- --- ---
	Halfs of CR for BDT training
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutBDTtoOutCR_OutVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutBDTtoOutCR_OutVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutBDTtoInCR_InVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutBDTtoInCR_InVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InBDTtoOutCR_OutVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InBDTtoOutCR_OutVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InBDTtoInCR_InVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InBDTtoInCR_InVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutBDTtoFullVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_OutBDTtoFullVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InBDTtoFullVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun16_InBDTtoFullVR_VR`
		---
	- minimum BTAG Score:
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun21_Nom_FullCRtoFullVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun21_Nom_FullCRtoFullVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR_VR`
		---
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun23_Nom_bJetScoreLoose_OutBDTtoFullVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun23_Nom_bJetScoreLoose_OutBDTtoFullVR_VR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun23_Nom_bJetScoreLoose_InBDTtoFullVR`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jun23_Nom_bJetScoreLoose_InBDTtoFullVR_VR`
		---
	Freeze params:
		`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR_VR CMS_bkgnorm`
		`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR_VR lumi_13TeV`
		`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR_VR CMS_trg_eff`
		`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf_VR autoMCStats`
		---
		`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jun21_Nom_FullCRtoFullVR_VR CMS_bkgnorm`
		`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jun21_Nom_FullCRtoFullVR_VR autoMCStats`
		`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jun21_Nom_FullCRtoFullVR_VR noneFrozen`
	up and down shapes from Out half and In half BDTs
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf`
		`. runLimits_parallel_2022Mar28.sh BDTsyst_2022Apr 2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf_VR`
		- freeze parameters:
			`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf CMS_bkgnorm`
			`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf_VR CMS_bkgnorm`
			---
			`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf CMS_bkgShape`
			`. runLimits_parallel_2022Jul5_freezeSyst.sh BDTsyst_2022Apr 2022Jul5_Nom_bJetScoreLoose_FullCRtoFullVR_upOutHalf_downInHalf_VR CMS_bkgShape`
			
#### BDT on Mx Slice
		`. runLimits_parallel_2022Mar28.sh fullSubmission_2022July 2022Sep14_Mx300_bJetLoose_3_VR`

### Extract Limits Text
	sed limits:
	`execute 'g/Combine/d8' | execute 'g/Done in/-d2' | execute 'g/Limits/norm! I,' | %s/: r </,/g`
	`sed -i -e 'g/Combine/d8' -e 'g/Done in/-d2' -e 'g/Limits/norm! I,' -e 's/: r </,/g'`
	`sed -i -e 'g/Combine/d8' -e 'g/Done in/-d2' -e 'g/Limits/norm! I,' -e 's/: r </,/g' localCombineRuns/freezeParams/autoMCStats/2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR_VR/limits.txt`
	`sed -i -e 'g/Combine/d8' localCombineRuns/freezeParams/autoMCStats/2022Jun21_Nom_bJetScoreLoose_FullCRtoFullVR_VR/limits.txt`
	`sed -i 'g/Combine/d8; g/Done in/-d2; g/Limits/norm! I,; s/: r </,/g' `
	`sed -i 'g/------/1,d; g/Combine/d8; g/Done in/-d2; g/Limits/norm! I,; s/: r </,/g' `
	`vim -e -s -c 'g/------/1,d' -c 'wq' limits_MX_300_MY_150_cp.txt`
	`vim -e -s -c "execute 'g/------/1,d' | execute 'g/Done in/d' | execute 'g/done/d' | execute 'g/execution/d' | execute 'g/random/d' | execute 'g/method/d' | execute 'g/Asymptotic/d' | execute 'g/SimNLL/d' | execute 'g/Limits/norm! I,' | execute 'g/datacard/+1d' |execute 'g/finished/d' |execute 'g/exit/d'" -c "execute '%s/: r </,/'" -c "execute '%s/\.\.\. running/,/'" -c "0r! echo %:p" -c "execute '%s/.*CondorJobs\///'"  -c 'wq' limits_MX_300_MY_150_cp.txt`
	
	`vim -e -s -c "0r! echo %" -c 'wq' limits_MX_300_MY_150_cp.txt`
	`vim -c "let @q='<C-V>7j$d 9k<C-V>7jI, \<ESC>\<C-V>7jp'"`
	`call setreg('q',"\<C-V>7j$d", "b")`
	`call setreg('q',"\<C-V>7j$d9k\<C-V>7jI , \<ESC>\<C-V>7jp", "b")`
	`call setreg("q","\<C-V>7j$d9k\<C-V>7jI , \<ESC>\<C-V>7jp", "b")`
	`vim -c 'call setreg("q","\<C-V>7j$d9k\<C-V>7jI , \<ESC>\<C-V>7jp", "b")' -e -s -c "g/statOnly/norm @q" -c "g/statOnly/norm @q" -c "execute 'g/^$/d' | execute 'g/, $/d'" -c "wq" limits_MX_300_MY_150.txt`
- edit and use the conversion file (which uses sed):
	`source LimitsTextConversion.sh`

## produce limits plots:
- code: /uscms/home/agrummer/nobackup/DiHiggs_v2/CMSSW_10_2_5/src/bbbbAnalysis/limits/produceAllResults.sh
- runs: `PlotLimitsFromCondor_allyears`  and `limits/PlotLimitVsMy.py`
- need to grab use tag from the previous step 
- to run syst
	- make sure line 106, minLimitOptions, has the `syst` option in `PlotLimitsFromCondor_allyears`
	- run PlotLimitVsMy.py with the corresponding folder tag, and the `--systematics` option
- to run freezeBKGnorm
	- make sure line 106, minLimitOptions, has the `freezeBKGnorm`  option in `PlotLimitsFromCondor_allyears`
	- run PlotLimitVsMy.py with the corresponding folder tag, and the `--freezeBKGnorm` option
## produce average of limits plots:
from `limits/` directory
- `. produceMeanLimitPlots.sh ` 
runs:  and `limits/PlotLimitMean.py`
(codes area based on `produceAllResults.sh`, and `limits/PlotLimitVsMy.py` used for making the mX limit plotts (limits as a function of mY))

## Goals
add ttbar shape:
histogram names should be:
data_BTagCSV_dataDriven_kinFit_ttbar_up
data_BTagCSV_dataDriven_kinFit_ttbar_down
1. add ttbar and ttbar_3bScaled to fillHistogram along with all the other variables from mx my quicktests
2. unroll, switch regions
3. new script to add and subtract ttbar and ttbar_3b
4. edit the combine scripts to add shape (names above, 2016 already done) run combine


python prepareModels/makeDatacardsAndWorkspaces.py --config prepareModels/config/LimitsConfig_2018.cfg  --no-comb --signal sig_NMSSM_bbbb_MX_600_MY_400 --bkgNorm 1.010
combineCards.py c2016=Limits_kinFit_2016/sig_NMSSM_bbbb_MX_600_MY_400/datacard2016_selectionbJets_SignalRegion.txt c2017=Limits_kinFit_2017/sig_NMSSM_bbbb_MX_600_MY_400/datacard2017_selectionbJets_SignalRegion.txt c2018=Limits_kinFit_2018/sig_NMSSM_bbbb_MX_600_MY_400/datacard2018_selectionbJets_SignalRegion.txt > Limits_kinFit_RunII/sig_NMSSM_bbbb_MX_600_MY_400/datacardRunII_selectionbJets_SignalRegion.txt
text2workspace.py Limits_kinFit_RunII/sig_NMSSM_bbbb_MX_600_MY_400/datacardRunII_selectionbJets_SignalRegion.txt
combine Limits_kinFit_RunII/sig_NMSSM_bbbb_MX_600_MY_400/datacardRunII_selectionbJets_SignalRegion.root -M AsymptoticLimits --rMax 30 --X-rtd  MINIMIZER_analytic --X-rtd  FAST_VERTICAL_MORPH


we cut on both pt and pt regressed
pt cuts of the trigger

derived trigger efficiencies
 - dependent on what you apply them on
 - we did this on the non-regressed pt
 apply them against something
 b-tagging scale factors: should be done using the pt that they are derived from
 trigger scale factors. have to be applied consitently - to the correct quantity they were derived from
 what are we applying to


## Cross checks:
- look at 3b distributions in the signal region and compare to 3b distributions in the control and validation region
	- if the shapes are different, maybe the study is not a good one...?
- Look at combine fit output
- Limits compared to bbgammagamma
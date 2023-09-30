from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'qcd_200pu_v11'
config.General.workArea = 'crab_area'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'testHGCalL1T_RelValV11_cfg.py'
config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = '/QCD_Pt-15to3000_TuneCP5_Flat_14TeV-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_castor_111X_mcRun4_realistic_T15_v1-v1/FEVT'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 50
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/ppradeep/HGCalTPG_LLP_NTuples_NewVar_v11'
config.Data.publication = True
config.Data.outputDatasetTag = 'qcd_200pu_v11'

config.Site.storageSite = 'T2_UK_London_IC'
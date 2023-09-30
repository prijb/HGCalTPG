from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'llp_ctau100_0pu_v11'
config.General.workArea = 'crab_area'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'testHGCalL1T_RelValV11_cfg.py'
config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = '/HiddenGluGluH_HToGG_M125_Phi-30_ctau-100/jlangfor-HiddenGluGluH_HToGG_M125_Phi-30_ctau-100_NoPU_DIGI-3607edd9fb51ebbc9bbac8adfb1b7ab9/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 4
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/ppradeep/HGCalTPG_LLP_NTuples_NewVar_v11'
config.Data.publication = True
config.Data.outputDatasetTag = 'llp_ctau100_0pu_v11'

config.Site.storageSite = 'T2_UK_London_IC'
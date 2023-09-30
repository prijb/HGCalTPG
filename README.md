# HGCalTPG
```
cmsrel 12_5_2_patch1
cd CMSSW_12_5_2_patch1/src
cmsenv
git cms-init
git remote add hgctpg https://github.com/hgc-tpg/cmssw.git
git fetch hgctpg
git cms-merge-topic -u hgc-tpg:v3.31.0_1252p1
git clone git@github.com:git@github.com:prijb/HGCalTPG.git
scram b -j 8
```

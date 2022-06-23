import numpy as np
import ROOT

bigfiles = ['mc_361106.Zee.4lep.root', 
'mc_363490.llll.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

def isGoodLepton(tree, ilep):
    if( (tree.lep_pt[ilep] > 5000.) and  \
        ( abs( tree.lep_eta[ilep]) < 2.5) and \
        ( (tree.lep_ptcone30[ilep]/tree.lep_pt[ilep]) < 0.3) and \
        ( (tree.lep_etcone20[ilep] / tree.lep_pt[ilep]) < 0.3 ) ):
        return True
    else: 
        return False

def isGoodMuon(tree, ilep):
    theta = 2*np.arctan(np.exp(-tree.lep_eta[ilep]))
    if( abs(tree.lep_type[ilep] ) == 13  and
        ( abs(tree.lep_trackd0pvunbiased[ilep])/tree.lep_tracksigd0pvunbiased[ilep] < 3) and
        ( abs(tree.lep_z0[ilep]*ROOT.TMath.Sin( theta )) < 0.5) ):
            return True
    else: 
        return False

def isGoodElectron(tree, ilep):
    theta = 2*np.arctan(np.exp(-tree.lep_eta[ilep]))
    if( abs(tree.lep_type[ilep] ) == 11  and
        ( tree.lep_pt[ilep] > 7000. )      and 
        ( abs( tree.lep_eta[ilep]) < 2.47) and 
        ( abs(tree.lep_trackd0pvunbiased[ilep])/tree.lep_tracksigd0pvunbiased[ilep] < 5) and
        ( abs(tree.lep_z0[ilep]*ROOT.TMath.Sin( theta )) < 0.5) 
        ):
            return True
    else: 
        return False




def ptfilter(bestand): 
    
    # for bestand in filelist:
    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
    tree = f.Get('mini')
    # number_entries = tree.GetEntries()
    
    ptdowncut = [25000, 15000, 10000, 7000]
    ptupcut = [1000000000, 60000, 40000, 30000]

    goodlist = []
    for event in range(1000):
        tree.GetEntry(event)
        
        ptfilter = False
        for i in range(4):
            if (tree.lep_pt[i] < ptdowncut[i]) or (tree.lep_pt[i] > ptupcut[i]):
                ptfilter = True
        
        if not ptfilter:
            goodlist.append(event)

    print(bestand, len(goodlist))

ptfilter('mc_345060.ggH125_ZZ4lep.4lep.root')
ptfilter('mc_363490.llll.4lep.root')
ptfilter('mc_361107.Zmumu.4lep.root')
ptfilter('mc_361106.Zee.4lep.root')
ptfilter('mc_345336.ZH125J_qqWW2lep.4lep.root')
ptfilter('mc_345337.ZH125J_llWW2lep.4lep.root')
ptfilter('mc_410000.ttbar_lep.4lep.root')
 
        
        

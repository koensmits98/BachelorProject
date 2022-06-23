import ROOT
import numpy as np

def vergelijk(bestand): 
    
    # for bestand in filelist:
    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
    tree = f.Get('mini')
    # number_entries = tree.GetEntries()
  
    goodlist = []

    for event in range(1000):
        tree.GetEntry(event)
        
        ratiolist = []
        
        etfilter = False
        for i in range(4):
            ratio = abs(tree.lep_etcone20[i]/tree.lep_pt[i])
            ratiolist.append(ratio)
            
        ratiolist.sort()
        # print(ratiolist)
        if ratiolist[2] > 0.3:
            etfilter = True
        if ratiolist[3] > 0.3:
            etfilter = True
        # print(ratiolist)
        if etfilter == False:
            goodlist.append(event)

    print(bestand, len(goodlist))

vergelijk('mc_345060.ggH125_ZZ4lep.4lep.root')
vergelijk('mc_363490.llll.4lep.root')
vergelijk('mc_361107.Zmumu.4lep.root')
vergelijk('mc_361106.Zee.4lep.root')
vergelijk('mc_345336.ZH125J_qqWW2lep.4lep.root')
vergelijk('mc_345337.ZH125J_llWW2lep.4lep.root')
vergelijk('mc_410000.ttbar_lep.4lep.root')
 
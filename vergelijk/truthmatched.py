import ROOT
import numpy as np

def truthmatched(bestand): 
    
    # for bestand in filelist:
    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
    tree = f.Get('mini')
    print(tree)
    trueevents = []
    for event in range(100):
        tree.GetEntry(event)
        truthmatched = True
        # print(tree.lep_truthMatched)
        print(tree.lep_truthMatched[1])
        if tree.lep_truthMatched[1] == true




truthmatched('mc_345060.ggH125_ZZ4lep.4lep.root')
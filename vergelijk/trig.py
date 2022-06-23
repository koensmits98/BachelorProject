import ROOT
import numpy as np


def vergelijk(bestand): 
    
    # for bestand in filelist:
    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
    tree = f.Get('mini')
    # print(tree)
    nontrig = []
    for event in range(1000):
        tree.GetEntry(event)
        if not tree.trigE and not tree.trigM:
            nontrig.append(event)

    print(len(nontrig))


vergelijk('mc_361106.Zee.4lep.root')
vergelijk('mc_361107.Zmumu.4lep.root')
vergelijk('mc_345060.ggH125_ZZ4lep.4lep.root')
vergelijk('mc_345336.ZH125J_qqWW2lep.4lep.root')
vergelijk('mc_345337.ZH125J_llWW2lep.4lep.root')
vergelijk('mc_363490.llll.4lep.root')
vergelijk('mc_410000.ttbar_lep.4lep.root')



            
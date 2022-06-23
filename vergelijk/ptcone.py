import ROOT
import numpy as np

jetsandhiggs = ['mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

def getshortname(bestand):
    shortname = bestand.replace('.4lep.root', '')
    shortname.replace('mc', '')
    return(shortname)

def vergelijk(bestand):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    canvas.Divide(2,1)

    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
    tree = f.Get('mini')
    hist = ROOT.TH1F('ratio', "ratio", 100, 0, 1 )
    hist2 = ROOT.TH1F('ratio2', "ratio", 100, 0 , 1 )

    for event in range(1000):
        tree.GetEntry(event)
        
        ratiolist = []
        for j in range(4):
            ratio = tree.lep_etcone20[j]/tree.lep_pt[j]
            ratiolist.append(ratio)
        
        ratiolist.sort()
        hist.Fill(ratiolist[0])
        hist.Fill(ratiolist[1])
        hist2.Fill(ratiolist[2])
        hist2.Fill(ratiolist[3])

    canvas.cd(1)
    hist.Draw()

    canvas.cd(2)
    hist2.Draw()

    canvas.Print('ptcone{}.jpg'.format(bestand))
        
vergelijk('mc_361106.Zee.4lep.root')
vergelijk('mc_361107.Zmumu.4lep.root')
vergelijk('mc_345060.ggH125_ZZ4lep.4lep.root')
# vergelijk('mc_345336.ZH125J_qqWW2lep.4lep.root')
# vergelijk('mc_345337.ZH125J_llWW2lep.4lep.root')
# vergelijk('mc_363490.llll.4lep.root')
# vergelijk('mc_410000.ttbar_lep.4lep.root')
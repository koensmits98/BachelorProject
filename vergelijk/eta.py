import ROOT
import numpy as np

def vergelijk(bestand):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)

    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
    tree = f.Get('mini')
    hist = ROOT.TH1F('ratio', "ratio", 100, -5 , 5 )

    for event in range(1000):
        tree.GetEntry(event)

        for j in range(4):
            # theta = 2*np.arctan(np.exp(-tree.lep_eta[j]))
            hist.Fill(tree.lep_eta[j])

            
    imagename = 'eta{}.jpg'.format(bestand)
    hist.Draw()
    canvas.Print(imagename)

vergelijk('mc_361106.Zee.4lep.root')
vergelijk('mc_361107.Zmumu.4lep.root')
vergelijk('mc_345060.ggH125_ZZ4lep.4lep.root')
vergelijk('mc_345336.ZH125J_qqWW2lep.4lep.root')
vergelijk('mc_345337.ZH125J_llWW2lep.4lep.root')
vergelijk('mc_363490.llll.4lep.root')
vergelijk('mc_410000.ttbar_lep.4lep.root')
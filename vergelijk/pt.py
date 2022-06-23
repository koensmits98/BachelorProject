import ROOT
import numpy as np

jetsandhiggs = ['mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']


def vergelijk(bestand):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)

    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
    tree = f.Get('mini')
    hist = ROOT.TH1F('ratio', "ratio", 100, 0 , 1 )

    for event in range(1000):
        tree.GetEntry(event)
        ptx = 0
        pty = 0
        for j in range(4):
            ptx += tree.lep_pt[j]*np.cos(tree.lep_phi[j])
            pty += tree.lep_pt[j]*np.sin(tree.lep_phi[j])

            # ratio = tree.lep_etcone20[j]/tree.lep_E[j]
            # hist.Fill(ratio)
        print(np.sqrt(ptx*ptx + pty*pty))

vergelijk('mc_361106.Zee.4lep.root')
# vergelijk('mc_345336.ZH125J_qqWW2lep.4lep.root')
# vergelijk('mc_345337.ZH125J_llWW2lep.4lep.root')
# vergelijk('mc_363490.llll.4lep.root')
# vergelijk('mc_410000.ttbar_lep.4lep.root')
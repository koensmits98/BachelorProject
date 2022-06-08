import ROOT
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# opening root file
f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root")
f2 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_363490.llll.4lep.root")

# Here we define a tree named "tree" to extract the data from the input .root file.
tree = f.Get("mini")
tree2 = f2.Get("mini")

lumi_data = 10 #fb ^-1
number_entries = tree.GetEntries()
number_entries2 = tree2.GetEntries()

# print "Number of entries in the tree = ", number_entries

canvas = ROOT.TCanvas("canvas","plot a variable",800,600)
# canvas.Divide(2,1)
# canvas.cd(1)


def m4lhistfile(tree, filename, histname, aantal, scaling):

    hist = ROOT.TH1F(histname,"plot m4l",100, 0 ,400000)
    samplesize = 1

    for i in range(aantal):
        tree.GetEntry(i)
        
        istight = True
        ptcone = False
        etcone = False
        ptfilter = False
        ptlist = [25, 15, 10, 7]

        for i in range(3):
            if tree.lep_isTightID[i] == False: 
                istight = False
            if tree.lep_ptcone30[i]/tree.lep_pt[i] > 0.15:
                ptcone = True
            if abs(tree.lep_etcone20[i]/tree.lep_E[i]) > 0.15:   
                etcone = True
            if tree.lep_pt[i] < ptlist[i]:
                ptfilter = True
        if istight == False or ptcone == True or etcone == True or ptfilter == True:
            continue
        
        samplesize += 1

        E4l_squared = np.sum(tree.lep_E) ** 2
        px = tree.lep_pt * np.cos(tree.lep_phi)
        py = tree.lep_pt * np.sin(tree.lep_phi)
        pz = tree.lep_pt * np.sinh(tree.lep_eta)

        p4l_squared = np.sum(px) ** 2 + np.sum(py) ** 2 + np.sum(pz) ** 2

        m4l = (E4l_squared - p4l_squared) ** 0.5
        if scaling == True:
            finalmcWeight = tree.XSection * 1000 * lumi_data * tree.mcWeight * 1/tree.SumWeights * tree.scaleFactor_LepTRIGGER * tree.scaleFactor_ELE * tree.scaleFactor_MUON
            hist.Fill(m4l, finalmcWeight)
        else:
            finalmcWeight = tree.XSection * 1000 * lumi_data * tree.mcWeight * 1/tree.SumWeights
            hist.Fill(m4l, finalmcWeight)

    print('samplesize is:', samplesize)
    b = ROOT.TFile.Open(filename, "RECREATE")
    b.cd()
    hist.Write()    

# m4lhistfile(tree,"higgs1.root", "higgs_hist", number_entries, False)
# m4lhistfile(tree2, "background1.root", "background_hist", number_entries2, False)

m4lhistfile(tree, 'higgsscaled.root', 'higgs_hist', number_entries, True)
m4lhistfile(tree2, 'backgroundscaled.root', 'background_hist', number_entries2, True)

def cone(tree):
    for i in range(10):
        tree.GetEntry(i)
        for j in range(4):
            print(tree.lep_ptcone30[j], tree.lep_etcone20[j])

# cone(tree)


	

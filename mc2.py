import ROOT
import numpy as np

lumi_data = 10


def m4lhist(mcfilename, rootfilename, scaling):
    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(mcfilename), "READ")
    tree = f.Get('mini')
    number_entries = tree.GetEntries()

    hist = ROOT.TH1F('m4lhist', "m4l",100, 0 ,400000)

    for i in range(number_entries):
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

    b = ROOT.TFile.Open('/user/ksmits/analyse/mcrootfiles/{}'.format(rootfilename), "RECREATE")
    b.cd()
    hist.Write() 

m4lhist('mc_345060.ggH125_ZZ4lep.4lep.root', 'mc_345060.ggH125_ZZ4lep.4lep.root', True)
m4lhist('mc_341155.VBFH125_tautaull.4lep.root', 'mc_341155.VBFH125_tautaull.4lep.root', True)
m4lhist('mc_341964.WH125_ZZ4lep.4lep.root', 'mc_341964.WH125_ZZ4lep.4lep.root', True)


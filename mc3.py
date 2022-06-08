import ROOT
import numpy as np

lumi_data = 10


def m4lhist(rootfilename, scaling):
    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(rootfilename), "READ")
    tree = f.Get('mini')
    number_entries = tree.GetEntries()

    hist = ROOT.TH1F('m4lhist', "m4l",100, 0 ,400000)

    for event in range(10):
        tree.GetEntry(event)
        
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


m4lhist('mc_361106.Zee.4lep.root', True)


errorlist = ['mc_361100.Wplusenu.4lep.root']

mclist = ['mc_341122.ggH125_tautaull.4lep.root' ,\
'mc_341155.VBFH125_tautaull.4lep.root' ,\
'mc_341947.ZH125_ZZ4lep.4lep.root' ,\
'mc_341964.WH125_ZZ4lep.4lep.root' ,\
'mc_344235.VBFH125_ZZ4lep.4lep.root' ,\
'mc_345060.ggH125_ZZ4lep.4lep.root' ,\
'mc_345323.VBFH125_WW2lep.4lep.root' ,\
'mc_345324.ggH125_WW2lep.4lep.root' ,\
'mc_345325.WpH125J_qqWW2lep.4lep.root' ,\
'mc_345327.WpH125J_lvWW2lep.4lep.root' ,\
'mc_345336.ZH125J_qqWW2lep.4lep.root' ,\
'mc_345337.ZH125J_llWW2lep.4lep.root' ,\
'mc_345445.ZH125J_vvWW2lep.4lep.root' ,\
'mc_361100.Wplusenu.4lep.root' ,\
'mc_361101.Wplusmunu.4lep.root' ,\
'mc_361102.Wplustaunu.4lep.root' ,\
'mc_361103.Wminusenu.4lep.root' ,\
'mc_361104.Wminusmunu.4lep.root' ,\
'mc_361105.Wminustaunu.4lep.root',\
'mc_361106.Zee.4lep.root' ,\
'mc_361107.Zmumu.4lep.root' ,\
'mc_361108.Ztautau.4lep.root' ,\
'mc_363356.ZqqZll.4lep.root' ,\
'mc_363358.WqqZll.4lep.root' ,\
'mc_363359.WpqqWmlv.4lep.root' ,\
'mc_363360.WplvWmqq.4lep.root' ,\
'mc_363489.WlvZqq.4lep.root' ,\
'mc_363490.llll.4lep.root' ,\
'mc_363491.lllv.4lep.root' ,\
'mc_363492.llvv.4lep.root' ,\
'mc_363493.lvvv.4lep.root' ]

# for filename in mclist:
#     m4lhist(filename, True)
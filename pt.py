import ROOT

lumi_data = 10

# Here we open the data that we want to analyse, which is in the form of a .root file. A .root file consists of a tree having branches and leaves.
# datafilelist = ["/data/atlas/users/mvozak/opendata/4lep/Data/data_A.4lep.root",\
# "/data/atlas/users/mvozak/opendata/4lep/Data/data_B.4lep.root" ,\
# "/data/atlas/users/mvozak/opendata/4lep/Data/data_C.4lep.root",\
# "/data/atlas/users/mvozak/opendata/4lep/Data/data_D.4lep.root"]

datafilelist = ["data_A.4lep.root",\
"data_B.4lep.root" ,\
"data_C.4lep.root",\
"data_D.4lep.root" ]

mcfilelist = ["/data/atlas/users/mvozak/opendata/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root" ,\
"/data/atlas/users/mvozak/opendata/4lep/MC/mc_363490.llll.4lep.root"]

goodfiles = ['mc_341122.ggH125_tautaull.4lep.root',\
'mc_341155.VBFH125_tautaull.4lep.root', \
'mc_341947.ZH125_ZZ4lep.4lep.root', \
'mc_341964.WH125_ZZ4lep.4lep.root', \
'mc_344235.VBFH125_ZZ4lep.4lep.root', \
'mc_345060.ggH125_ZZ4lep.4lep.root', \
'mc_345323.VBFH125_WW2lep.4lep.root', \
'mc_345324.ggH125_WW2lep.4lep.root', \
'mc_345325.WpH125J_qqWW2lep.4lep.root', \
'mc_345327.WpH125J_lvWW2lep.4lep.root', \
'mc_345336.ZH125J_qqWW2lep.4lep.root', \
'mc_345337.ZH125J_llWW2lep.4lep.root', \
'mc_345445.ZH125J_vvWW2lep.4lep.root', \
'mc_361106.Zee.4lep.root', \
'mc_361107.Zmumu.4lep.root', \
'mc_361108.Ztautau.4lep.root', \
'mc_363356.ZqqZll.4lep.root', \
'mc_363358.WqqZll.4lep.root', \
'mc_363490.llll.4lep.root', \
'mc_363491.lllv.4lep.root', \
'mc_363492.llvv.4lep.root', \
'mc_410000.ttbar_lep.4lep.root', \
'mc_410011.single_top_tchan.4lep.root', \
'mc_410012.single_antitop_tchan.4lep.root', \
'mc_410013.single_top_wtchan.4lep.root', \
'mc_410014.single_antitop_wtchan.4lep.root', \
'mc_410025.single_top_schan.4lep.root', \
'mc_410026.single_antitop_schan.4lep.root']

def pthist(filelist):
    
    hist0 = ROOT.TH1F("pt1","transverse momentum; transverse momentum; Events ",40,0,100000)
    hist1 = ROOT.TH1F("pt2","transverse momentum; transverse momentum; Events ",40,0,100000)
    hist2 = ROOT.TH1F("pt3","transverse momentum; transverse momentum; Events ",40,0,100000)
    hist3 = ROOT.TH1F("pt4","transverse momentum; transverse momentum; Events ",40,0,100000)
    histlist = [hist0, hist1, hist2, hist3]
    
    
    for bestand in filelist:
        f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand), 'READ')
        tree = f.Get('mini')
        number_entries = tree.GetEntries()

        for event in range(number_entries):
            tree.GetEntry(event)

            finalmcWeight = tree.XSection * 1000 * lumi_data * tree.mcWeight * 1/tree.SumWeights * tree.scaleFactor_LepTRIGGER * tree.scaleFactor_ELE * tree.scaleFactor_MUON
            for i in range(4):
                histlist[i].Fill(tree.lep_pt[i], finalmcWeight) 
        b = ROOT.TFile.Open('/user/ksmits/BachelorProject/pthists/{}'.format(bestand), "RECREATE")
        b.cd()
        for i in range(4):
            histlist[i].Write()  

lijst = ['mc_345060.ggH125_ZZ4lep.4lep.root']

pthist(goodfiles)
    
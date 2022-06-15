import ROOT

datafilelist = ["data_A.4lep.root",\
"data_B.4lep.root" ,\
"data_C.4lep.root",\
"data_D.4lep.root" ]

def ptdata(filelist, filename):
    hist0 = ROOT.TH1F("pt1","transverse momentum; transverse momentum; Events ",40,0,100000)
    hist1 = ROOT.TH1F("pt2","transverse momentum; transverse momentum; Events ",40,0,100000)
    hist2 = ROOT.TH1F("pt3","transverse momentum; transverse momentum; Events ",40,0,100000)
    hist3 = ROOT.TH1F("pt4","transverse momentum; transverse momentum; Events ",40,0,100000)
    histlist = [hist0, hist1, hist2, hist3]
        

    for bestand in filelist:
        f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/{}".format(bestand), 'READ')
        tree = f.Get('mini')
        number_entries = tree.GetEntries()
        for event in range(number_entries):
            tree.GetEntry(event)
            for i in range(4):
                histlist[i].Fill(tree.lep_pt[i])

    b = ROOT.TFile.Open('/user/ksmits/BachelorProject/pthists/{}'.format(filename), "RECREATE")
    b.cd()
    for i in range(4):
        histlist[i].Write()

ptdata(datafilelist, 'datastacked.root')


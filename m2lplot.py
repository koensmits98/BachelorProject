import ROOT

higgs = ['mc_345060.ggH125_ZZ4lep.4lep.root']

ZZ = ['mc_363490.llll.4lep.root']

higgsandZZ = ['mc_363490.llll.4lep.root',\
'mc_345060.ggH125_ZZ4lep.4lep.root']

datafilelist = ["data_A.4lep.root",\
"data_B.4lep.root" ,\
"data_C.4lep.root",\
"data_D.4lep.root" ]

datastacked = ['datastacked.root']

def m2lplot(filelist):
    for bestand in filelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/{}'.format(bestand), "READ")
        hist = f.Get('m2l')

        canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
        canvas.cd()

        hist.Draw()
        imagename = bestand.replace('.root','.jpg', 1)
        canvas.Print('/user/ksmits/BachelorProject/m2lhists/{}'.format(imagename))

# m2lplot(datastacked)

def m2lwithdata(datafilelist, mcfilelist, filename):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    datahist = ROOT.TH1F('datahist', "dileptonmass; invmass; events", 40, 0, 120000) 
    mchist = hist = ROOT.TH1F('mchist', "dileptonmass; invmass; events", 40, 0, 120000)

    for bestand in datafilelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/{}'.format(bestand), "READ")
        hist = f.Get('m2l')
        datahist.Add(hist)
    
    for bestand in mcfilelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/{}'.format(bestand), "READ")
        hist = f.Get('m2l')
        hist.Rebin(25)
        mchist.Add(hist)

    datahist.Draw('e')
    mchist.Draw('same hist')
    canvas.Print('/user/ksmits/BachelorProject/m2lhists/{}'.format(filename))

m2lwithdata(datastacked, higgsandZZ, 'mcendata.jpg')

    
import ROOT

datafilelist = ["data_A.4lep.root",\
"data_B.4lep.root" ,\
"data_C.4lep.root",\
"data_D.4lep.root" ]

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

bigfiles = ['mc_363490.llll.4lep.root',
'mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

higgsandZZ = ['mc_363490.llll.4lep.root',\
'mc_345060.ggH125_ZZ4lep.4lep.root']

def ptplot(filelist):
    datafile = ROOT.TFile.Open('/user/ksmits/BachelorProject/pthists/datastacked.root' , "READ")
    datahist0 = datafile.Get('pt1')
    datahist1 = datafile.Get('pt2')
    datahist2 = datafile.Get('pt3')
    datahist3 = datafile.Get('pt4')
    datahistlist = [datahist0, datahist1, datahist2, datahist3]
    
    for bestand in filelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/pthists/{}'.format(bestand), "READ")
        histlist = []
        hist0 = f.Get('pt1')
        hist1 = f.Get('pt2')
        hist2 = f.Get('pt3')
        hist3 = f.Get('pt4')
        histlist = [hist0, hist1, hist2, hist3]
        canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
        canvas.Divide(2,2)
        
        for i in range(4):
            canvas.cd(i+1)
            # datahistlist[i].Draw('e')
            histlist[i].Draw('same hist')
        imagename = bestand.replace('.root','.jpg', 1)
        canvas.Print('/user/ksmits/BachelorProject/pthists/{}'.format(imagename))

ptplot(bigfiles)





def ptstack(filelist, imagename):
    datafile = ROOT.TFile.Open('/user/ksmits/BachelorProject/pthists/datastacked.root' , "READ")
    datahist0 = datafile.Get('pt1')
    datahist1 = datafile.Get('pt2')
    datahist2 = datafile.Get('pt3')
    datahist3 = datafile.Get('pt4')
    datahistlist = [datahist0, datahist1, datahist2, datahist3]
    
    mchist0 = ROOT.TH1F("pt1","transverse momentum; transverse momentum; Events ",40,0,100000)
    mchist1 = ROOT.TH1F("pt2","transverse momentum; transverse momentum; Events ",40,0,100000)
    mchist2 = ROOT.TH1F("pt3","transverse momentum; transverse momentum; Events ",40,0,100000)
    mchist3 = ROOT.TH1F("pt4","transverse momentum; transverse momentum; Events ",40,0,100000)
    mchistlist= [mchist0, mchist1, mchist2, mchist3]

    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    canvas.Divide(2,2)
        
    for bestand in filelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/pthists/{}'.format(bestand), "READ")
        hist0 = f.Get('pt1')
        hist1 = f.Get('pt2')
        hist2 = f.Get('pt3')
        hist3 = f.Get('pt4')
        histlist = [hist0, hist1, hist2, hist3]
        
        for i in range(4):
            mchistlist[i].Add(histlist[i])


    for i in range(4):
        canvas.cd(i+1)
        datahistlist[i].Draw('E')
        mchistlist[i].Draw('same hist')
    # imagename = bestand.replace('.root','.jpg', 1)
    canvas.Print('/user/ksmits/BachelorProject/pthists/{}'.format(imagename))

ptstack(bigfiles, 'bigfiles.jpg')
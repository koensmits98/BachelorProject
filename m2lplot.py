import ROOT

bigfiles = ['mc_363490.llll.4lep.root',
'mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

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

m2lplot(bigfiles)

def m2lwithdata(mcfilelist, filename):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
 
    mchist = ROOT.TH1F('mchist', "dileptonmass; invmass; events", 40, 0, 120000)

    datafile = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/datastacked.root', 'READ')
    datahist = datafile.Get('m2l')
    datahist.Draw('E')
    
    for bestand in mcfilelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/{}'.format(bestand), "READ")
        hist = f.Get('m2l')
        hist.Rebin(25)
        mchist.Add(hist)

    mchist.Draw('same hist')
    canvas.Print('/user/ksmits/BachelorProject/m2lhists/{}'.format(filename))

# m2lwithdata(higgsandZZ, 'mcendata.jpg')



def m2lstacked(filelist, imagename):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
 
    mchist = hist = ROOT.TH1F('mchist', "dileptonmass; invmass; events", 40, 0, 120000)

    datafile = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/datastacked.root', 'READ')
    datahist = datafile.Get('m2l')
    datahist.Draw('E')
    
    stack = {}
    stack['0'] = ROOT.TH1F('abc', "m2l", 40, 0, 120000)

    
    histlist = {}
    countslist = []
    sortedlist = []
    indexlist = []
    for bestand in filelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/{}'.format(bestand), "READ")
        hist = f.Get('m2l')
        counts = hist.Integral()
        countslist.append(counts)
        sortedlist.append(counts)
    print(countslist)
    sortedlist.sort(reverse=True)
    print(sortedlist)
    for i in sortedlist:
        indexlist.append(countslist.index(i))
    
    print(indexlist)
    
    i = 0

    for j in indexlist:
        i += 1
        print(i)
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/{}'.format(filelist[j]), "READ")
        hist = f.Get('m2l')
        hist.Rebin(25)
        if filelist[j] == "mc_363490.llll.4lep.root":
            hist.Scale(1.3)
        
        stack['{}'.format(i)] = stack['{}'.format(i-1)].Clone()
        stack['{}'.format(i)].Add(hist)
        stack['{}'.format(i)].SetDirectory(0)


        # print(stack['{}'.format(i)])

    for i in range(i, 0, -1):
        stack['{}'.format(i)].SetFillColor(i+1)
        stack['{}'.format(i)].Draw('same hist')
    canvas.Print('/user/ksmits/BachelorProject/m2lhists/{}'.format(imagename))

# m2lstacked(bigfiles, 'bigfiles.jpg')

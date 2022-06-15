import ROOT
import copy
import numpy as np

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
'mc_361105.Wminustaunu.4lep.root' ,\
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
'mc_363493.lvvv.4lep.root' ,\
'mc_410000.ttbar_lep.4lep.root' ,\
'mc_410011.single_top_tchan.4lep.root' ,\
'mc_410012.single_antitop_tchan.4lep.root' ,\
'mc_410013.single_top_wtchan.4lep.root' ,\
'mc_410014.single_antitop_wtchan.4lep.root' ,\
'mc_410025.single_top_schan.4lep.root' ,\
'mc_410026.single_antitop_schan.4lep.root' ,\
'mc_410155.ttW.4lep.root' ,\
'mc_410218.ttee.4lep.root' ,\
'mc_410219.ttmumu.4lep.root' ]

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

higgsfiles = ['mc_341122.ggH125_tautaull.4lep.root' ,\
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
'mc_363490.llll.4lep.root' ]

bigfiles = ['mc_363490.llll.4lep.root',
'mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

taufiles = [ 'mc_410155.ttW.4lep.root', \
'mc_410218.ttee.4lep.root', \
'mc_410219.ttmumu.4lep.root']

datafilelist = ["data_A.4lep.root",\
"data_B.4lep.root" ,\
"data_C.4lep.root",\
"data_D.4lep.root" ]

ZZandHiggs = ["mc_363490.llll.4lep.root" ,\
"mc_345060.ggH125_ZZ4lep.4lep.root"]

datastacked = ['datastacked.root']

higgs = ['mc_345060.ggH125_ZZ4lep.4lep.root']

#this function plots every hist in the list and gives it an image with the same name
def m4lplot(filelist, cut):
    stackedhist = ROOT.TH1F('stackedhist',"plot m4l", 100, 0 , 400000)
    
    
    for bestand in filelist:
        if cut == True:
            bestand = bestand.replace('.root', 'cut.root')

        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(bestand), "READ")
        hist = f.Get('m4lhist')
        # if bestand == 'mc_363490.llll.4lep.root':
        #     hist.Scale(1.3)
        print(hist.Integral())
        canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)


    # datahist.Draw('E')
    # stackedhist.Draw('same hist')

        hist.Draw('E')
        imagename = bestand.replace('.root','.jpg', 1)
        canvas.Print('/user/ksmits/BachelorProject/m4lhists/{}'.format(imagename))

m4lplot(bigfiles, True)

# m4lplot(['datastackedcut1.root'])



def integral(filename):
    f = ROOT.TFile.Open(filename)
    hist = f.Get('m4lhist')
    integral = hist.Integral()
    print(integral)

# integral('/user/ksmits/BachelorProject/m4lhists/higgsuncut.root')
# integral('/user/ksmits/BachelorProject/m4lhists/higgscut.root')

def stack(filelist, imagename, cut):

    
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    
    if cut == True:
        datafile = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/datastackedcut.root', 'read')
    if cut == False:
        datafile = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/datastacked.root', 'read')
    datahist = datafile.Get('m4lhist')
    datahist.Draw('E')
    
    stack = {}
    stack['0'] = ROOT.TH1F('abc', "m4l", 100, 0 , 400000)

    # stack['{}'.format(i)] = stack['{}'.format(i-1)].Clone()
    # stack['1'].Draw('hist')
    # print(stack['0'])
    # a = stack['0'].Clone()
    # print(a)
    
    histlist = {}
    countslist = []
    sortedlist = []
    indexlist = []
    for bestand in filelist:
        if cut == True:
            bestand = bestand.replace('.root','cut.root')
            print(bestand)
        
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(bestand), "READ")
        hist = f.Get('m4lhist')
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
        filelist[j] = filelist[j].replace('.root', 'cut.root')
        i += 1
        # print(i)
        print(filelist[j])
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(filelist[j]), "READ")
        hist = f.Get('m4lhist')
        
        if filelist[j] == "mc_363490.llll.4lep.root":
            hist.Scale(1.3)
        
        stack['{}'.format(i)] = stack['{}'.format(i-1)].Clone()
        stack['{}'.format(i)].Add(hist)
        stack['{}'.format(i)].SetDirectory(0)


        # print(stack['{}'.format(i)])

    for i in range(i, 0, -1):
        stack['{}'.format(i)].SetFillColor(i+1)
        stack['{}'.format(i)].Draw('same hist')
    canvas.Print('/user/ksmits/BachelorProject/m4lhists/{}'.format(imagename))

stack(bigfiles, 'bigfiles.jpg', False)
# stack(ZZandHiggs, 'ZZandHiggs.jpg')



import ROOT
import copy

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

taufiles = [ 'mc_410155.ttW.4lep.root', \
'mc_410218.ttee.4lep.root', \
'mc_410219.ttmumu.4lep.root']

datafile = ROOT.TFile('datastacked.root', 'READ')
datahist = datafile.Get('datastacked')


stackedhist = ROOT.TH1F('stackedhist',"plot m4l",100, 0 ,400000)

def plot(filelist, plotname):
    for bestand in filelist:
        
        f = ROOT.TFile.Open('/user/ksmits/analyse/mcrootfiles/{}'.format(bestand), "READ")
        hist = f.Get('m4lhist')

        if bestand == 'mc_363490.llll.4lep.root':
            hist.Scale(1.3)
        
        stackedhist.Add(hist)

    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)


    datahist.Draw('E')
    stackedhist.Draw('same hist')


    canvas.Print(plotname)

# plot(goodfiles, 'goodfiles.jpg')


def combinedplot(filelist, plotname):
    
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)

    combinedhist = ROOT.THStack('datastacked',"plot m4l")

    datahist.Draw('E')

    i = 0

    for bestand in filelist:
        
        i += 1

        f = ROOT.TFile.Open('/user/ksmits/analyse/mcrootfiles/{}'.format(bestand), "READ")
        hist = f.Get('m4lhist')
        hist.SetName(hist.GetName()+str(i))

        if bestand == 'mc_363490.llll.4lep.root':
            hist.Scale(1.3)

        hist.SetLineColor(ROOT.kBlack) 
        hist.SetLineWidth(2) 
        hist.SetFillColor(i)
        hist.Print()

        combinedhist.Add(copy.deepcopy(hist))

    print()
    combinedhist.Print()
    combinedhist.Draw('same hist')
    

    canvas.Print(plotname)

combinedplot(goodfiles, 'layered.jpg')
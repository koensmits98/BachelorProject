import ROOT
import copy
import numpy as np

bigfiles = ['mc_363490.llll.4lep.root',
'mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

goodfileswithout = [
'mc_341155.VBFH125_tautaull.4lep.root', \
'mc_341947.ZH125_ZZ4lep.4lep.root', \
'mc_341964.WH125_ZZ4lep.4lep.root', \
'mc_344235.VBFH125_ZZ4lep.4lep.root', \
'mc_345323.VBFH125_WW2lep.4lep.root', \
'mc_345324.ggH125_WW2lep.4lep.root', \
'mc_345325.WpH125J_qqWW2lep.4lep.root', \
'mc_345327.WpH125J_lvWW2lep.4lep.root', \
'mc_345445.ZH125J_vvWW2lep.4lep.root', \
'mc_361108.Ztautau.4lep.root', \
'mc_363356.ZqqZll.4lep.root', \
'mc_363358.WqqZll.4lep.root', \
'mc_363492.llvv.4lep.root', \
'mc_410000.ttbar_lep.4lep.root', \
'mc_410011.single_top_tchan.4lep.root', \
'mc_410012.single_antitop_tchan.4lep.root', \
'mc_410013.single_top_wtchan.4lep.root', \
'mc_410014.single_antitop_wtchan.4lep.root', \
'mc_410025.single_top_schan.4lep.root', \
'mc_410026.single_antitop_schan.4lep.root']

goodfiles = ['mc_341155.VBFH125_tautaull.4lep.root', \
'mc_341947.ZH125_ZZ4lep.4lep.root', \
'mc_341964.WH125_ZZ4lep.4lep.root', \
'mc_344235.VBFH125_ZZ4lep.4lep.root', \
'mc_345323.VBFH125_WW2lep.4lep.root', \
'mc_345324.ggH125_WW2lep.4lep.root', \
'mc_345325.WpH125J_qqWW2lep.4lep.root', \
'mc_345327.WpH125J_lvWW2lep.4lep.root', \
'mc_345445.ZH125J_vvWW2lep.4lep.root', \
'mc_361108.Ztautau.4lep.root', \
'mc_363356.ZqqZll.4lep.root', \
'mc_363358.WqqZll.4lep.root', \
'mc_363492.llvv.4lep.root', \
'mc_410000.ttbar_lep.4lep.root', \
'mc_410011.single_top_tchan.4lep.root', \
'mc_410012.single_antitop_tchan.4lep.root', \
'mc_410013.single_top_wtchan.4lep.root', \
'mc_410014.single_antitop_wtchan.4lep.root', \
'mc_410025.single_top_schan.4lep.root', \
'mc_410026.single_antitop_schan.4lep.root',\
'mc_363490.llll.4lep.root',
'mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']


def m4lplot(filelist, cutlist, directory):  
    for bestand in filelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/{}/{}'.format(directory, bestand), "READ")
        f.ls()
        for cut in cutlist:    
            hist = f.Get(cut)
            
            # if bestand == 'mc_363490.llll.4lep.root':
            #     hist.Scale(1.3)
            # print(hist.Integral())
            canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)


        # datahist.Draw('E')
        # stackedhist.Draw('same hist')

            hist.Draw()
            imagename = bestand.replace('.root','{}.jpg'.format(cut), 1)
            
            
            canvas.Print('/user/ksmits/BachelorProject/{}/{}'.format(directory, imagename))

cutlist = ['m4lhist', 'cut1', 'cut2', 'cut3', 'cut4' , 'cut5', 'cut6']
# m4lplot(bigfiles, cutlist, 'm4lrecreate')

# m4lplot(['datastacked.root'], cutlist, 'm4lrecreate')
# ['datastacked.root']













def stack(filelist, cut, directory, imagename):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    
    datafile = ROOT.TFile.Open('/user/ksmits/BachelorProject/{}/datastacked.root'.format(directory), 'read')
    datahist = datafile.Get('m4l' + cut)
    print(datahist)
    datahist.Draw('E')
    
    stack = {}
    stack['0'] = ROOT.TH1F('abc', "m4l", 23, 80000 , 170000)

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
        
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/{}/{}'.format(directory, bestand), "READ")
        hist = f.Get('m4l' + cut)
        print(hist)
        counts = hist.Integral()
        countslist.append(counts)
        sortedlist.append(counts)
    print(countslist)
    sortedlist.sort(reverse=True)
    print(sortedlist)
    for i in sortedlist:
        indexlist.append(countslist.index(i))
    
    print(indexlist)
    

    leg = ROOT.TLegend(.40,.50,.70,.80)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.035)



    i = 0
    for j in indexlist:
        i += 1
        # print(i)
        print(filelist[j])
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/{}/{}'.format(directory, filelist[j]), "READ")
        hist = f.Get('m4l'+ cut)
        
        if filelist[j] == "mc_363490.llll.4lep.root":
            hist.Scale(1.3)
        
        stack['{}'.format(i)] = stack['{}'.format(i-1)].Clone()
        stack['{}'.format(i)].Add(hist)
        stack['{}'.format(i)].SetDirectory(0)
        
        leg.AddEntry(stack['{}'.format(i)], '{},    {}'.format(filelist[j], int(hist.Integral())), 'f')

        # print(stack['{}'.format(i)])


   

    for i in range(i, 0, -1):
        stack['{}'.format(i)].SetFillColor(i+1)
        stack['{}'.format(i)].Draw('same hist')
        
    # imagename = '{}{}.jpg'.format(str(filelist), cut)

    
    
    leg.Draw('same')
    canvas.Print('/user/ksmits/BachelorProject/{}/{}'.format(directory, imagename))


# stack(goodfiles, 'm4lhist', 'm4lrecreate', 'goodfiles.jpg')
# stack(goodfiles, 'cut1', 'm4lrecreate', 'goodfilescut1.jpg')
# stack(goodfiles, 'cut2', 'm4lrecreate', 'goodfilescut2.jpg')
# stack(goodfiles, 'cut3', 'm4lrecreate', 'goodfilescut3.jpg')
# stack(goodfiles, 'cut4', 'm4lrecreate', 'goodfilescut4.jpg')
# stack(goodfiles, 'cut5', 'm4lrecreate', 'goodfilescut5.jpg')
# stack(goodfiles, 'cut6', 'm4lrecreate', 'goodfilescut6.jpg')


stack(bigfiles, 'cut0' , 'analyse', 'm4lbigfiles.jpg')
stack(bigfiles, 'cut1' , 'analyse', 'm4lbigfilescut1.jpg')
stack(bigfiles, 'cut2' , 'analyse', 'm4lbigfilescut2.jpg')
stack(bigfiles, 'cut3' , 'analyse', 'm4lbigfilescut3.jpg')
stack(bigfiles, 'cut4' , 'analyse', 'm4lbigfilescut4.jpg')
stack(bigfiles, 'cut5' , 'analyse', 'm4lbigfilescut5.jpg')


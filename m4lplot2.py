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

def m4lplot(filelist, cut):  
    for bestand in filelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(bestand), "READ")
        f.ls()
        hist = f.Get(cut)
        
        # if bestand == 'mc_363490.llll.4lep.root':
        #     hist.Scale(1.3)
        # print(hist.Integral())
        canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)


    # datahist.Draw('E')
    # stackedhist.Draw('same hist')

        hist.Draw('E')
        imagename = bestand.replace('.root','{}.jpg'.format(cut), 1)
        canvas.Print('/user/ksmits/BachelorProject/m4lhists/{}'.format(imagename))

# m4lplot(bigfiles, 'cut3')





def stack(filelist, cut, imagename):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    

    datafile = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/datastacked.root', 'read')
    datahist = datafile.Get(cut)
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
        
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(bestand), "READ")
        hist = f.Get(cut)
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
    
    i = 0

    for j in indexlist:
        i += 1
        # print(i)
        print(filelist[j])
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(filelist[j]), "READ")
        hist = f.Get(cut)
        
        if filelist[j] == "mc_363490.llll.4lep.root":
            hist.Scale(1.3)
        
        stack['{}'.format(i)] = stack['{}'.format(i-1)].Clone()
        stack['{}'.format(i)].Add(hist)
        stack['{}'.format(i)].SetDirectory(0)


        # print(stack['{}'.format(i)])

    for i in range(i, 0, -1):
        stack['{}'.format(i)].SetFillColor(i+1)
        stack['{}'.format(i)].Draw('same hist')
    
    # leg = ROOT.TLegend(.50,.60,.80,.80)
    # leg.AddEntry('1', '2','3' , 'f')
    canvas.Print('/user/ksmits/BachelorProject/m4lhists/{}'.format(imagename))

stack(bigfiles, 'm4lhist' ,'bigfilesuncut.jpg')
import ROOT


def m2lplot(filelist):
    for bestand in filelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/pthists/{}'.format(bestand), "READ")
        for i in range(4):
            hist0 = f.Get('pt1')
            hist1 = f.Get('pt2')
            hist2 = f.Get('pt3')
            hist3 = f.Get('pt4')
            histlist = [hist0, hist1, hist2, hist3]
        canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
        canvas.Divide(2,2)
        
        for i in range(4):
            canvas.cd(i+1)
            histlist[i].Draw('hist')
        imagename = bestand.replace('.root','.jpg', 1)
        canvas.Print('/user/ksmits/BachelorProject/pthists/{}'.format(imagename))

lijst = ['mc_345060.ggH125_ZZ4lep.4lep.root']

m2lplot(lijst)
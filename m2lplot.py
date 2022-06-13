import ROOT

def m2lplot(filelist):
    for bestand in filelist:
        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/{}'.format(bestand), "READ")
        hist = f.Get('m2l Z boson')

        canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
        canvas.cd()

        hist.Draw()
        imagename = bestand.replace('.root','.jpg', 1)
        canvas.Print('/user/ksmits/BachelorProject/m2lhists/{}'.format(imagename))

lijst = ['mc_345060.ggH125_ZZ4lep.4lep.root']
lijst2 = ['mc_363490.llll.4lep.root']

m2lplot(lijst2)
import ROOT


def mcendataplot(higgsfile, bgfile, datafile, imagename):

    f1 = ROOT.TFile(higgsfile, "READ")
    f2 = ROOT.TFile(bgfile, "READ")
    f3 = ROOT.TFile(datafile, 'READ')

    histhiggs = f1.Get("higgs_hist")
    histbg = f2.Get("background_hist")
    histdata = f3.Get("datastacked")

    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)

    histbg.Scale(1.3)
    histhiggs.Scale(1.1)

    histbg.Add(histhiggs)


    histdata.Draw('E')
    histbg.Draw("same hist")

    canvas.Print(imagename)

mcendataplot("higgsscaled.root", "backgroundscaled.root", "datastacked.root", 'mcendatascaled.jpg')


def histdivide(higgs, bg, higgsscaled, bgscaled):
    
    f1 = ROOT.TFile(higgs, "READ")
    f2 = ROOT.TFile(bg, "READ")
    f3 = ROOT.TFile(higgsscaled, 'READ')
    f4 = ROOT.TFile(bgscaled, 'READ')

    histhiggs = f1.Get("higgs_hist")
    histbg = f2.Get("background_hist")
    histhiggsscaled = f3.Get('higgs_hist')
    histbgscaled = f4.Get('background_hist')

    histbg.Add(histhiggs)

    histbgscaled.Add(histhiggsscaled)

    histbg.Divide(histbgscaled)

    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)

    histbg.Draw('hist')

    canvas.Print('divide.jpg')



def allmcdata(a):
    f = ROOT.TFile('/user/ksmits/analyse/mcrootfiles/zz4lep.root', 'read')
    # f3 = ROOT.TFile('datastacked.root', 'READ')
    
    histmc = f.Get('m4lhist')
    # histdata = f3.Get("datastacked")

    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    
    
    # histdata.Draw('E')
    histmc.Draw("hist")

    canvas.Print('allMC.jpg')

# allmcdata(1)

# histdivide('higgs1.root', 'background1.root', 'higgsscaled.root', 'backgroundscaled.root')


# histhiggs.Rebin(30)
# histbg.Rebin(30)
# histdata.Scale(0.5)

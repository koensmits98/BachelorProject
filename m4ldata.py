import ROOT
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# opening root file

datafilelist = ["data_A.4lep.root",\
"data_B.4lep.root" ,\
"data_C.4lep.root",\
"data_D.4lep.root" ]

def m4lstacked(filelist, filename):
    stackedhist = ROOT.TH1F('datastacked',"plot m4l",100, 0, 400000)
     
    for bestand in filelist:

        f = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(bestand), 'READ')
        hist = f.Get('m4lhist')
        stackedhist.Add(hist)
    b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(filename), 'recreate')
    b.cd()
    stackedhist.Write()

m4lstacked(datafilelist, 'datastacked.root')
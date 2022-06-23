import ROOT
import copy
import numpy as np


def zzscale(directory, cut):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    
    datafile = ROOT.TFile.Open('/user/ksmits/BachelorProject/{}/datastacked.root'.format(directory), 'read')
    datahist = datafile.Get(cut)

    zzfile = ROOT.TFile.Open('/user/ksmits/BachelorProject/{}/mc_363490.llll.4lep.root'.format(directory))
    zzhist = zzfile.Get(cut)

    datahist.Divide(zzhist)
    # datahist.Draw()
    # zzhist.Draw()
    datahist.Draw()
    canvas.Print('zzscale.jpg')

zzscale('m4lrecreate', 'cut2')

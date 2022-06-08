import ROOT
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# opening root file

f1 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/data_A.4lep.root")
f2 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/data_B.4lep.root")
f3 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/data_C.4lep.root")
f4 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/data_D.4lep.root")

# Here we define a tree named "tree" to extract the data from the input .root file.

tree1 = f1.Get('mini')
tree2 = f2.Get('mini')
tree3 = f3.Get('mini')
tree4 = f4.Get('mini')


hist = ROOT.TH1F('datastacked',"plot m4l",100, 0, 400000)

def datahistfile(tree):
    """ Function to plot a histogram of invariant mass of Higgs boson via 4 lepton measurements (m4l)
    Input: 
        tree: tree object from ROOT file
        lumi_data: luminosity of the actual data [fb^-1]
        number_entries: number of entries of the generated MC data
        scaling: set True for scaling and False for no scaling
    Output:
        saved file named my_hist_m4l.jpg (no scaling) or my_hist_m4l_scaled.jpg (with scaling)
    """

    # Define a 'canvas' on which to draw a histogram. Its name is "canvas" and its header is "plot a variable". 
    # The two following arguments define the width and the height of the canvas
    
    number_entries = tree.GetEntries()

    for i in range(number_entries):
        tree.GetEntry(i)
        
        istight = True
        ptcone = False
        etcone = False

        for i in range(3):
            if tree.lep_isTightID[i] == False: 
                istight = False
            if tree.lep_ptcone30[i]/tree.lep_pt[i] > 0.15:
                ptcone = True
            if abs(tree.lep_etcone20[i]/tree.lep_E[i]) > 0.15:   
                etcone = True
            if tree.lep_pt[i] < ptlist[i]:
                ptfilter = True
        if istight == False or ptcone == True or etcone == True or ptfilter == True:
            continue

        E4l_squared = np.sum(tree.lep_E) ** 2
        px = tree.lep_pt * np.cos(tree.lep_phi)
        py = tree.lep_pt * np.sin(tree.lep_phi)
        pz = tree.lep_pt * np.sinh(tree.lep_eta)

        p4l_squared = np.sum(px) ** 2 + np.sum(py) ** 2 + np.sum(pz) ** 2
        m4l = (E4l_squared - p4l_squared) ** 0.5
        hist.Fill(m4l)


datahistfile(tree1)    
datahistfile(tree2)   
datahistfile(tree3)   
datahistfile(tree4)

b = ROOT.TFile.Open('datastacked.root', 'recreate')
b.cd()
hist.Write()



hist0 = ROOT.TH1F("hist0","transverse momentum; transverse momentum; Events ",40,0,100000)
hist1 = ROOT.TH1F("hist1","transverse momentum; transverse momentum; Events ",40,0,100000)
hist2 = ROOT.TH1F("hist2","transverse momentum; transverse momentum; Events ",40,0,100000)
hist3 = ROOT.TH1F("hist3","transverse momentum; transverse momentum; Events ",40,0,100000)

histlist = [hist0, hist1, hist2, hist3]

def pt(tree):
    for event in tree:
        for i in range(4):
            histlist[i].Fill(tree.lep_pt[i])        

def ptplot(filename):
    pt(tree1)
    pt(tree2)
    pt(tree3)
    pt(tree4)

    canvas = ROOT.TCanvas("canvas","plot a variable",800,600)
    canvas.Divide(2,2)

    hist0.SetLineColor(ROOT.kBlack) 
    hist0.SetLineWidth(2) 
    hist0.SetFillColor(ROOT.kAzure)

    hist1.SetLineColor(ROOT.kBlack) 
    hist1.SetLineWidth(2) 
    hist1.SetFillColor(ROOT.kAzure)

    hist2.SetLineColor(ROOT.kBlack) 
    hist2.SetLineWidth(2) 
    hist2.SetFillColor(ROOT.kAzure)

    hist3.SetLineColor(ROOT.kBlack) 
    hist3.SetLineWidth(2) 
    hist3.SetFillColor(ROOT.kAzure)

    canvas.cd(1)
    hist0.Draw("HIST")

    canvas.cd(2)
    hist1.Draw("HIST")

    canvas.cd(3)
    hist2.Draw("HIST")

    canvas.cd(4)
    hist3.Draw("HIST")

    canvas.Print(filename)



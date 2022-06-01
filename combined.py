import ROOT
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def hello():
    print("hello")
    print("test")

# opening root file
f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root")
f2 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_363490.llll.4lep.root")

# Here we define a tree named "tree" to extract the data from the input .root file.
tree = f.Get("mini")
tree2 = f2.Get("mini")

lumi_data = 10 #fb ^-1
number_entries = tree.GetEntries()
number_entries2 = tree2.GetEntries()

# print "Number of entries in the tree = ", number_entries

canvas = ROOT.TCanvas("canvas","plot a variable",800,600)
# canvas.Divide(2,1)
# canvas.cd(1)

hist = ROOT.TH1F("tryout","tryout plot m4l",100,50000,700000)

def m4lhist(tree, lumi_data, number_entries):
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
    # The two following arguments define the width and the height of the canvas.

    for event in tree:
        E4l_squared = np.sum(tree.lep_E) ** 2
        px = tree.lep_pt * np.cos(tree.lep_phi)
        py = tree.lep_pt * np.sin(tree.lep_phi)
        pz = tree.lep_pt * np.sinh(tree.lep_eta)

        p4l_squared = np.sum(px) ** 2 + np.sum(py) ** 2 + np.sum(pz) ** 2

        m4l = (E4l_squared - p4l_squared) ** 0.5

        #finalmcWeight = tree.XSection * 1000 * lumi_data * tree.mcWeight * 1/number_entries
        finalmcWeight = tree.XSection * 1000 * lumi_data * tree.mcWeight * 1/tree.SumWeights
        hist.Fill(m4l, finalmcWeight)
 
m4lhist(tree, lumi_data, number_entries)
m4lhist(tree2, lumi_data, number_entries2)

hist.SetLineColor(ROOT.kBlack) 
hist.SetLineWidth(2) 
hist.SetFillColor(ROOT.kAzure)
hist.Draw("HIST")
canvas.Print("combinedin1plot.jpg")

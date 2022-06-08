import ROOT

# Here we open the data that we want to analyse, which is in the form of a .root file. A .root file consists of a tree having branches and leaves.
f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root")
f1 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/data_A.4lep.root")
f2 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/data_B.4lep.root")
f3 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/data_C.4lep.root")
f4 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/data_D.4lep.root")

tree = f.Get("mini")
number_entries = tree.GetEntries()


canvas = ROOT.TCanvas("canvas","plot a variable",800,600)
canvas.Divide(2,2)



# ptmax = 0
# for event in tree:
#     if tree.lep_pt > ptmax:
#         ptmax = tree.lep_pt
# print(ptmax)

hist = ROOT.TH1F("hist","transverse momentum; transverse momentum; Events ",20,0,100000)
hist1 = ROOT.TH1F("hist1","transverse momentum; transverse momentum; Events ",20,0,100000)
hist2 = ROOT.TH1F("hist2","transverse momentum; transverse momentum; Events ",20,0,100000)
hist3 = ROOT.TH1F("hist3","transverse momentum; transverse momentum; Events ",20,0,100000)

for event in tree:
    hist.Fill(tree.lep_pt[0])
    hist1.Fill(tree.lep_pt[1])
    hist2.Fill(tree.lep_pt[2])
    hist3.Fill(tree.lep_pt[3])

hist.SetLineColor(ROOT.kBlack) 
hist.SetLineWidth(2) 
hist.SetFillColor(ROOT.kAzure)

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
hist.Draw("HIST")

canvas.cd(2)
hist1.Draw("HIST")

canvas.cd(3)
hist2.Draw("HIST")

canvas.cd(4)
hist3.Draw("HIST")

canvas.Print("pt.jpg")

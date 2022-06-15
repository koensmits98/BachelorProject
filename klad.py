import ROOT
import numpy as np

f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_361106.Zee.4lep.root")
f2 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_363490.llll.4lep.root")
f3 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root")

tree = f.Get('mini')
tree2 = f2.Get("mini")
tree3 = f3.Get('mini')


bigfiles = ['mc_363490.llll.4lep.root',
'mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

def weg(tree, imagename):
    lijst = [] 
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    hist = ROOT.TH1F('m4lhist',"plot m4l",100, -10000, 10000)
    for event in range(1000):
        tree.GetEntry(event)
        # print(tree.jet_pt)
        a = False
        if tree.jet_n != 0:
            lijst.append(event)
        
        
        # for i in range(tree.jet_n):
            # print(tree.jet_pt[i], tree.jet_jvt[i])
        for i in range(4):
            print(tree.lep_etcone20[i])
            hist.Fill(tree.lep_etcone20[i])
    hist.Draw()
    canvas.Print(imagename)
        #     if abs(tree.lep_etcone20[i]/tree.lep_pt[i]) > 0.15:
        #         a = True
        # if a == True:
        #     lijst.append(a)
    # print(len(lijst))

# weg(tree3, 'etconehiggs.jpg')
# weg(tree, 'etconeZee.jpg')
def etconehist(tree):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    lijst = [] 
    for event in range(100):
        tree.GetEntry(event)

# print(weg(tree), weg(tree2), weg(tree3))


print('abdcd'.replace('d', 'e'))

# lijst = [3,2,4,5,6]
# lijst2 = [3,2,4,5,6]
# lijst2.sort()

# print(lijst)
# indexlist = []
# for i in lijst2:
#     indexlist.append(lijst.index(i))
    
# print(indexlist)
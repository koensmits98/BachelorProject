import ROOT
import numpy as np

f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_361106.Zee.4lep.root")
f2 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_363490.llll.4lep.root")
f3 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root")


tree = f.Get('mini')
tree2 = f2.Get("mini")
tree3 = f3.Get('mini')

f4 = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/mc_361106.Zee.4lep.root')
f4.ls()

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
        a = False
        if tree.jet_n != 0:
            lijst.append(event)
        
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


# print('abdcd'.replace('d', 'e'))

# lijst = [3,2,4,5,6]
# lijst2 = [3,2,4,5,6]
# lijst2.sort()

# print(lijst)
# indexlist = []
# for i in lijst2:
#     indexlist.append(lijst.index(i))
    
# print(indexlist)

def sfos(tree):
    sfos = []
    
    for event in range(100):
        tree.GetEntry(event)
        
        checkpair = [[0,1],[0,2],[0,3]]
        pairs_found = []
        
        for i,j in checkpair:
            otherpair = [0,1,2,3]
            otherpair.remove(i)
            otherpair.remove(j)

            index0 = otherpair[0]
            index1 = otherpair[1]

            if tree.lep_charge[i] == - tree.lep_charge[j] and tree.lep_type[i] == tree.lep_type[j] \
            and tree.lep_charge[index0] == - tree.lep_charge[index1] and tree.lep_type[index0] == tree.lep_type[index1]: 
                pairs_found.append([i,j])
        # if len(pairs_found == 0)
        # print(pairs_found)
        
        if len(pairs_found) != 0:
            sfos.append(event)
        if len(pairs_found) == 0:
            typelist = []
            chargelist = []
            for i in range(4):
                typelist.append(tree.lep_charge[i])
                chargelist.append(tree.lep_type[i])
            print(typelist, chargelist)
    print(len(sfos))
        # for i in range(4):
        #     print(tree.lep_charge[i])
        #     print(tree.lep_type[i])

# sfos(tree3)

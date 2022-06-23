import ROOT
import numpy as np

# f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_361106.Zee.4lep.root")
# f2 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_363490.llll.4lep.root")
# f3 = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root")
# tree = f.Get('mini')
# tree2 = f2.Get("mini")
# tree3 = f3.Get('mini')


lumi_data = 10

zh = ['mc_345060.ggH125_ZZ4lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root']

for bestand in zh:
    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
    tree = f.Get('mini')
    print(tree)
    number_entries = tree.GetEntries()
    for event in range(10):
        tree.GetEntry(event)
        finalmcWeight = tree.XSection * 1000 * lumi_data * tree.mcWeight * 1/ tree.SumWeights * tree.scaleFactor_LepTRIGGER * tree.scaleFactor_ELE * tree.scaleFactor_MUON * tree.scaleFactor_PILEUP
        # print(tree.SumWeights , tree.scaleFactor_LepTRIGGER , tree.scaleFactor_ELE , tree.scaleFactor_MUON , tree.scaleFactor_PILEUP)
        # print(finalmcWeight)
        print(tree.XSection)




f4 = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/mc_361106.Zee.4lep.root')
# f4.ls()

bigfiles = ['mc_363490.llll.4lep.root',
'mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

def isGoodLepton(tree, ilep):
    if( (tree.lep_pt[ilep] > 5000.) and  \
        ( abs( tree.lep_eta[ilep]) < 2.5) and \
        ( (tree.lep_ptcone30[ilep]/tree.lep_pt[ilep]) < 0.3) and \
        ( (tree.lep_etcone20[ilep] / tree.lep_pt[ilep]) < 0.3 ) ):
        return True
    else: 
        return False

def isGoodMuon(tree, ilep):
    theta = 2*np.arctan(np.exp(-tree.lep_eta[ilep]))
    if( abs(tree.lep_type[ilep] ) == 13  and
        ( abs(tree.lep_trackd0pvunbiased[ilep])/tree.lep_tracksigd0pvunbiased[ilep] < 3) and
        ( abs(tree.lep_z0[ilep]*ROOT.TMath.Sin( theta )) < 0.5) ):
            return True
    else: 
        return False

def isGoodElectron(tree, ilep):
    theta = 2*np.arctan(np.exp(-tree.lep_eta[ilep]))
    if( abs(tree.lep_type[ilep] ) == 11  and
        ( tree.lep_pt[ilep] > 7000. )      and 
        ( abs( tree.lep_eta[ilep]) < 2.47) and 
        ( abs(tree.lep_trackd0pvunbiased[ilep])/tree.lep_tracksigd0pvunbiased[ilep] < 5) and
        ( abs(tree.lep_z0[ilep]*ROOT.TMath.Sin( theta )) < 0.5) 
        ):
            return True
    else: 
        return False

# def klad(tree):
#     canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
#     hist = ROOT.TH1F('m4lhist',"plot m4l",100, -10000, 10000)
#     for event in range(100):
#         tree.GetEntry(event)
#         for i in range(4):


for it, event in enumerate(tree):
    if not tree.trigE and not tree.trigM:
        print(event)
# klad(tree)

def goodmuon(tree):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
    lijst = [] 
    for event in range(100):
        tree.GetEntry(event)
        for i in range(4):
            if (isGoodElectron(tree, i) == False and isGoodMuon(tree, i) == False) and isGoodLepton(tree, i) == False:
                lijst.append(event)
                continue
            # if (tree.lep_type[i] == 11 and  or (tree.lep_type[i] == 13 and isGoodElectron(tree, i) == False):
            # if tree.lep_type == 11:
            #     if isGoodElectron(tree, i) == False:
                
    print(lijst, len(lijst))
# goodmuon(tree)
# goodmuon(tree3)

def pt(tree):
     for event in range(20):
        istight = True
        
        tree.GetEntry(event)
        print(tree.lep_pt)
        print(tree.lep_isTightID)

# pt(tree3)
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
# for event in tree:
#     lep_n = len(tree.lep_pt)
#     lep_ids   = [lep for lep in range(0, lep_n)]
#     all_pairs = [(a, b) for idx, a in enumerate(lep_ids) for b in lep_ids[idx + 1:]]
#     if not trigE and 

# for i in range(10):
    # print(i)
    # if i == 6:
    #     continue
    # print('hoi')

for i in range(2,4,1):
    print(i)
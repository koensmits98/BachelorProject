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

def isGoodJet(tree, ijet):
   if( tree.jet_pt[ijet] > 30000. and abs(tree.jet_eta[ijet]) < 4.4): return True
   else: return False

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


def m4lstacked(filelist):
    histnames = ['m4lhist', 'cut1', 'cut2', 'cut3', 'cut4', 'cut5', 'cut6']
    histlist = []
    for histname in histnames:
        histlist.append(ROOT.TH1F(histname,"plot m4l", 23, 80000, 170000))


    for bestand in filelist:
        f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/{}".format(bestand), 'READ')
        tree = f.Get('mini')
        number_entries = tree.GetEntries()
        
        for event in range(number_entries):
            tree.GetEntry(event)
        
            E4l_squared = np.sum(tree.lep_E) ** 2
            px = tree.lep_pt * np.cos(tree.lep_phi)
            py = tree.lep_pt * np.sin(tree.lep_phi)
            pz = tree.lep_pt * np.sinh(tree.lep_eta)

            p4l_squared = np.sum(px) ** 2 + np.sum(py) ** 2 + np.sum(pz) ** 2
            m4l = (E4l_squared - p4l_squared) ** 0.5
            
            histlist[0].Fill(m4l)

            
            sfos = True
            istight = True
            leptonfilter = False
            ptfilter = False
            jetfilter = False
            ptlist = [25000, 15000, 10000, 7000]

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
            if len(pairs_found) == 0:
                sfos = False

            nGoodLeptons = 0
            for i in range(4):
                if tree.lep_isTightID[i] == False: 
                    istight = False
                isGoodLep = isGoodLepton(tree, i)
                isGoodMu  = isGoodMuon(tree, i)
                isGoodEle = isGoodElectron(tree, i)
                # print(isGoodLep, isGoodMu, isGoodEle)
                if( isGoodLep and (isGoodMu or isGoodEle)): 
                    nGoodLeptons += 1
                else: 
                    pass
                # print(nGoodLeptons)

                
                if tree.lep_pt[i] < ptlist[i]:
                    ptfilter = True
            
            if nGoodLeptons != 4:
                leptonfilter = True

            nGoodJets = 0
            for ijet in range(0, len(tree.jet_pt) ):
                goodJet = isGoodJet(tree, ijet) 

                if not goodJet: continue

                nGoodJets += 1
            if nGoodJets != len(tree.jet_pt):
                jetfilter = True    

            if sfos == False:
                continue
            histlist[1].Fill(m4l)
            
            if tree.lep_n > 4:
                continue
            histlist[2].Fill(m4l)
            
            if leptonfilter == True:
                continue
            histlist[3].Fill(m4l)
            
            if ptfilter == True:
                continue
            histlist[4].Fill(m4l)

            if jetfilter == True:
                continue
            histlist[5].Fill(m4l)
            if istight == False:
                continue    
            histlist[6].Fill(m4l)



            


    b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lrecreate/{}'.format('datastacked.root'), "RECREATE")
        
    
    # b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(filename), 'recreate')
    b.cd()
    for i in range(len(histlist)):
        histlist[i].SetStats(False)
        histlist[i].Write()
    b.Close()

m4lstacked(datafilelist)
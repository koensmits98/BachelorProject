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
    histnames = ['m4lhist', 'cut1', 'cut2', 'cut3' , 'cut4', 'cut5', 'cut6']
    datahistlist = []
    for histname in histnames:
        datahistlist.append(ROOT.TH1F(histname, "m4l", 100, 0 , 400000))
 
    
    for bestand in filelist:
        f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/{}".format(bestand), 'READ')
        tree = f.Get('mini')
        number_entries = tree.GetEntries()
        
        for event in range(number_entries):
            tree.GetEntry(event)
        
   
            sfos = True
            leptonfilter = False
            jetfilter = False
            istight = True
            ptfilter = False
            ptdowncut = [25000, 15000, 10000, 7000]
            ptupcut = [1000000000, 60000, 40000, 30000]
            
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
                    pairs_found.append([index0, index1])
            
            endpairs = []
            endm2l = []
            
            if len(pairs_found) == 0:
                sfos = False

            
            nGoodLeptons = 0
            for i in range(4):
                if tree.lep_isTightID[i] == False: 
                    istight = False
                if tree.lep_pt[i] < ptdowncut[i]:
                    ptfilter = True
                if tree.lep_pt[i] > ptupcut[i]:
                    ptfilter = True
                isGoodLep = isGoodLepton(tree, i)
                isGoodMu  = isGoodMuon(tree, i)
                isGoodEle = isGoodElectron(tree, i)
                # print(isGoodLep, isGoodMu, isGoodEle)
                if( isGoodLep and (isGoodMu or isGoodEle)): 
                    nGoodLeptons += 1
                else: 
                    pass

            if nGoodLeptons != 4 or tree.lep_n > 4:
                leptonfilter = True
            
            # nGoodJets = 0
            # for ijet in range(0, len(tree.jet_pt) ):
            #     goodJet = isGoodJet(tree, ijet) 

            #     if not goodJet: continue

            #     nGoodJets += 1
            # if nGoodJets != len(tree.jet_pt):
            #     jetfilter = True 

            E4l_squared = np.sum(tree.lep_E) ** 2
            px = tree.lep_pt * np.cos(tree.lep_phi)
            py = tree.lep_pt * np.sin(tree.lep_phi)
            pz = tree.lep_pt * np.sinh(tree.lep_eta)

            p4l_squared = np.sum(px) ** 2 + np.sum(py) ** 2 + np.sum(pz) ** 2

            m4l = (E4l_squared - p4l_squared) ** 0.5

            datahistlist[0].Fill(m4l)

            if sfos == False:
                continue
            datahistlist[1].Fill(m4l)

            if leptonfilter == True:
                continue
            datahistlist[2].Fill(m4l)

            if ptfilter == True:
                continue
            datahistlist[3].Fill(m4l)

    
    b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lrecreate/{}'.format('datastacked.root'), "RECREATE")
    b.cd()

    for i in range(len(datahistlist)):
        datahistlist[i].Write()
    b.Close()

m4lstacked(datafilelist)
import ROOT
import numpy as np

datafilelist = ["data_A.4lep.root",\
"data_B.4lep.root" ,\
"data_C.4lep.root",\
"data_D.4lep.root" ]

datastacked = ['datastacked.root']

ZZ = ['mc_363490.llll.4lep.root']

higgs = ['mc_345060.ggH125_ZZ4lep.4lep.root']

lumi_data = 10


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

def m2l(filelist):
    histnames = ['m2l', 'cut1', 'cut2']
    histlist = []
    for histname in histnames:
        histlist.append(ROOT.TH1F(histname, "dileptonmass; invmass; events", 40, 0, 120000))
    k = 0
    
    for bestand in filelist:
        f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/{}".format(bestand))
        tree = f.Get("mini")
        number_entries = tree.GetEntries()


        meerleptons = []

        for event in range(number_entries):
            tree.GetEntry(event)

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
            
            if nGoodLeptons != 4 or tree.lep_n > 4:
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
            

            zmass1 = None
            zmass2 = None





            checkpair = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
            otherpair = [0,1,2,3]
            m2l_total = []
            mass_Z = 91000 # MeV
            
            
            E = tree.lep_E
            px = tree.lep_pt * np.cos(tree.lep_phi)
            py = tree.lep_pt * np.sin(tree.lep_phi)
            pz = tree.lep_pt * np.sinh(tree.lep_eta)

            m2ls_per_event = []
            pairs_found = []

            if len(tree.lep_type) > 4:
                # print(event)
                meerleptons.append(event)
            
            for i,j in checkpair: 
                    if tree.lep_charge[i] == - tree.lep_charge[j] and tree.lep_type[i] == tree.lep_type[j]:
                        pairs_found.append([i,j])
                        m2l = ((E[i] + E[j]) ** 2 - ((px[i] + px[j]) ** 2 + (py[i] + py[j]) ** 2 + (pz[i] + pz[j]) ** 2)) ** 0.5
                        m2ls_per_event.append(m2l)

            if len(pairs_found) == 2:
                # hist.Fill(m2ls_per_event[0], finalmcWeight)
                # hist.Fill(m2ls_per_event[1], finalmcWeight)
                zmass1 = m2ls_per_event[0]
                zmass2 = m2ls_per_event[1]
                # hist_2d.Fill(m2ls_per_event[0], m2ls_per_event[1], finalmcWeight)
                # histm4l.Fill(m2ls_per_event[0]+ m2ls_per_event[1], finalmcWeight)
            if len(pairs_found) == 4:
                smallest = 1000000
                bestpair = []
                bestm2l = 0
                for i in range(len(pairs_found)):
                
                    absdif = abs(m2ls_per_event[i] - mass_Z)
                
                    if absdif <= smallest:
                        bestpair = pairs_found[i]
                        bestm2l = m2ls_per_event[i]
                
                otherpair.remove(bestpair[0])
                otherpair.remove(bestpair[1])

                index = pairs_found.index(otherpair)

                zmass1 = bestm2l
                zmass2 = m2ls_per_event[index]

            histlist[0].Fill(zmass1)
            histlist[0].Fill(zmass2)

            if leptonfilter == True:
                continue
            histlist[1].Fill(zmass1)
            histlist[1].Fill(zmass2)

    b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/{}'.format('datastacked.root'), "RECREATE")
    b.cd()
    for hist in histlist:
        hist.Write()  
    b.Close()  
        # hist_2d.Write()
        # histm4l.Write()
        # print(len(meerleptons))

    
m2l(datafilelist)
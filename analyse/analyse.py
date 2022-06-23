import ROOT
import numpy as np

lumi_data = 10

bigfiles = ['mc_363490.llll.4lep.root',
'mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

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


def analyse(filelist):
    cutlist = ['cut0', 'cut1', 'cut2', 'cut3' , 'cut4', 'cut5', 'cut6']
    for bestand in filelist:
        m4lhistlist = []
        m2lhistlist = []
        pthistlist = []

        for cut in cutlist:
            m4lhistlist.append(ROOT.TH1F('m4l'+ cut,"plot m4l", 23, 80000, 170000))
            m2lhistlist.append(ROOT.TH1F('m2l'+ cut, "dileptonmass; invmass; events", 1000, 0, 120000))

        
        f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
        tree = f.Get("mini")
        number_entries = tree.GetEntries()

        for event in range(number_entries):
            tree.GetEntry(event)

            E = tree.lep_E
            px = tree.lep_pt * np.cos(tree.lep_phi)
            py = tree.lep_pt * np.sin(tree.lep_phi)
            pz = tree.lep_pt * np.sinh(tree.lep_eta)

            E4l_squared = np.sum(tree.lep_E) ** 2
            px = tree.lep_pt * np.cos(tree.lep_phi)
            py = tree.lep_pt * np.sin(tree.lep_phi)
            pz = tree.lep_pt * np.sinh(tree.lep_eta)
            p4l_squared = np.sum(px) ** 2 + np.sum(py) ** 2 + np.sum(pz) ** 2

            m4l = (E4l_squared - p4l_squared) ** 0.5
            
            finalmcWeight = tree.XSection * 1000 * lumi_data * tree.mcWeight * 1/tree.SumWeights * \
            tree.scaleFactor_LepTRIGGER * tree.scaleFactor_ELE * tree.scaleFactor_MUON * tree.scaleFactor_PILEUP
            
            m4lhistlist[0].Fill(m4l, finalmcWeight)
            
            sfos = True
            leptonfilter = False
            jetfilter = False
            istight = True
            ptfilter = False
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
                    pairs_found.append([index0, index1])
            
            endpairs = []
            endm2l = []
            
            if len(pairs_found) == 0:
                sfos = False

            
            nGoodLeptons = 0
            for i in range(4):
                if tree.lep_isTightID[i] == False: 
                    istight = False
                if tree.lep_pt[i] < ptlist[i]:
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
            
            nGoodJets = 0
            for ijet in range(0, len(tree.jet_pt) ):
                goodJet = isGoodJet(tree, ijet) 

                if not goodJet: continue

                nGoodJets += 1
            if nGoodJets != len(tree.jet_pt):
                jetfilter = True 
            
            
            
            if sfos == False:
                continue
            

            checkpair = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
            otherpair = [0,1,2,3]
            m2l_total = []
            mass_Z = 91000 # MeV

            m2ls_per_event = []
            pairs_found = []
            meerleptons = []

            zmass1 = None
            zmass2 = None

            if len(tree.lep_type) > 4:
                # print(event)
                meerleptons.append(event)
            
            for i,j in checkpair: 
                    if tree.lep_charge[i] == - tree.lep_charge[j] and tree.lep_type[i] == tree.lep_type[j]:
                        pairs_found.append([i,j])
                        m2l = ((E[i] + E[j]) ** 2 - ((px[i] + px[j]) ** 2 + (py[i] + py[j]) ** 2 + (pz[i] + pz[j]) ** 2)) ** 0.5
                        m2ls_per_event.append(m2l)

            if len(pairs_found) == 2:
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

            
            m2lhistlist[1].Fill(zmass1, finalmcWeight)
            m2lhistlist[1].Fill(zmass2, finalmcWeight)
            m4lhistlist[1].Fill(m4l, finalmcWeight)

            if leptonfilter == True:
                continue
            m2lhistlist[2].Fill(zmass1, finalmcWeight)
            m2lhistlist[2].Fill(zmass2, finalmcWeight)
            m4lhistlist[2].Fill(m4l, finalmcWeight)

            if jetfilter == True:
                continue
            m2lhistlist[3].Fill(zmass1, finalmcWeight)
            m2lhistlist[3].Fill(zmass2, finalmcWeight)
            m4lhistlist[3].Fill(m4l, finalmcWeight)

            if ptfilter == True:
                continue
            m2lhistlist[4].Fill(zmass1, finalmcWeight)
            m2lhistlist[4].Fill(zmass2, finalmcWeight)
            m4lhistlist[4].Fill(m4l, finalmcWeight)

            if istight == False:
                continue
            m2lhistlist[5].Fill(zmass1, finalmcWeight)
            m2lhistlist[5].Fill(zmass2, finalmcWeight)
            m4lhistlist[5].Fill(m4l, finalmcWeight)

            
            
        b = ROOT.TFile.Open('/user/ksmits/BachelorProject/analyse/{}'.format(bestand), "RECREATE")
        b.cd()
        for hist in m4lhistlist:
            hist.Write()  
        for hist in m2lhistlist:
            hist.Write()
        b.Close()
analyse(bigfiles)
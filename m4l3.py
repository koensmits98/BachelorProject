import ROOT
import numpy as np

lumi_data = 10

higgsandZZ = ["mc_345060.ggH125_ZZ4lep.4lep.root" ,\
"mc_363490.llll.4lep.root"]

higgs = ['mc_345060.ggH125_ZZ4lep.4lep.root']

bigfiles = ['mc_363490.llll.4lep.root',
'mc_361106.Zee.4lep.root',
'mc_361107.Zmumu.4lep.root',
'mc_410000.ttbar_lep.4lep.root',
'mc_345336.ZH125J_qqWW2lep.4lep.root',
'mc_345337.ZH125J_llWW2lep.4lep.root',
'mc_363491.lllv.4lep.root',
'mc_345060.ggH125_ZZ4lep.4lep.root']

goodfileswithout = [
'mc_341155.VBFH125_tautaull.4lep.root', \
'mc_341947.ZH125_ZZ4lep.4lep.root', \
'mc_341964.WH125_ZZ4lep.4lep.root', \
'mc_344235.VBFH125_ZZ4lep.4lep.root', \
'mc_345323.VBFH125_WW2lep.4lep.root', \
'mc_345324.ggH125_WW2lep.4lep.root', \
'mc_345325.WpH125J_qqWW2lep.4lep.root', \
'mc_345327.WpH125J_lvWW2lep.4lep.root', \
'mc_345445.ZH125J_vvWW2lep.4lep.root', \
'mc_361108.Ztautau.4lep.root', \
'mc_363356.ZqqZll.4lep.root', \
'mc_363358.WqqZll.4lep.root', \
'mc_363492.llvv.4lep.root', \
'mc_410000.ttbar_lep.4lep.root', \
'mc_410011.single_top_tchan.4lep.root', \
'mc_410012.single_antitop_tchan.4lep.root', \
'mc_410013.single_top_wtchan.4lep.root', \
'mc_410014.single_antitop_wtchan.4lep.root', \
'mc_410025.single_top_schan.4lep.root', \
'mc_410026.single_antitop_schan.4lep.root']

otherfiles = ['mc_361107.Zmumu.4lep.root',\
'mc_410000.ttbar_lep.4lep.root',\
'mc_345336.ZH125J_qqWW2lep.4lep.root',\
'mc_345337.ZH125J_llWW2lep.4lep.root',\
'mc_363491.lllv.4lep.root',\
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

range1 = [100, 0, 400000]
range2 = [25, 80000, 170000]

def m4lhist(filelist):
    histnames = ['m4lhist', 'cut1', 'cut2', 'cut3' , 'cut4', 'cut5', 'cut6']
    k = 0
    for bestand in filelist:
        histlist = []
        for histname in histnames:
            histlist.append(ROOT.TH1F(histname,"plot m4l", 23, 80000, 170000))
            print(histlist)
        directory = '/data/atlas/users/mvozak/opendata/4lep/MC/{}'.format(bestand)
        print(directory)
        f = ROOT.TFile.Open(directory, 'READ')
        tree = f.Get('mini')
        print(tree)
        number_entries = tree.GetEntries()

        for event in range(number_entries):
            # print(event)
            tree.GetEntry(event)
            E4l_squared = np.sum(tree.lep_E) ** 2
            px = tree.lep_pt * np.cos(tree.lep_phi)
            py = tree.lep_pt * np.sin(tree.lep_phi)
            pz = tree.lep_pt * np.sinh(tree.lep_eta)

            p4l_squared = np.sum(px) ** 2 + np.sum(py) ** 2 + np.sum(pz) ** 2

            m4l = (E4l_squared - p4l_squared) ** 0.5
            
            finalmcWeight = tree.XSection * 1000 * lumi_data * tree.mcWeight * 1/tree.SumWeights * \
            tree.scaleFactor_LepTRIGGER * tree.scaleFactor_ELE * tree.scaleFactor_MUON * tree.scaleFactor_PILEUP

            histlist[0].Fill(m4l, finalmcWeight)

            
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
            histlist[1].Fill(m4l, finalmcWeight)
            
            if tree.lep_n > 4:
                continue
            histlist[2].Fill(m4l, finalmcWeight)
            
            if leptonfilter == True:
                continue
            histlist[3].Fill(m4l, finalmcWeight)
            
            if ptfilter == True:
                continue
            histlist[4].Fill(m4l, finalmcWeight)

            if jetfilter == True:
                continue
            histlist[5].Fill(m4l, finalmcWeight)
            if istight == False:
                continue    
            histlist[6].Fill(m4l, finalmcWeight)

        b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lrecreate/{}'.format(bestand), "RECREATE")
        b.cd()
        k += 1
        print(k)
        for i in range(len(histlist)):
            histlist[i].Write()
        b.Close()

m4lhist(bigfiles)

histparameters1 = [100, 0, 400000]
histparameters2 = [23, 80000 , 170000]


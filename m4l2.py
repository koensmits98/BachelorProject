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

otherfiles = ['mc_361107.Zmumu.4lep.root',\
'mc_410000.ttbar_lep.4lep.root',\
'mc_345336.ZH125J_qqWW2lep.4lep.root',\
'mc_345337.ZH125J_llWW2lep.4lep.root',\
'mc_363491.lllv.4lep.root',\
'mc_345060.ggH125_ZZ4lep.4lep.root']

#  def isGoodLepton(tree, ilep):
#  if( (tree.lep_pt[ilep] > 5000.) and  
#      ( abs( tree.lep_eta[ilep]) < 2.5) and 
#      ( (tree.lep_ptcone30[ilep]/tree.lep_pt[ilep]) < 0.3) and
#      ( (tree.lep_etcone20[ilep] / tree.lep_pt[ilep]) < 0.3 ) ):
#     return True
#  else: 
#     return False

# def isGoodMuon(tree, ilep, lv):
#   if( abs(tree.lep_type[ilep] ) == 13  and
#     ( abs(tree.lep_trackd0pvunbiased[ilep])/tree.lep_tracksigd0pvunbiased[ilep] < 3) and
#     ( abs(tree.lep_z0[ilep]*ROOT.TMath.Sin( lv.Theta() )) < 0.5) ):
#           return True
#   else: 
#      return False

# def isGoodElectron(tree, ilep, lv):
#   if( abs(tree.lep_type[ilep] ) == 11  and
#     ( tree.lep_pt[ilep] > 7000. )      and 
#     ( abs( tree.lep_eta[ilep]) < 2.47) and 
#     ( abs(tree.lep_trackd0pvunbiased[ilep])/tree.lep_tracksigd0pvunbiased[ilep] < 5) and
#     ( abs(tree.lep_z0[ilep]*ROOT.TMath.Sin( lv.Theta() )) < 0.5) 
#     ):
#         return True
#   else: return False




def m4lhist(filelist):
    histnames = ['m4lhist', 'cut1', 'cut2', 'cut3']
    k = 0
    for bestand in filelist:
        histlist = []
        for histname in histnames:
            histlist.append(ROOT.TH1F(histname,"plot m4l",100, 0, 400000))
            print(histlist)
        # for i in range(len(histlist)):
        #     print(histlist[i])
        directory = '/data/atlas/users/mvozak/opendata/4lep/MC/{}'.format(bestand)
        # print(bestand)
        # print(histlist)
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
            ptcone = False
            etcone = False
            etfilter = False
            ptfilter = False
            jetfilter = False
            ptlist = [25, 15, 10, 7]

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

            for i in range(3):
                if tree.lep_isTightID[i] == False: 
                    istight = False
                if tree.lep_ptcone30[i]/tree.lep_pt[i] > 0.15:
                    ptcone = True
                if tree.lep_etcone20 < 0 or abs(tree.lep_etcone20[i]/tree.lep_pt[i]) > 0.15:   
                    etcone = True
                if tree.lep_etcone20[i] > 2000:
                    etfilter = True
                if tree.lep_pt[i] < ptlist[i]:
                    ptfilter = True
            for i in range(tree.jet_n):
                if tree.jet_pt[i] < 25000:
                    jetfilter = True
                if tree.jet_jvt[i] < 0.59:
                    jetfilter = True
            

            if sfos == False:
                continue
            histlist[1].Fill(m4l, finalmcWeight)
            if istight == False or ptcone == True or etcone == True or ptfilter == True:
                continue
            histlist[2].Fill(m4l, finalmcWeight)
            if jetfilter == True or etfilter == True :
                continue
            histlist[3].Fill(m4l, finalmcWeight)



        b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(bestand), "RECREATE")
        # b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(filename), "RECREATE")
        b.cd()
        k += 1
        print(k)
        # print(len(histlist))
        print(histlist)
        for i in range(len(histlist)):
            histlist[i].Write()
        # del histlist

# m4lhist(otherfiles)


m4lhist(['mc_363490.llll.4lep.root'])
m4lhist(['mc_361106.Zee.4lep.root'])
m4lhist(['mc_361107.Zmumu.4lep.root'])
m4lhist(['mc_410000.ttbar_lep.4lep.root'])
m4lhist(['mc_345336.ZH125J_qqWW2lep.4lep.root'])
m4lhist(['mc_345337.ZH125J_llWW2lep.4lep.root'])
m4lhist(['mc_363491.lllv.4lep.root'])
m4lhist(['mc_345060.ggH125_ZZ4lep.4lep.root'])











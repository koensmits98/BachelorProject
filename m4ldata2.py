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



def m4lstacked(filelist):
    histnames = ['m4lhist', 'cut1', 'cut2', 'cut3']
    histlist = []
    for histname in histnames:
        histlist.append(ROOT.TH1F(histname,"plot m4l",100, 0, 400000))
    

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
            histlist[1].Fill(m4l)
            if istight == False or ptcone == True or etcone == True or ptfilter == True:
                continue
            histlist[2].Fill(m4l)
            if jetfilter == True or etfilter == True :
                continue
            histlist[3].Fill(m4l)

            


    b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format('datastacked.root'), "RECREATE")
        
    
    # b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(filename), 'recreate')
    b.cd()
    for i in range(len(histlist)):
        histlist[i].Write()

m4lstacked(datafilelist)
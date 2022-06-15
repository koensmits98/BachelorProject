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

def m4lstacked(filelist, cut, filename):
    stackedhist = ROOT.TH1F('m4lhist',"plot m4l",100, 0, 400000)
     
    for bestand in filelist:
        f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/Data/{}".format(bestand), 'READ')
        tree = f.Get('mini')
        number_entries = tree.GetEntries()
        
        for event in range(number_entries):
            tree.GetEntry(event)
            
            istight = True
            ptcone = False
            etcone = False
            etfilter = False
            ptfilter = False
            ptlist = [25, 15, 15, 7]
            jetfilter = False

            for i in range(3):
                if tree.lep_isTightID[i] == False: 
                    istight = False
                if tree.lep_ptcone30[i]/tree.lep_pt[i] > 0.15:
                    ptcone = True
                if tree.lep_etcone20 < 0 or abs(tree.lep_etcone20[i]/tree.lep_pt[i]) > 0.15:   
                    etcone = True
                # print(tree.lep_etcone20)
                if tree.lep_etcone20[i] > 2000:
                    etfilter = True
                if tree.lep_pt[i] < ptlist[i]:
                    ptfilter = True
            for i in range(tree.jet_n):
                if tree.jet_pt[i] < 25000:
                    jetfilter = True
                if tree.jet_jvt[i] < 0.59:
                    jetfilter = True
            
            if cut == True:
                if istight == False or ptcone == True or etcone == True or ptfilter == True or jetfilter == True or etfilter == True:
                    continue

            E4l_squared = np.sum(tree.lep_E) ** 2
            px = tree.lep_pt * np.cos(tree.lep_phi)
            py = tree.lep_pt * np.sin(tree.lep_phi)
            pz = tree.lep_pt * np.sinh(tree.lep_eta)

            p4l_squared = np.sum(px) ** 2 + np.sum(py) ** 2 + np.sum(pz) ** 2

            m4l = (E4l_squared - p4l_squared) ** 0.5

            stackedhist.Fill(m4l)

    # b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(bestand), "RECREATE")
        
    
    b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m4lhists/{}'.format(filename), 'recreate')
    b.cd()
    stackedhist.Write()

m4lstacked(datafilelist, True, 'datastackedcut1.root')
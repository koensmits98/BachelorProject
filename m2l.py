import ROOT
import numpy as np

datafilelist = ["data_A.4lep.root",\
"data_B.4lep.root" ,\
"data_C.4lep.root",\
"data_D.4lep.root" ]

datastacked = ['datastacked.root']

ZZ = ['mc_363490.llll.4lep.root']

higgs = ['mc_345060.ggH125_ZZ4lep.4lep.root']

higgsandZZ = ['mc_363490.llll.4lep.root',\
'mc_345060.ggH125_ZZ4lep.4lep.root']

higgsfiles = ['mc_341122.ggH125_tautaull.4lep.root' ,\
'mc_341155.VBFH125_tautaull.4lep.root' ,\
'mc_341947.ZH125_ZZ4lep.4lep.root' ,\
'mc_341964.WH125_ZZ4lep.4lep.root' ,\
'mc_344235.VBFH125_ZZ4lep.4lep.root' ,\
'mc_345060.ggH125_ZZ4lep.4lep.root' ,\
'mc_345323.VBFH125_WW2lep.4lep.root' ,\
'mc_345324.ggH125_WW2lep.4lep.root' ,\
'mc_345325.WpH125J_qqWW2lep.4lep.root' ,\
'mc_345327.WpH125J_lvWW2lep.4lep.root' ,\
'mc_345336.ZH125J_qqWW2lep.4lep.root' ,\
'mc_345337.ZH125J_llWW2lep.4lep.root' ,\
'mc_345445.ZH125J_vvWW2lep.4lep.root']

lumi_data = 10



def m2l(filelist):
    for bestand in filelist:
        f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
        tree = f.Get("mini")
        number_entries = tree.GetEntries()

        hist = ROOT.TH1F('m2l', "dileptonmass; invmass; events", 1000, 0, 120000)
        
        meerleptons = []

        for event in range(number_entries):
            tree.GetEntry(event)

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

            finalmcWeight = tree.XSection * 1000 * lumi_data * tree.mcWeight * 1/tree.SumWeights * tree.scaleFactor_LepTRIGGER * tree.scaleFactor_ELE * tree.scaleFactor_MUON
            
            if len(tree.lep_type) > 4:
                # print(event)
                meerleptons.append(event)
            
            for i,j in checkpair: 
                    if tree.lep_charge[i] == - tree.lep_charge[j] and tree.lep_type[i] == tree.lep_type[j]:
                        pairs_found.append([i,j])
                        m2l = ((E[i] + E[j]) ** 2 - ((px[i] + px[j]) ** 2 + (py[i] + py[j]) ** 2 + (pz[i] + pz[j]) ** 2)) ** 0.5
                        m2ls_per_event.append(m2l)

            if len(pairs_found) == 2:
                hist.Fill(m2ls_per_event[0], finalmcWeight)
                hist.Fill(m2ls_per_event[1], finalmcWeight)
                
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

                hist.Fill(bestm2l,finalmcWeight)
                hist.Fill(m2ls_per_event[index], finalmcWeight)
                
                # hist_2d.Fill(bestm2l, m2ls_per_event[index], finalmcWeight)
                # histm4l.Fill(bestm2l + m2ls_per_event[index], finalmcWeight)
        
        # scale1 = hist.Integral()
        # hist.Scale(1/scale1)
        # hist.SetLineColor(ROOT.kBlack) 
        # hist.SetLineWidth(2) 
        # hist.SetFillColor(ROOT.kAzure)
        # hist.Draw("HIST")

        b = ROOT.TFile.Open('/user/ksmits/BachelorProject/m2lhists/{}'.format(bestand), "RECREATE")
        b.cd()
        hist.Write()    
        # hist_2d.Write()
        # histm4l.Write()
        # print(len(meerleptons))

m2l(higgsfiles)



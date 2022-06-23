import ROOT
import numpy as np

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
    histnames = ['m2l, cut1', 'cut2', 'cut3']
    
    for bestand in filelist:
        f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
        tree = f.Get("mini")
        number_entries = tree.GetEntries()

        hist = ROOT.TH1F('m2l', "dileptonmass; invmass; events", 1000, 0, 120000)
        
        meerleptons = []

        for event in range(number_entries):
            tree.GetEntry(event)

            istight = True
            ptcone = False
            etcone = False
            ptfilter = False
            ptlist = [25, 15, 10, 7]

            for i in range(3):
                if tree.lep_isTightID[i] == False: 
                    istight = False
                if tree.lep_ptcone30[i]/tree.lep_pt[i] > 0.15:
                    ptcone = True
                if abs(tree.lep_etcone20[i]/tree.lep_E[i]) > 0.15:   
                    etcone = True
                if tree.lep_pt[i] < ptlist[i]:
                    ptfilter = True
            if cut == True:
                if istight == False or ptcone == True or etcone == True or ptfilter == True:
                    continue

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

# m2l(goodfileswithout)




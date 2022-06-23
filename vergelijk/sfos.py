import ROOT
import numpy as np

def vergelijk(bestand):
    canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)

    f = ROOT.TFile.Open("/data/atlas/users/mvozak/opendata/4lep/MC/{}".format(bestand))
    tree = f.Get('mini')
    hist = ROOT.TH1F('ratio', "ratio", 100, -5 , 5 )

    sfos = 0
    for event in range(1000):
        tree.GetEntry(event)

        
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
        # print(pairs_found)
        endpairs = []
        endm2l = []
        
        if len(pairs_found) != 0:
            sfos +=1
            # print(sfos)
        ratio = float(0.001*sfos)
    print(bestand, ratio)

            
    # imagename = 'eta{}.jpg'.format(bestand)
    # hist.Draw()
    # canvas.Print(imagename)

vergelijk('mc_361106.Zee.4lep.root')
vergelijk('mc_361107.Zmumu.4lep.root')
vergelijk('mc_345060.ggH125_ZZ4lep.4lep.root')
vergelijk('mc_345336.ZH125J_qqWW2lep.4lep.root')
vergelijk('mc_345337.ZH125J_llWW2lep.4lep.root')
vergelijk('mc_363490.llll.4lep.root')
vergelijk('mc_410000.ttbar_lep.4lep.root')
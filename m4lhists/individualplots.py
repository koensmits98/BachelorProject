import ROOT

goodfiles = ['mc_341122.ggH125_tautaull.4lep.root', 'mc_341155.VBFH125_tautaull.4lep.root', 'mc_341947.ZH125_ZZ4lep.4lep.root', 'mc_341964.WH125_ZZ4lep.4lep.root', 'mc_344235.VBFH125_ZZ4lep.4lep.root', 'mc_345060.ggH125_ZZ4lep.4lep.root', 'mc_345323.VBFH125_WW2lep.4lep.root', 'mc_345324.ggH125_WW2lep.4lep.root', 'mc_345325.WpH125J_qqWW2lep.4lep.root', 'mc_345327.WpH125J_lvWW2lep.4lep.root', 'mc_345336.ZH125J_qqWW2lep.4lep.root', 'mc_345337.ZH125J_llWW2lep.4lep.root', 'mc_345445.ZH125J_vvWW2lep.4lep.root', 'mc_361106.Zee.4lep.root', 'mc_361107.Zmumu.4lep.root', 'mc_361108.Ztautau.4lep.root', 'mc_363356.ZqqZll.4lep.root', 'mc_363358.WqqZll.4lep.root', 'mc_363490.llll.4lep.root', 'mc_363491.lllv.4lep.root', 'mc_363492.llvv.4lep.root', 'mc_410000.ttbar_lep.4lep.root', 'mc_410011.single_top_tchan.4lep.root', 'mc_410012.single_antitop_tchan.4lep.root', 'mc_410013.single_top_wtchan.4lep.root', 'mc_410014.single_antitop_wtchan.4lep.root', 'mc_410025.single_top_schan.4lep.root', 'mc_410026.single_antitop_schan.4lep.root', 'mc_410155.ttW.4lep.root', 'mc_410218.ttee.4lep.root', 'mc_410219.ttmumu.4lep.root']

# for bestand in goodfiles:
#     canvas = ROOT.TCanvas("canvas","plot a variable", 800, 600)
#     f = ROOT.TFile.Open(bestand, "READ")
#     hist = f.Get('m4lhist')

#     hist.Draw('hist')

#     canvas.Print('{}.jpg'.format(bestand))

f = ROOT.TFile.Open('mc_363493.lvvv.4lep.root', "READ")

tree = f.Get('m4lhist')

for i in range(10):
    tree.GetEntry(i)
    print(tree.XSection)



from rootpy import ROOT

import numpy as np

with open('accuracy.dat', 'r') as infile:
    points = [[float(x) for x in l.split()] for l in infile]

    N = np.array([p[0] for p in points])
    A = np.array([p[1] for p in points])

ROOT.gStyle.SetOptStat(0)

c = ROOT.TCanvas('c1')
c.SetLogx(True)

graph = ROOT.TGraph(len(N), N, A)
graph.SetTitle('Monte Carlo Integral of 1 - x^2')
graph.GetXaxis().SetTitle('Number of Points Drawn')
graph.GetYaxis().SetTitle('Integral')
graph.Draw("APL")

reference = ROOT.TGraph(2, np.array([1, 1000000]), np.array([4/3.0, 4/3.0]))
reference.SetLineColor(2)
reference.Draw("L")

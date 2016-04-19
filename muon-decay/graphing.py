#!/usr/bin/env python

import json

# sadly we can't do this in python3
from rootpy.plotting import Hist
from rootpy import ROOT

with open('lifetimes.json', 'r') as infile:
    lifetimes = json.loads(infile.read())

print len(lifetimes)

h = Hist(50, 0, max(lifetimes)/1000.0, title="Muon Lifetimes")

for l in lifetimes:
    h.Fill(l/1000.0)

ROOT.gStyle.SetOptStat(0)
h.GetXaxis().SetTitle('Lifetime (\mu s)')
h.Scale(1.0/len(lifetimes))
f = ROOT.TF1('f1', '[0]*exp(-x/[1])', 0, max(lifetimes)/1000.0)
f.SetParameters(1, 1)
h.Fit(f)
h.Draw("HIST")
f.Draw("SAME")

#!/usr/bin/env python

import json

# sadly we can't do this in python3
from rootpy.plotting import Hist
from rootpy import ROOT

with open('result-values.json', 'r') as infile:
    result_sample = json.loads(infile.read())


h = Hist(500, min(result_sample), max(result_sample), title="Result Distribution")

for l in result_sample:
    h.Fill(l)

ROOT.gStyle.SetOptStat(0)
h.Fit('gaus')
f = h.GetFunction('gaus')
h.Draw("HIST")
f.Draw("SAME")

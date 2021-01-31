"""
DSC 530 T303 (2213-1)

Week 7 - 7.1 Exercise: Using data from the NSFG, make a scatter plot of birth weight versus mother’s age. Plot
percentiles of birth weight versus mother’s age. Compute Pearson’s and Spearman’s cor‐
relations. How would you characterize the relationship between these variables?

Author: Rajasekharreddy Karna
01/31/2021

"""

from __future__ import print_function
import thinkplot
import thinkstats2
import sys
import math
import first
import numpy as np

def ScatterPlot(ages, weights, alpha=1.0):
    thinkplot.Scatter(ages, weights, alpha=alpha)
    thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     xlim=[10, 45],
                     ylim=[0, 15],
                     legend=False)

def HexBin(ages, weights, bins=None):
    thinkplot.HexBin(ages, weights, bins=bins)
    thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     legend=False)

def BinnedPercentiles(df):
    bins = np.arange(10, 48, 3)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)

    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

    thinkplot.Save(root='chap07scatter3',
                   formats=['jpg'],
                   xlabel="mother's age (years)",
                   ylabel='birth weight (lbs)')

def main(script):
    thinkstats2.RandomSeed(17)
    
    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    BinnedPercentiles(live)

    ages = live.agepreg
    weights = live.totalwgt_lb
    print('thinkstats2 Corr', thinkstats2.Corr(ages, weights))
    print('thinkstats2 SpearmanCorr', 
          thinkstats2.SpearmanCorr(ages, weights))

    ScatterPlot(ages, weights, alpha=0.1)
    thinkplot.Save(root='chap07scatter1', 
                   legend=False,
                   formats=['jpg'])

if __name__ == '__main__':
    main(*sys.argv)

"""
Analysis Notes:
1) The scatterplot correlation shows a weak relationship between the variables.
2) Pearson = 0.068, Spearman = 0.094. Plotting percentiles relationship shows it is non-linear.  We can observe the birth weight increasing in the range of mother's age from 15 to 25.  After that it is weaker.
"""
"""
DSC 530 T303 (2213-1)

Week 10 - 
Exercise 13.1: In NSFG Cycles 6 and 7, the variable cmdivorcx contains the date of divorce for the respondent’s first marriage, if applicable, encoded in century-months.

Compute the duration of marriages that have ended in divorce, and the duration, so far, of marriages that are ongoing. Estimate the hazard and survival function for the duration of marriage.

Use resampling to take into account sampling weights, and plot data from several re‐samples to visualize sampling error.

Consider dividing the respondents into groups by decade of birth, and possibly by age at first marriage.

Author: Rajasekharreddy Karna
02/22/2021
"""

from __future__ import print_function
import thinkplot
import thinkstats2
import survival
import pandas
import numpy as np

def CleanData(resp):
    resp.cmdivorcx.replace([9998, 9999], np.nan, inplace=True)
    resp['notdivorced'] = resp.cmdivorcx.isnull().astype(int)
    resp['duration'] = (resp.cmdivorcx - resp.cmmarrhx) / 12.0
    resp['durationsofar'] = (resp.cmintvw - resp.cmmarrhx) / 12.0
    month0 = pandas.to_datetime('1899-12-15')
    dates = [month0 + pandas.DateOffset(months=cm) 
             for cm in resp.cmbirth]
    resp['decade'] = (pandas.DatetimeIndex(dates).year - 1900) // 10

def ResampleDivorceCurve(resps):
    for _ in range(41):
        samples = [thinkstats2.ResampleRowsWeighted(resp) 
                   for resp in resps]
        sample = pandas.concat(samples, ignore_index=True)
        PlotDivorceCurveByDecade(sample, color='#225EA8', alpha=0.1)


def PlotDivorceCurveByDecade(samples, **options):
    """Groups respondents by decade and plots survival curves.

    groups: GroupBy object
  
        thinkplot.Config(xlabel='Age (years)',
                 ylabel='Prob unmarried',
                 xlim=[13, 45],
                 ylim=[0, 1])    
    """
    thinkplot.Show(xlabel='years',
                   axis=[0, 28, 0, 1])


def ResampleDivorceCurveByDecade(resps):
    for i in range(41):
        samples = [thinkstats2.ResampleRowsWeighted(resp) 
                   for resp in resps]
        sample = pandas.concat(samples, ignore_index=True)
        groups = sample.groupby('decade')
        if i == 0:
            survival.AddLabelsByDecade(groups, alpha=0.7)

        EstimateSurvivalByDecade(groups, alpha=0.2)
    thinkplot.Save(root='survival7',
                   xlabel='years',
                   axis=[0, 28, 0, 1])

def EstimateSurvivalByDecade(groups, **options):
    thinkplot.PrePlot(len(groups))
    for name, group in groups:
        print(name, len(group))
        _, sf = EstimateSurvival(group)
        thinkplot.Plot(sf, **options)

def EstimateSurvival(resp):
    complete = resp[resp.notdivorced == 0].duration
    ongoing = resp[resp.notdivorced == 1].durationsofar
    hf = survival.EstimateHazardFunction(complete, ongoing)
    sf = hf.MakeSurvival()
    return hf, sf

def main():
    resp6 = survival.ReadFemResp2002()
    CleanData(resp6)
    married6 = resp6[resp6.evrmarry==1]
    resp7 = survival.ReadFemResp2010()
    CleanData(resp7)
    married7 = resp7[resp7.evrmarry==1]
    ResampleDivorceCurveByDecade([married6, married7])

if __name__ == '__main__':
    main()

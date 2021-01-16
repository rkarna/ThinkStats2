"""
DSC 530 T303 (2213-1)
Purpose of Program: Compute the median, mean, skewness and Pearson’s skewness of the resulting sample.
What fraction of households reports a taxable income below the mean? How do the
results depend on the assumed upper bound?

Week 5 - 5.2 Exercise: Modeling Distributions and PDFs

Author: Rajasekharreddy Karna
01/16/2020

"""

from __future__ import print_function
import thinkplot
import thinkstats2
import density
import hinc
import numpy as np


def InterpolateSample(df, log_upper=4.0):
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.log_lower[0] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.log_upper[41] = log_upper

    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, int(row.freq))
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample


def main():
    df = hinc.ReadData()
    log_sample = InterpolateSample(df, log_upper=4.0)

    log_cdf = thinkstats2.Cdf(log_sample)
    thinkplot.Cdf(log_cdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='CDF')

    sample = np.power(10, log_sample)
    mean, median = density.Summarize(sample)

    cdf = thinkstats2.Cdf(sample)
    print('cdf[mean]', cdf[mean])

    pdf = thinkstats2.EstimatedPdf(sample)
    thinkplot.Pdf(pdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='PDF')


if __name__ == "__main__":
    main()


"""
Output:

With log_lower=3
    mean 62490.11985588097
    std 50335.43661200617
    median 49247.54376068318
    skewness 1.2208933251563383
    pearson skewness 0.7892596341583735
    cdf[mean] 0.6016920086886932

With log_upper=4
    mean 63190.30168734388
    std 50413.27490160796
    median 49844.797605412416
    skewness 1.222493635820741
    pearson skewness 0.794166066853101
    cdf[mean] 0.6024514527429813

With log_upper=6
    mean 74278.7075311872
    std 93946.92996347835
    median 51226.45447894046
    skewness 4.949920244429583
    pearson skewness 0.7361258019141782
    cdf[mean] 0.660005879566872

With log_upper=7
    mean 124267.39722164697
    std 559608.5013743473
    median 51226.45447894046
    skewness 11.603690267537793
    pearson skewness 0.39156450927742087
    cdf[mean] 0.8565630665207663

With a higher upper bound:
    - The moment-based skewness increases
    - The Pearson skewness goes down due to that increasing the upper bound has a modest effect on the mean and effect on standard deviation.  
    - Represents Pearson skewness is not working well as a summary statistic.

"""

"""
DSC 530 T303 (2213-1)

Week 7 - 8.1 Exercise: In this chapter we used x¯ and median to estimate μ, and found that x¯ yields lower MSE.
Also, we used S2 and Sn-12 to estimate σ, and found that S2 is biased and Sn-12 is unbiased.Run similar experiments to see if x¯ and median are biased estimates of μ. Also checkwhether S2 or Sn-12 yields a lower MSE.
Week 7 - 8.2 Exercise:Suppose that you draw a sample with size n = 10 from an exponential distribution with λ = 2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval.
Repeat the experiment with a few different values of n and make a plot of standard error versus n.

Author: Rajasekharreddy Karna
01/31/2021

"""

from __future__ import print_function, division

import thinkstats2
import thinkplot
import random
import math
import numpy as np

from scipy import stats
from estimation import RMSE, MeanError

def Estimate1(n=7, m=100000):
    mu = 0
    sigma = 1

    means = []
    medians = []
    for _ in range(m):
        xs = [random.gauss(mu, sigma) for i in range(n)]
        xbar = np.mean(xs)
        median = np.median(xs)
        means.append(xbar)
        medians.append(median)
    print('mean error in xbar = ', MeanError(means, mu))
    print('mean error in median = ', MeanError(medians, mu))

def Estimate2(n=7, m=100000):
    mu = 0
    sigma = 1

    estimates1 = []
    estimates2 = []
    for _ in range(m):
        xs = [random.gauss(mu, sigma) for i in range(n)]
        biased = np.var(xs)
        unbiased = np.var(xs, ddof=1)
        estimates1.append(biased)
        estimates2.append(unbiased)
    print('RMSE biased value = ', RMSE(estimates1, sigma**2))
    print('RMSE unbiased value = ', RMSE(estimates2, sigma**2))

def SimulateSample(lam=2, n=100, m=10000):
    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

    estimates = []
    for j in range(m):
        xs = np.random.exponential(1/lam, n)
        lamhat = 1/np.mean(xs)
        estimates.append(lamhat)

    stderr = RMSE(estimates, lam)
    print('standard error value =', stderr)

    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval = ', ci)
    VertLine(ci[0])
    VertLine(ci[1])

    # plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Save(root='estimation2',
                   xlabel='estimate',
                   ylabel='CDF',
                   title='Sampling distribution')

    return stderr

def main():
    thinkstats2.RandomSeed(17)

    Estimate1()
    Estimate2()

    for n in [100, 1000, 10000]:
        stderr = SimulateSample(n=n)
        print(n, stderr)

if __name__ == '__main__':
    main()


"""
Data Analaysis:
1) 
mean error in xbar =  0.0009731646745573738
mean error in median =  0.0009977514720499036
xbar and median mean error values in lower, so neither one is obviously biased.
2) Around 10% unbiased estimate in RMSE calculation.  And the difference holds up as m increases.
RMSE biased value =  0.5160608912798944
RMSE unbiased value =  0.57826602081194
3) With sample size 100, standard error value = 0.20473491433621238; confidence interval =  (1.7085078203363588, 2.3741928476744736)
As sample size increases, standard error and the width are decreasing:
100      0.204    (1.7, 2.3)
1000     0.063    (1.9, 2.1)
10000    0.019    (1.9, 2.0)
"""
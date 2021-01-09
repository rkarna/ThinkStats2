"""
DSC 530 T303 (2213-1)
Purpose of Program: In “Summarizing Distributions” on page 22 we computed the mean of a sample by
adding up the elements and dividing by n. If you are given a PMF, you can still compute
the mean, but the process is slightly different:
x¯ = ∑
i
pi xi
where the xi
 are the unique values in the PMF and pi = PMF (xi). Similarly, you can
compute variance like this:
S
2 = ∑
i
pi (xi
- x¯ )
2
Write functions called PmfMean and PmfVar that take a Pmf object and compute the
mean and variance. To test these methods, check that they are consistent with the
methods Mean and Var provided by Pmf.

Week 4 - 4.2 Exercise: Probability Mass Functions and Cumulative Distribution Functions

Author: Rajasekharreddy Karna
01/09/2020

"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import first
import thinkstats2
import thinkplot


def PmfMean(pmf):
    """Computes the mean of a PMF.

    Returns:
        float mean
    """
    mean = 0.0
    for x, p in pmf.d.items():
        mean += p * x
    return mean


def PmfVar(pmf, mu=None):
    """Computes the variance of a PMF.

    Args:
        mu: the point around which the variance is computed;
            if omitted, computes the mean

    Returns:
        float variance
    """
    if mu is None:
        mu = pmf.Mean()

    var = 0.0
    for x, p in pmf.d.items():
        var += p * (x - mu) ** 2
    return var


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()

    # test PmfMean and PmfVar
    prglngth = live.prglngth
    pmf = thinkstats2.Pmf(prglngth)
    mean = PmfMean(pmf)
    var = PmfVar(pmf)

    assert(mean == pmf.Mean())
    assert(var == pmf.Var())
    print('# capture the mean value')
    print('Mean Value length', mean)
    print('# capture the var value')
    print('Var Value length', var)
    print('# capture the mean/ preg length value')
    print('mean/var preg length', mean, var)
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

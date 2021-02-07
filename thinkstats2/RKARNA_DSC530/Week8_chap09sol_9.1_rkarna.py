"""
DSC 530 T303 (2213-1)

Week 8 - 9.1 Exercise: As sample size increases, the power of a hypothesis test increases, which means it is
more likely to be positive if the effect is real. Conversely, as sample size decreases, the
test is less likely to be positive even if the effect is real.

To investigate this behavior, run the tests in this chapter with different subsets of the
NSFG data. You can use thinkstats2.SampleRows to select a random subset of the rows
in a DataFrame.

What happens to the p-values of these tests as the sample size decreases? What is the
smallest sample size that yields a positive test?

Author: Rajasekharreddy Karna
02/07/2021
"""

from __future__ import print_function, division
import thinkstats2
import hypothesis
import first

def RunTests(live, iters=100):
    n = len(live)
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]

    # Pregnancy Lengths
    data = firsts.prglngth.values, others.prglngth.values
    ht = hypothesis.DiffMeansPermute(data)
    p1 = ht.PValue(iters=iters)

    # Birth Weights
    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    ht = hypothesis.DiffMeansPermute(data)
    p2 = ht.PValue(iters=iters)

    # Correlation
    live2 = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    data = live2.agepreg.values, live2.totalwgt_lb.values
    ht = hypothesis.CorrelationPermute(data)
    p3 = ht.PValue(iters=iters)

    # Pregnancy Lengths (chi-squared)
    data = firsts.prglngth.values, others.prglngth.values
    ht = hypothesis.PregLengthTest(data)
    p4 = ht.PValue(iters=iters)

    print('%d\t%0.2f\t%0.2f\t%0.2f\t%0.2f' % (n, p1, p2, p3, p4))

def main():
    thinkstats2.RandomSeed(18)
    live, firsts, others = first.MakeFrames()
    n = len(live)
    for _ in range(7):
        sample = thinkstats2.SampleRows(live, n)
        RunTests(sample)
        n //= 2
if __name__ == '__main__':
    main()

""" 
Analysis results:

 n       Mean Preg.Length   Birth Weight   Correlation   Chi-Square Preg.Length
9148	    0.22	            0.00	     0.00	           0.00
4574	    0.14	            0.00	     0.00	           0.00
2287	    0.96	            0.02	     0.00	           0.00
1143	    0.90	            0.08	     0.09	           0.11
571	        0.34	            0.51	     0.04	           0.01
285 	    0.96	            0.69	     0.36	           0.63
142	        0.15	            0.49	     0.82	           0.38

Conclusion: Test pattern are erratic, with couple of positive tests even at very small sample sizes (100).

"""
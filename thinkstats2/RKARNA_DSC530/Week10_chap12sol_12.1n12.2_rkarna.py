"""
DSC 530 T303 (2213-1)

Week 10 - 
Exercise 12.1: The linear model I used in this chapter has the obvious drawback that it is linear, and there is no reason to expect prices to change linearly over time. We can add flexibility to the model by adding a quadratic term, as we did in “Nonlinear Relationships” on page 133.

Use a quadratic model to fit the time series of daily prices, and use the model to generate predictions. You will have to write a version of RunLinearModel that runs that quadratic model, but after that you should be able to reuse code in timeseries.py to generate predictions.

Exercise 12.2: Write a definition for a class named SerialCorrelationTest that extends HypothesisTest from “HypothesisTest” on page 102. It should take a series and a lag as data, compute the serial correlation of the series with the given lag, and then compute the p-value of the observed correlation.

Use this class to test whether the serial correlation in raw price data is statistically significant. Also test the residuals of the linear model and (if you did the previous exercise), the quadratic model.

Author: Rajasekharreddy Karna
02/15/2021
"""

from __future__ import print_function, division
import thinkplot
import numpy as np
import regression
import timeseries
import statsmodels.formula.api as smf

def RunQuadraticModel(daily):
    daily['years2'] = daily.years**2
    model = smf.ols('ppg ~ years + years2', data=daily)
    results = model.fit()
    return model, results

def PlotQuadraticModel(daily, name):
    model, results = RunQuadraticModel(daily)
    regression.SummarizeResults(results)
    timeseries.PlotFittedValues(model, results, label=name)
    thinkplot.Save(root='Output_Timeseries1',
                   title='Fitted Val',
                   xlabel='yr',
                   xlim=[-0.2, 4],
                   ylabel='price per gram ($)')

    timeseries.PlotResidualPercentiles(model, results)
    thinkplot.Save(root='Output_Timeseries2',
                   title='Residual',
                   xlabel='yr',
                   ylabel='price per gram ($)')

    years = np.linspace(0, 10, 200)
    thinkplot.Scatter(daily.years, daily.ppg, alpha=0.1, label=name)
    timeseries.PlotPredictions(daily, years, func=RunQuadraticModel)
    thinkplot.Save(root='Output_Timeseries3',
                   title='Predict',
                   xlabel='yr',
                   xlim=[years[0]-0.1, years[-1]+0.1],
                   ylabel='price per gram ($)')

def main(name):
    transactions = timeseries.ReadData()
    dailies = timeseries.GroupByQualityAndDay(transactions)
    name = 'high'
    daily = dailies[name]
    PlotQuadraticModel(daily, name)

if __name__ == '__main__':
    import sys
    main(*sys.argv)


"""
Output Results: 
Intercept   13.7   (0)
years   -1.12   (5.86e-38)
years2   0.113   (4.82e-07)
R^2 0.4553
Std(ys) 1.096
Std(res) 0.809
"""
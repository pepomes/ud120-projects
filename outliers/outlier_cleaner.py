#!/usr/bin/python
from operator import itemgetter
clean_up_perc = 10

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    temp = [(i, (x - y) ** 2) for (i, x, y) in
            zip(xrange(len(predictions)), predictions, net_worths)]
    temp = sorted(temp, key=itemgetter(1))
    cleaned_data = []

    # your code goes here
    cleaned_data = [(ages[temp[i][0]],
                    net_worths[temp[i][0]],
                    temp[i][1])
                    for i in xrange(len(predictions) *
                                    (100 - clean_up_perc) / 100)]
    return cleaned_data

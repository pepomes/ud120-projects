#!/usr/bin/python

import pickle
import numpy
import matplotlib.pyplot as plt
import sys
import random as r
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


def dist_a_b(a, b):
    """Distance between two points."""
    return sum([(y - x) ** 2 for (x, y) in zip(a, b)])


def rand_list(n=1000):
    """Return a list of random tuples. n is the number of tuples."""
    res = []
    res += [(r.random()/2, r.random()/2) for i in xrange(n)]
    res += [(1 - r.random()/2, 1 - r.random()/2) for i in xrange(n)]
    return res


def k_mean(data, n_clusters=2):
    means = [(r.random(), r.random()) for i in xrange(n_clusters)]
    dist = [apply(dist_a_b, x]
coord = rand_list()
for i in coord:
    plt.scatter(*i, color="r")

plt.show()

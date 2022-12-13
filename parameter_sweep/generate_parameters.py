import numpy as np
from itertools import product
import os
import csv

# some parameter values
p1 = np.arange(.2, .7, .1).round(2)
p2 = [0, 1]
p3 = np.arange(1, 31)

# all possible combinations between parameters + check of length
combinations = list(product(*[p1 ,p2, p3]))
assert len(combinations) == (len(p1) * len(p2) * len(p3))

# set your working directory
os.chdir(r"/user/gent/435/vsc43506/parameter_sweep")

# title for your csv file
header = ["learning_rate", "syncing", "sub_id"]

# actual writing to file
with open('parameters.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(header)
    [writer.writerow(list(c)) for c in combinations]

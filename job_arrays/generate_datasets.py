import os
import numpy as np

# make the required folders
W_DIR = r"/data/gent/435/vsc43506/job_arrays"
[os.makedirs(os.path.join(W_DIR, f)) for f in ["input", "output"] if not os.path.exists(os.path.join(W_DIR, f))]

# generate some random arrays and save them
[np.save(os.path.join(W_DIR, "input", "dataset_{}".format(i)), np.random.random((100, 100))) for i in range(1, 101)]

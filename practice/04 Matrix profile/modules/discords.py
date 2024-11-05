import numpy as np

from modules.utils import *


def top_k_discords(mp, top_k: int, excl_zone):
    """
    Find the top-k discords based on matrix profile

    Parameters
    ---------
    matrix_profile: the matrix profile structure
    top_k: number of discords

    Returns
    --------
    discords: top-k discords (indices, distances to its nearest neighbor and the nearest neighbors indices)
    """
 
    discords_idx = []
    discords_dist = []
    discords_nn_idx = []

    # INSERT YOUR CODE
    top_k_idxs = []
    argsort_mp = np.argsort(mp['mp'])
    for i in range (1, len(argsort_mp)+1):
      idx = argsort_mp[-i]
      flag =True
      for top_k_idx in top_k_idxs:
          if abs (top_k_idx - idx) < excl_zone:
            flag = False
      if flag:
          top_k_idxs.append(idx)
      if len (top_k_idxs) == top_k:
          break

    return top_k_idxs

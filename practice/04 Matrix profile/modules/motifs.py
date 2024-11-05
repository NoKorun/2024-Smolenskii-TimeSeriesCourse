import numpy as np

from modules.utils import *
import stumpy


def top_k_motifs(ts, matrix_profile: dict, top_k: int = 3) -> dict:
    """
    Find the top-k motifs based on matrix profile

    Parameters
    ---------
    matrix_profile: the matrix profile structure
    top_k : number of motifs

    Returns
    --------
    motifs: top-k motifs (left and right indices and distances)
    """

    motifs_idx = []
    motifs_dist = []

    # INSERT YOUR CODE
    motifs = stumpy.motifs(ts, matrix_profile['mp'], cutoff=np.nanmean(matrix_profile['mp']), max_motifs=top_k) 
    motifs_idx = motifs[1]
    motifs_dist = motifs[0]

    return {
        "indices" : motifs_idx,
        "distances" : motifs_dist
        }

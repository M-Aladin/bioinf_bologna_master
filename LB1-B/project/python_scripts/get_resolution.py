"""usage: python3 get_resolution.py clustered_id_path > output_path"""

from pypdb import get_entity_info
import sys
from math import inf


def resolution(pdb_id):
    metadata = get_entity_info(pdb_id)
    reso = float(metadata.get('resolution', inf))
    return reso


def cluster_rep(clust_ids):
    """
    Create a dictionary and populate it like so:
    for each cluster, the key will be an increasing integer, the value will be a list such that [id, resolution]
    :param clust_ids: a file with all the clustered ids
    """
    representatives = dict()
    f = open(clust_ids)
    i = 0
    for cluster in f:  # cluster aka line
        representatives[i] = [' ', inf]  # we populate the dictionary like so
        ids = cluster.rstrip().split()
        for id_chain in ids:
            pdb_id = id_chain.split('_')[0]  # take away the chain ID for a moment
            pdb_res = resolution(pdb_id)
            if pdb_res <= representatives[i][1]:
                representatives[i] = [id_chain, pdb_res]
        i += 1
    for rep in representatives.keys():
        print(representatives[rep][0])  # print in output all the representative structures
        # in id_chain format
    f.close()


def cluster_sort(clust_ids):
    """
    Input is a file containing in each line a cluster (easily converted to list)
    Get resolution for each list item, zip the lists, sort the tuples for resolution,
    reconstitute id-only list and print it (since we are going to manually select the ids later,
    we don't really care about format here)
    """
    f = open(clust_ids)
    for cluster in f:
        resolutions = []
        ids = cluster.rstrip().split()  # we get a list of id_chain elements
        for id_chain in ids:
            pdb_id = id_chain.split('_')[0]
            pdb_res = resolution(pdb_id)
            resolutions.append(pdb_res)
        sorted_ids = list(zip(resolutions, ids))
        sorted_ids = sorted(sorted_ids)
        print(sorted_ids)
    f.close()


if __name__ == '__main__':
    # tentative = resolution('1gyc')
    # print(type(tentative))
    clustered_ids = sys.argv[1]
    cluster_sort(clustered_ids)

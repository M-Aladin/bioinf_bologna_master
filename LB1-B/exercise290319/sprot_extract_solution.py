#!/usr/bin/python

"""
1-4-19
this implementation actually teaches me that when I write scripts to be used within the shell envo,
I should use the sys module much more
"""

import sys


def get_fasta(sid, fasta):
    """
    :param sid: list of seq identifiers
    :param fasta: output?
    :return:
    """
    f = open(fasta)
    c = 0  # state variable can be 0 or 1
    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            tid = line.split('|')[1]
        if tid == sid:  # is the id we found in the header corresponding to the one we passed as input?
            c = 1
            print(line)
            continue
        else:
            c = 0
        # if c == 1:
        #     print(line)


def get_list_fasta(lid, fasta):
    f = open(fasta)
    c = 0
    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            tid = line.split('|')[1]
        if tid in lid:
            c = 1
        else:
            c = 0
        if c == 1:
            print(line)


if __name__ == "__main__":
    # sid = sys.argv[1]
    fid = sys.argv[1]  # seq ids stored in a file passed as input
    fasta=sys.argv[2]
    # get_fasta(sid, fasta)
    lid = open(fid).read().split('\n')  # open the file containing ids and make a list out of it
    get_list_fasta(lid, fasta)

#!/usr/bin/env/python

"""
Usage: ./sprot_extract.py <query ID file> <uniprot_sprot.fasta>
"""
import sys


def get_list_fasta(lid, fasta):
    """
    :param lid: list of sequence ids
    :param fasta: uniprot_sprot.fasta
    :return: None
    """
    f = open(fasta)
    c = 0
    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            tid = line.split('|')[1]
        if lid.get(tid, False):
            c = 1
            print(line)
        else:
            c = 0


if __name__ == "__main__":
    # sid = sys.argv[1]
    fid = sys.argv[1]  # seq ids stored in a file passed as input
    fasta = sys.argv[2]  # uniprot_sprot.fasta path
    # get_fasta(sid, fasta)
    lid = dict([(i, True) for i in open(fid).read().split('\n')])
    get_list_fasta(lid, fasta)

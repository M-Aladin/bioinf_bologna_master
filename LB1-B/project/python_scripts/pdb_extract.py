"""
Usage: python pdb_extract.py <query ID file> <pdb_seqres.txt>
"""

import sys


def get_list_fasta(lid, fasta):
    """
    :param lid: dictionary of sequence ids
    :param fasta: pdb_seqres.txt
    :return: None
    """
    f = open(fasta)
    c = 0
    tid = ''
    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            tid = line.split()[0].lstrip('>')
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
    # create dictionary with the input file
    lid = dict([(i, True) for i in open(fid).read().split('\n')])
    get_list_fasta(lid, fasta)

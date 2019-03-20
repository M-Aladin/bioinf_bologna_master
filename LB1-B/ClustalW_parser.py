#!/usr/bin/env/python3

# data structure for seqs: dictionary
# particularly suitable because uniprot ids are unique and are used as keys

import sys


def parse_aln(alnfile):
    d = dict()
    f = open(alnfile)
    for line in f:
        line = line.rstrip()  # remove newline char
        v = line.split()  # separate the two columns of the clw format
        d[v[0]] = d.get(v[0], '')  # check if the key is already present, return empty str otherwise
        d[v[0]] = d[v[0]] + v[1]  # the value will be the seq corresponding to the key
    f.close()
    return d


# the problem with the dictionary is that we don't retrieve an element (e.g. wrong key),
# the program crashes.
# the get method lets us circumvent this, as we can pass an optional argument which will serve
# as default value.


if __name__ == "__main__":
    aln = sys.argv[1]
    d = parse_aln(aln)
    for k in d.keys():
        print(k, d[k])

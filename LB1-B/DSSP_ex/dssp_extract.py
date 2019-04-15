import sys

Norm_Acc = {"A": 106.0, "B": 160.0,
            "C": 135.0, "D": 163.0, "E": 194.0,
            "F": 197.0, "G": 84.0, "H": 184.0,
            "I": 169.0, "K": 205.0, "L": 164.0,
            "M": 188.0, "N": 157.0, "P": 136.0,
            "Q": 198.0, "R": 248.0, "S": 130.0,
            "T": 142.0, "V": 142.0, "W": 227.0,
            "X": 180.0, "Y": 222.0, "Z": 196.0}


def parse_dssp(dsspfyle, ch='A'):
    dssphandler = open(dsspfyle)
    dssp = []
    for line in dssphandler:
        if line.lstrip().startswith('#'):
            break  # I jump to the point where the parsable section starts. Tested on the shell, it should work.
    for line in dssphandler:
        if line[11] == ch:
            r = line[13]
            ss = line[16]
            if ss == ' ':
                ss = 'C'
            pos = line[5:10].strip()
            acc = float(line[35:38])
            phi = float(line[103:109])
            psi = float(line[109:115])
            racc = min(acc / Norm_Acc[r], 1.0)  # oh wow what a nice way to fix it
            v = [r, pos, ch, ss, racc, phi, psi]
            dssp.append(v)
    return dssp


# relative accessibility calculation: we need to use a dictionary

if __name__ == '__main__':
    dsspfile = sys.argv[1]
    chain = sys.argv[2]
    dssp = parse_dssp(dsspfile, chain)
    for l in dssp:
        print('\t'.join([str(i) for i in l]))

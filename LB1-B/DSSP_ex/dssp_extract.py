import sys


def parse_dssp(dsspfile, ch = 'A'):
    dssphandler = open(dsspfile)
    for line in dssphandler:
        if line.lstrip().startswith('#'):
            break  # I jump to the point where the parsable section starts. Tested on the shell, it should work.
    for line in dssphandler:
        if line[11] == ch:
            r = line[13]
            ss = line[16]
            if ss == ' ':
                ss = 'C'
            acc = float(line[35:38])
            phi = float(line[103:109])
            psi = float(line[109:115])
            v = [r, ss, acc, phi, psi]


# relative accessibility calculation: we need to use a dictionary

if __name__ == '__main__':
    dssp = sys.argv[1]
    outfile = sys.argv[2]

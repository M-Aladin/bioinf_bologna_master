"""
In principle we know how a FASTA format works.
The script should take as input a list of IDs, traverse the sprot file, when a header is found AND it contains
an ID that you are looking for, you start printing until you find another header.
"""


def fasta_mapper(multifasta, filesize):
    """
    Takes a file handler of a multifasta and returns a dictionary where keys are AC numbers and values are the
    whole sequences in fasta format
    """
    index = dict()
    firstheader = multifasta.readline()
    key = firstheader.split("|")[1]
    value = firstheader
    while multifasta.tell() < filesize:  # repeat cycle until end of the file is reached

        # read a new line
        a = multifasta.readline()

        if a.startswith(">sp"):  # a new header is found
            index[key] = value  # save current variables in dictionary

            # overwrite key and value with new header data
            key = a.split("|")[1]
            value = a

        else:  # the line is part of the previous entry
            value += a  # sum the sequence to the previous value of a (i.e. concatenate string)

    index[key] = value  # save the last sequence

    return index
    # value = "is for the way you look at me"
    # key = "l"
    # index[key] = value


def dprint(d):
    """
    print dictionary in a decent way
    """
    print("{")
    for i in d.keys():
        print(i + ":")
        print(d[i])
    print("}")


if __name__ == "__main__":
    import os
    fastapath = "/home/maryblue/bioinfogit/LB1-B/exercise290319/somesequences.fasta"
    f = open(fastapath)
    size = os.path.getsize(fastapath)
    indexed = fasta_mapper(f, size)
    f.close()
    dprint(indexed)
    print(indexed["Q67475"])

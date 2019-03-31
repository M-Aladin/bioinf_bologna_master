from multifasta_mapper import fastamap
from multifasta_mapper import fastafind
import os

# create dictionary "database" from uniprot_sprot.fasta
dbpath = "/home/maryblue/bioinfogit/LB1-B/exercise290319/uniprot_sprot.fasta"
database = open(dbpath)
size = os.path.getsize(dbpath)
d = fastamap(database, size)
database.close()

# extract desired AC from the dictionary
inputpath = "/home/maryblue/bioinfogit/LB1-B/exercise290319/kunitz_hsa_AC"
outputpath = inputpath + ".fasta"
output = open(outputpath, 'w')
input = open(inputpath)

for line in input:
    key = line.rstrip()
    output.write(d[key])

input.close()
output.close()

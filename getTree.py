from Bio.Phylo.Applications import _Fasttree
import Bio.Phylo as Phylo
from Bio import SeqIO
import networkx, pylab
import numpy as np

fasttree_exe = "./FastTree"
file = "glob"

# Load all protein names
handle = open(file+".ali", "rU")
strucParse = struc = SeqIO.parse(handle, "pir")
protein_names = [i.id for i in struc]

# Convert file so fasttree can use it
sequences = SeqIO.convert(file+".ali", "pir", file+".fasta", "fasta")

cmd = _Fasttree.FastTreeCommandline(fasttree_exe, input=file+".fasta", out='ExampleTree.tree')

tree = Phylo.read('ExampleTree.tree', "newick")

cherryX = []
cherryY = []
count = 0

# # Find leaf pairs
# for i in tree.find_clades():
#     # Is node before leaves
#     if i.is_preterminal():
#         count += 1
#         # Can't use len for iter. Needs list.
#         sub_tree = list(i.find_clades())
#         if len(sub_tree) > 2:
#             j1, j2, j3 = sub_tree
#             cherryY.append(j2, j3)
#             cherryX.append(j3, j2)

net = Phylo.to_networkx(tree)
adj_mat = networkx.adjacency_matrix(net)
print adj_mat
np.savetxt("test.csv", adj_mat.todense())

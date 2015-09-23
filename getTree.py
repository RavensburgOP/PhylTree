from Bio.Phylo.Applications import _Fasttree
import Bio.Phylo as Phylo
from Bio import SeqIO

fasttree_exe = "./FastTree"
file = "glob"

sequences = SeqIO.convert(file+".ali", "pir", file+".fasta", "fasta")

cmd = _Fasttree.FastTreeCommandline(fasttree_exe, input=file+".fasta", out='ExampleTree.tree')


tree = Phylo.read('ExampleTree.tree', "newick")

for i in tree.find_clades():
    # Is node before leaves
    if i.is_preterminal():
        # Can't use len for iter. Needs list.
        sub_tree = list(i.find_clades())
        if len(sub_tree) > 2:
            j1, j2, j3 = sub_tree
            # Distance between two leaves == similarity
            print j1.distance(j2, j3)

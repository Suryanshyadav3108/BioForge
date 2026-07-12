"""
=====================================================
BioForge Phylogenetic Tree Module

By Suryansh Singh Yadav
=====================================================
"""

from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
from Bio import Phylo
import matplotlib.pyplot as plt


def build_tree(alignment_file, output_image="phylogenetic_tree.png"):
    """
    Build a Neighbor-Joining phylogenetic tree from a multiple sequence alignment.
    """

    alignment = AlignIO.read(alignment_file, "fasta")

    calculator = DistanceCalculator("identity")

    distance_matrix = calculator.get_distance(alignment)

    constructor = DistanceTreeConstructor()

    tree = constructor.nj(distance_matrix)

    plt.figure(figsize=(10, 6))

    Phylo.draw(tree, do_show=False)

    plt.savefig(output_image, dpi=300, bbox_inches="tight")

    plt.close()

    return output_image
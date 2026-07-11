"""
==========================================
BioForge RNA Module
Author : Aman Yadav
Version : 1.0
==========================================
"""


def transcribe_dna(sequence):
    """
    Convert DNA into RNA
    """

    sequence = sequence.upper()

    return sequence.replace("T", "U")


def reverse_rna(sequence):
    """
    Reverse RNA Sequence
    """

    return sequence[::-1]


def rna_length(sequence):
    """
    Return RNA Length
    """

    return len(sequence)


def count_rna_bases(sequence):
    """
    Count RNA Bases
    """

    counts = {}

    for base in "AUGC":

        counts[base] = sequence.count(base)

    return counts
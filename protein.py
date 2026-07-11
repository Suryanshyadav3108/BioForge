"""
=====================================================
BioForge Protein Module
Author  : Suryansh Singh Yadav
Version : 2.0
=====================================================
"""

# Standard Genetic Code (64 Codons)

CODON_TABLE = {

    # Phenylalanine
    "TTT": "F", "TTC": "F",

    # Leucine
    "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L",
    "CTA": "L", "CTG": "L",

    # Isoleucine
    "ATT": "I", "ATC": "I",
    "ATA": "I",

    # Methionine (START)
    "ATG": "M",

    # Valine
    "GTT": "V", "GTC": "V",
    "GTA": "V", "GTG": "V",

    # Serine
    "TCT": "S", "TCC": "S",
    "TCA": "S", "TCG": "S",
    "AGT": "S", "AGC": "S",

    # Proline
    "CCT": "P", "CCC": "P",
    "CCA": "P", "CCG": "P",

    # Threonine
    "ACT": "T", "ACC": "T",
    "ACA": "T", "ACG": "T",

    # Alanine
    "GCT": "A", "GCC": "A",
    "GCA": "A", "GCG": "A",

    # Tyrosine
    "TAT": "Y", "TAC": "Y",

    # Histidine
    "CAT": "H", "CAC": "H",

    # Glutamine
    "CAA": "Q", "CAG": "Q",

    # Asparagine
    "AAT": "N", "AAC": "N",

    # Lysine
    "AAA": "K", "AAG": "K",

    # Aspartic Acid
    "GAT": "D", "GAC": "D",

    # Glutamic Acid
    "GAA": "E", "GAG": "E",

    # Cysteine
    "TGT": "C", "TGC": "C",

    # Tryptophan
    "TGG": "W",

    # Arginine
    "CGT": "R", "CGC": "R",
    "CGA": "R", "CGG": "R",
    "AGA": "R", "AGG": "R",

    # Glycine
    "GGT": "G", "GGC": "G",
    "GGA": "G", "GGG": "G",

    # STOP
    "TAA": "*",
    "TAG": "*",
    "TGA": "*"
}


def translate_dna(sequence):

    sequence = sequence.upper()

    protein = ""

    for i in range(0, len(sequence)-2, 3):

        codon = sequence[i:i+3]

        amino = CODON_TABLE.get(codon, "X")

        protein += amino

    return protein


def protein_length(protein):

    return len(protein)


def amino_acid_count(protein):

    counts = {}

    for aa in protein:

        counts[aa] = counts.get(aa, 0) + 1

    return counts


def has_start_codon(sequence):

    return sequence.startswith("ATG")


def has_stop_codon(sequence):

    stop_codons = ["TAA", "TAG", "TGA"]

    return sequence[-3:] in stop_codons
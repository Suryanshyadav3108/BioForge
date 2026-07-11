"""
=====================================================
BioForge ORF Finder
Author : Suryansh Singh Yadav
Version : 1.0
=====================================================
"""

STOP_CODONS = ["TAA", "TAG", "TGA"]


def find_orf(sequence):

    sequence = sequence.upper()

    start = sequence.find("ATG")

    if start == -1:

        return None

    for i in range(start, len(sequence), 3):

        codon = sequence[i:i+3]

        if codon in STOP_CODONS:

            return sequence[start:i+3]

    return None


def orf_length(orf):

    if orf is None:

        return 0

    return len(orf)


def has_orf(sequence):

    return find_orf(sequence) is not None

#temporary
if __name__ == "__main__":

    dna = "CCCATGGCTTTTGAATAG"

    orf = find_orf(dna)

    print("ORF")

    print(orf)

    print()

    print("Length")

    print(orf_length(orf))
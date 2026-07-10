"""
==========================================
BioForge DNA Module
Author : Aman Yadav
==========================================
"""

# DNA Complement Mapping
DNA_COMPLEMENT = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}


def get_length(sequence):
    """Return sequence length."""
    return len(sequence)


def count_bases(sequence):
    """Count A, T, G and C."""

    counts = {}

    for base in "ATGC":
        counts[base] = sequence.count(base)

    return counts


def gc_content(sequence):
    """Calculate GC percentage."""

    if len(sequence) == 0:
        return 0

    gc = sequence.count("G") + sequence.count("C")

    return (gc / len(sequence)) * 100


def at_content(sequence):
    """Calculate AT percentage."""

    if len(sequence) == 0:
        return 0

    at = sequence.count("A") + sequence.count("T")

    return (at / len(sequence)) * 100


def reverse_sequence(sequence):
    """Return reverse DNA sequence."""

    return sequence[::-1]


def reverse_complement(sequence):
    """Return reverse complement."""

    complement = ""

    for base in sequence:
        complement += DNA_COMPLEMENT[base]

    return complement[::-1]
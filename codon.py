"""
=====================================================
BioForge Codon Analysis Module

By Suryansh Singh Yadav
=====================================================
"""

from collections import Counter
from validation import validate_dna


def split_codons(sequence):
    """
    Split DNA sequence into codons.
    """

    sequence = sequence.upper().strip()

    valid, invalid = validate_dna(sequence)

    if not valid:
        raise ValueError("Invalid DNA sequence")

    codons = []

    for i in range(0, len(sequence) - 2, 3):
        codons.append(sequence[i:i+3])

    return codons


def codon_frequency(sequence):
    """
    Count codon frequency.
    """

    codons = split_codons(sequence)

    return dict(Counter(codons))


def total_codons(sequence):
    """
    Total codons.
    """

    return len(split_codons(sequence))


def most_frequent_codon(sequence):
    """
    Return most common codon.
    """

    freq = codon_frequency(sequence)

    if not freq:
        return None

    codon = max(freq, key=freq.get)

    return codon, freq[codon]


def generate_codon_report(sequence):

    freq = codon_frequency(sequence)

    report = []

    report.append("=" * 45)
    report.append("BioForge Codon Usage Report")
    report.append("=" * 45)

    for codon, count in sorted(freq.items()):

        report.append(f"{codon} : {count}")

    report.append("")

    report.append(f"Total Codons : {total_codons(sequence)}")

    most = most_frequent_codon(sequence)

    if most:

        report.append(
            f"Most Frequent : {most[0]} ({most[1]})"
        )

    return "\n".join(report)
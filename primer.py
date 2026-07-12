"""
=====================================================
BioForge Primer Design Module

By Suryansh Singh Yadav
=====================================================
"""

from dna import reverse_complement
from validation import validate_dna


def gc_content(sequence):
    sequence = sequence.upper()
    gc = sequence.count("G") + sequence.count("C")
    return (gc / len(sequence)) * 100 if sequence else 0


def melting_temperature(sequence):
    """
    Wallace Rule:
    Tm = 2(A+T) + 4(G+C)
    """

    sequence = sequence.upper()

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    return 2 * (a + t) + 4 * (g + c)


def design_primers(sequence, primer_length=20):

    sequence = sequence.upper().strip()

    valid, invalid = validate_dna(sequence)

    if not valid:
        raise ValueError("Invalid DNA sequence")

    if len(sequence) < primer_length:
        raise ValueError("Sequence is shorter than primer length")

    forward = sequence[:primer_length]

    reverse = reverse_complement(
        sequence[-primer_length:]
    )

    return {
        "forward": forward,
        "reverse": reverse,
        "length": primer_length,
        "gc": round(gc_content(forward), 2),
        "tm": melting_temperature(forward)
    }


def primer_quality(primer):

    gc = gc_content(primer)

    if 40 <= gc <= 60:
        return "GOOD ✅"

    elif 35 <= gc <= 65:
        return "ACCEPTABLE ⚠"

    return "POOR ❌"
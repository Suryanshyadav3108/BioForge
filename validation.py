"""
BioForge Validation Module
"""


def validate_dna(sequence):
    """
    Validate a DNA sequence.

    Returns:
        (True, [])
        OR
        (False, invalid_bases)
    """

    valid_bases = {"A", "T", "G", "C"}

    invalid_bases = []

    for base in sequence:

        if base not in valid_bases:

            if base not in invalid_bases:

                invalid_bases.append(base)

    if invalid_bases:

        return False, invalid_bases

    return True, []
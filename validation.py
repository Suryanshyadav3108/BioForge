"""
==========================================
BioForge Validation Module
Author : Aman Yadav
Version : 0.5
==========================================
"""

# Valid DNA Bases
VALID_BASES = {"A", "T", "G", "C"}


def validate_dna(sequence):
    """
    Validate a DNA sequence.

    Parameters
    ----------
    sequence : str
        DNA sequence entered by the user.

    Returns
    -------
    tuple
        (True, [])
            If the sequence is valid.

        (False, invalid_bases)
            If invalid characters are found.
    """

    # Empty sequence check
    if len(sequence) == 0:
        return False, ["Empty Sequence"]

    invalid_bases = []

    for base in sequence:

        if base not in VALID_BASES:

            if base not in invalid_bases:
                invalid_bases.append(base)

    if len(invalid_bases) > 0:
        return False, invalid_bases

    return True, []
"""
=====================================================
BioForge Sequence Alignment Module

By Suryansh Singh Yadav
=====================================================
"""

from validation import validate_dna


def align_sequences(seq1, seq2):
    """
    Simple global alignment without gaps.
    """

    seq1 = seq1.upper().strip()
    seq2 = seq2.upper().strip()

    valid1, _ = validate_dna(seq1)
    valid2, _ = validate_dna(seq2)

    if not valid1 or not valid2:
        raise ValueError("Invalid DNA sequence")

    length = min(len(seq1), len(seq2))

    aligned1 = ""
    aligned2 = ""
    match_line = ""

    matches = 0
    mismatches = 0

    for i in range(length):

        aligned1 += seq1[i]
        aligned2 += seq2[i]

        if seq1[i] == seq2[i]:
            match_line += "|"
            matches += 1
        else:
            match_line += " "
            mismatches += 1

    similarity = round((matches / length) * 100, 2)

    return {
        "sequence1": aligned1,
        "sequence2": aligned2,
        "match_line": match_line,
        "matches": matches,
        "mismatches": mismatches,
        "length": length,
        "similarity": similarity
    }


def generate_alignment_report(seq1, seq2):

    result = align_sequences(seq1, seq2)

    report = []

    report.append("=" * 55)
    report.append("BioForge Sequence Alignment")
    report.append("=" * 55)

    report.append("")
    report.append(result["sequence1"])
    report.append(result["match_line"])
    report.append(result["sequence2"])
    report.append("")

    report.append(f"Length : {result['length']}")
    report.append(f"Matches : {result['matches']}")
    report.append(f"Mismatches : {result['mismatches']}")
    report.append(f"Similarity : {result['similarity']} %")

    return "\n".join(report)
"""
=====================================================
BioForge Protein Properties

By Suryansh Singh Yadav
=====================================================
"""

from Bio.SeqUtils.ProtParam import ProteinAnalysis


def analyze_protein(protein_sequence):
    """
    Analyze protein properties using Biopython.
    """

    protein = protein_sequence.upper().replace("*", "")

    if len(protein) == 0:
        raise ValueError("Protein sequence is empty.")

    analysis = ProteinAnalysis(protein)

    return {
        "length": len(protein),
        "molecular_weight": round(
            analysis.molecular_weight(), 2
        ),
        "isoelectric_point": round(
            analysis.isoelectric_point(), 2
        ),
        "aromaticity": round(
            analysis.aromaticity(), 3
        ),
        "instability_index": round(
            analysis.instability_index(), 2
        ),
        "gravy": round(
            analysis.gravy(), 3
        ),
        "amino_acid_percent": analysis.amino_acids_percent
    }


def protein_status(instability):

    if instability < 40:
        return "Stable ✅"

    return "Unstable ❌"